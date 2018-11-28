#include <iostream>
#include <sstream>
#include <vector>

using namespace std;


int findMaxGooglers(int nbSurprising, int limitMin, vector<int> scores)
{
	int maxGooglers = 0;
	
	for(int i=0 ; i<scores.size() ; i++)
	{
		int a, b;
		
		a = b = scores[i] / 3;
		
		if(scores[i] % 3 >= 1)
			a++;
		
		if(scores[i] % 3 >= 2)
			b++;
		
		if(a >= limitMin)
		{
			maxGooglers++;
		}
		else if(a+1 >= limitMin && b > 0 && nbSurprising > 0)
		{
			maxGooglers++;
			nbSurprising--;
		}
	}
	
	return maxGooglers;
}



int main()
{
	int nbCases;
	cin >> nbCases;
	
	for(int i=0 ; i<nbCases ; i++)
	{
		int nbScores;
		int nbSurprising;
		int limitMin;
		
		cin >> nbScores;
		cin >> nbSurprising;
		cin >> limitMin;
		
		vector<int> scores(nbScores);
		
		for(int j=0 ; j<nbScores ; j++)
			cin >> scores[j];
		
		int maxi = findMaxGooglers(nbSurprising, limitMin, scores);
		cout << "Case #" << (i+1) << ": " << maxi << endl;
	}
	
	return 0;
}



