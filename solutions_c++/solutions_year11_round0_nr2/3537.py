#include <iostream>
#include <string>
#include <sstream>

char const INVALID_CHAR = 0;
char const MIN_CHAR = 'A';
char const MAX_CHAR = 'Z';
unsigned int const LETTER_COUNT = MAX_CHAR - MIN_CHAR + 1;

unsigned int index(char c)
{
	if (c < MIN_CHAR || c > MAX_CHAR)
	{
		throw std::exception("invalid character: out-of-range");
	}
	return c - MIN_CHAR;
}

class LetterSet
{
public:
	LetterSet()
		:	m_bits(0)
	{
	}

	bool insert(char c)
	{
		if (contains(c))
		{
			return false;
		}
		m_bits |= mask(c);
		return true;
	}

	bool contains(char c) const
	{
		return (m_bits & mask(c)) != 0;
	}

private:
	static unsigned int mask(char c)
	{
		return 1 << index(c);
	}

	unsigned int m_bits;
};

struct TestCase
{
	// If combines[x][y] = z, z != INVALID_CHAR, then x and y combine to produce z
	char combines[LETTER_COUNT][LETTER_COUNT]; // by index
	LetterSet opposed[LETTER_COUNT]; // for each element, set of elements to which it is opposed
	std::string invoked;

	TestCase()
	{
		memset(combines, 0, sizeof(combines));
	}
};

std::istream& operator >> (std::istream& stream, TestCase& testCase)
{
	// Read combines
	unsigned int C = 0;
	stream >> C;
	for (unsigned int c = 0; c < C; ++c)
	{
		std::string combineString;
		stream >> combineString;

		// Store the fact that base elements can combine in either order, for easy look-up.
		testCase.combines[index(combineString[0])][index(combineString[1])] = combineString[2];
		testCase.combines[index(combineString[1])][index(combineString[0])] = combineString[2];
	}

	// Read oppositions
	unsigned int D = 0;
	stream >> D;
	for (unsigned int d = 0; d < D; ++d)
	{
		std::string opposeString;
		stream >> opposeString;

		// Store that each element is opposed to the other, for easy look-up.
		testCase.opposed[index(opposeString[0])].insert(opposeString[1]);
		testCase.opposed[index(opposeString[1])].insert(opposeString[0]);
	}

	// Read invocations
	unsigned int N = 0;
	stream >> N;
	stream >> testCase.invoked;

	return stream;
}

int main()
{
	unsigned int T = 0;
	std::cin >> T;
	for (unsigned int t = 0; t < T; ++t)
	{
		TestCase testCase;
		std::cin >> testCase;

		std::string elementList;
		for (std::string::const_iterator iterElement = testCase.invoked.begin();
				iterElement != testCase.invoked.end();
				++iterElement)
		{
			char const invoked = (*iterElement);
			elementList.push_back(invoked);

			if (elementList.size() > 1)
			{
				char const combineResult = testCase.combines[index(invoked)][index(elementList[elementList.size() - 2])];
				if (combineResult != INVALID_CHAR)
				{
					elementList.pop_back(); // remove the second of the pair; just appended
					elementList.back() = combineResult; // replace the first of the pair (was already there) with the result of combination
				}
				else
				{
					// "After you invoke an element, if it isn't immediately combined to form another element,
					//  and it is opposed to something in your element list,
					//  then your whole element list will be cleared."
					LetterSet const& opposedToThis = testCase.opposed[index(invoked)];
					for (std::string::iterator iterOther = elementList.begin();
							iterOther != --elementList.end();
							++iterOther)
					{
						char const otherElement = (*iterOther);
						if (opposedToThis.contains(otherElement))
						{
							elementList.clear();
							break;
						}
					}
				}
			}
		}

		std::ostringstream outputStream;
		outputStream << "Case #" << t + 1 <<": [";
		for (std::string::const_iterator iterElement = elementList.begin();
				iterElement != elementList.end();
				++iterElement)
		{
			outputStream << (*iterElement);
			if (iterElement != (--elementList.end()))
			{
				outputStream << ", ";
			}
		}
		outputStream << "]" << std::endl;

		std::string const output = outputStream.str();
		std::cout << output;
		std::cerr << output;
	}

	return 1;
}