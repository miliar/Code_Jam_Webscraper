#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

unsigned WordLength, DictSize, n_TestCases;

std::vector<std::string> Dict;

void ReadWord();
unsigned TestIt();
std::vector<std::vector<char> >& GetTestCase(std::string& line);
unsigned GetPoss(std::vector<std::vector<char> >& Data, unsigned term = 0, unsigned start = 0, unsigned end=DictSize-1);

int main()
{
	// Get Sizes
	std::cin >> WordLength >> DictSize >> n_TestCases;
	std::cin.ignore();
	for (int i = 0; i < DictSize; i++)
		ReadWord();

	std::sort(Dict.begin(), Dict.end());

	for (int i = 1; i <= n_TestCases; i++)
		std::cout << "Case #" << i << ": " << TestIt() << std::endl;
	return 0;
}

void ReadWord()
{
	char in;
	std::string buffer;
	getline(std::cin, buffer);
	Dict.push_back(buffer);
}

unsigned TestIt()
{
	char in;
	std::string line;
	getline(std::cin, line);

	std::vector<std::vector<char> >& Data = GetTestCase(line);

	return GetPoss(Data);
}

std::vector<std::vector<char> >& GetTestCase(std::string& line)
{
	std::vector<std::vector<char> >* dataptr = new std::vector<std::vector<char> >();


	std::istringstream iss(line);

	for (int i = 0; i < WordLength; i++)
	{
		std::vector<char> buffer;
		if (iss.peek() == '(')
		{
			iss.ignore(); // (
			while (iss.peek() != ')')
			{
				char in;
				iss >> in;
				buffer.push_back(in);
			}
			iss.ignore(); // )
		} else {
			char in;
			iss >> in;
			buffer.push_back(in);
		}
		dataptr->push_back(buffer);
	}
	return *dataptr;
}



unsigned GetPoss(std::vector<std::vector<char> >& Data, unsigned term, unsigned start, unsigned end)
{
	//std::cout << "GetPoss " << term << " S"<< start << " E" << end << " {" << std::endl;

	unsigned ans = 0;
	std::vector<char>& sel = Data[term];
	for (int j = 0; j < sel.size(); j++)
	{
		//std::cout << "Trying character number " << j << "(" << sel[j] << ") {" << std::endl;
		unsigned n_start = 60000;
		unsigned n_end = end;
		for (int i = start; i <= end; i++)
		{
			if (Dict[i][term] == sel[j])
			{
				//std::cout << "Term = " << term << ": Equal: " << Dict[i] << "'s term " << term << std::endl;
				if (term == WordLength -1)
					ans++;
				if (n_start == 60000)
					n_start = i;
			} else if (n_start != 60000 && n_end == end)
				n_end = i-1;
		}
		if (n_start != 60000 && term < WordLength-1)
			ans += GetPoss(Data, term+1, n_start, n_end);
		//std::cout << "}Tried character number " << j << "(" << sel[j] << ")" << std::endl;
	}
	//std::cout << "} GetPoss " << term << " Ans = " << ans << std::endl;
	return ans;
}
