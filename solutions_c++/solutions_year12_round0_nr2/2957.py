#include <iostream>
#include <vector>
#include <string>

using namespace std;

int canMakeScore(int score, int aimingFor)
{
	if(score > 30)
		return 0;

	if(score == 0 && aimingFor == 0)
		return 1;

	int difference = aimingFor-1;
	if(difference < 0)
		difference = 0;

	int differenceSurprising = aimingFor-2;
	if(differenceSurprising < 0)
		difference = 0;

	if(score >= (aimingFor + 2*difference) && score > 0)
		return 1;

	if(score >= (aimingFor + 2*differenceSurprising)  && score > 0)
		return 2;

	return 0;
}


int main(void)
{
	int num_of_testcases = 0;
	vector<int> testcases;
	
	cin >> num_of_testcases;

	for(int i=0; i<num_of_testcases; i++)
	{
		int googlers = 0;
		int surprising = 0;
		int aimingFor = 0;
		int P = 0;

		cin >> googlers >> surprising >> aimingFor;

		for(int j=0; j<googlers; j++)
		{
			int score;
			int canMake;

			cin >> score;
			canMake = canMakeScore(score, aimingFor);
			
			if(canMake == 1)
				P++;
			else if(canMake == 2 && surprising > 0)
			{
				P++;
				surprising--;
			}
		}

		testcases.push_back(P);
	}

	for(int i=0; i<testcases.size(); i++)
	{
		cout << "Case #" << i+1 <<  ": " << testcases[i] << endl;
	}

	return 0;
}