#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <stack>
#include <queue>
#include <valarray>
#include <cmath>
#include <ctime>
using namespace std;

class Prisoner
{
public:
	Prisoner()
	{
		mBribeCount = 0;
		setExists(true);
	}

	int getBribeCount() const
	{
		return mBribeCount;
	}

	void incrementBribe()
	{
		++mBribeCount;
	}

	bool doesExist() const
	{
		return mExist;
	}

	void setExists(bool val)
	{
		mExist = val;
	}

private:
	int mBribeCount;
	bool mExist;

};



void fillVector(std::vector<Prisoner>& prisoners, int cellCount)
{
	for (int i = 0; i < cellCount; ++i)
	{
		prisoners.push_back(Prisoner());
	}
}

int releasePrisoner(std::vector<Prisoner>& prisoners, int noOfRelease)
{
	int indexOfRelese = noOfRelease - 1;

	prisoners[indexOfRelese].setExists(false);

	int number = 0;
	for (int i = indexOfRelese - 1; i >= 0; --i)
	{
		Prisoner& prisoner = prisoners[i];
		if ( prisoner.doesExist() == false )
		{
			break;
		}
		prisoner.incrementBribe();
		++number;
	}

	for (int r = indexOfRelese + 1; r < prisoners.size(); ++r)
	{
		Prisoner& prisoner = prisoners[r];
		if ( prisoner.doesExist() == false )
		{
			break;
		}
		prisoner.incrementBribe();
		++number;
	}
	return number;
}

int fact(int a)
{
	if (a == 0  || a == 1)
	{
		return 1;
	}
	return a * fact(a-1);
}

int getNumberOfBribes(const std::vector<Prisoner>& prisoners)
{
	int total = 0;
	int cellCount = prisoners.size();
	for (int i = 0; i < cellCount; ++i)
	{
		const Prisoner& prisoner = prisoners[i];
		total += prisoner.getBribeCount();
	}
	return total;
}

int main()
{
    ifstream input("C:\\CodeJam\\in.txt");
    ofstream output("C:\\CodeJam\\out.txt");

    int T;
    input >> T;

    int testCase = 0;
    while(testCase < T)
    {
		int P, Q;
		std::vector<int> prisonerList;
		input >> P >> Q;
		int prisonerCount = Q;
		std::vector<Prisoner> prisoners;
		while(Q--)
		{
			int prisonerId;
			input >> prisonerId;
			prisonerList.push_back(prisonerId);
		}

		std::vector<int> goldList;
		for (int i = 0 ; i < fact(prisonerCount) ; ++i)
		{
			std::next_permutation(prisonerList.begin(), prisonerList.end());
			std::vector<Prisoner> prisoners;
			fillVector(prisoners, P);
			for (int k = 0 ; k < prisonerList.size(); ++k)
			{
				releasePrisoner(prisoners, prisonerList.at(k));
			}
			goldList.push_back(getNumberOfBribes(prisoners));
		}
		
		valarray<int> valArray(&goldList[0], goldList.size());
        output << "Case #" << testCase + 1  << ": " << valArray.min() << std::endl;
		testCase++;
    }

    return 0;
}