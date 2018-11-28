#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

int main()
{
	int T = 0;
	ifstream infile("input.in");
	ofstream outfile("output.txt");
	infile>>T;
	vector<int> S;
	vector<int> p;
	vector<int> N;
	int scores[100][100];
	vector<int> results;
	for(int i = 0; i < T; i++)
	{
		int n, supr, max = 0;
		infile>>n>>supr>>max;
		S.push_back(supr);
		p.push_back(max);
		N.push_back(n);
		for(int j = 0; j < N[i]; j++)
		{
			int total;
			infile>>total;
			scores[i][j] = total;
			
		}
	}
	for(int i = 0; i < T; i++)
	{
		int eachgoogler[100][3];
		int numofg = N[i];
		int counter = 0;
		int surprising = S[i];
		for(int j=0; j<numofg; j++)
		{
			
			int total = scores[i][j];
			eachgoogler[j][0] = ceil((double)total/ (double)3);
			eachgoogler[j][1] = floor((double)total/ (double)3);
			eachgoogler[j][2] = scores[i][j] - ( eachgoogler[j][0] + eachgoogler[j][1]);
			if(surprising > 0  && (eachgoogler[j][0]  < p[i] && eachgoogler[j][2]  < p[i]) && eachgoogler[j][0] > 0 && eachgoogler[j][2] > 0)
			{
				if(j + 1 == numofg)
				{
					eachgoogler[j][0]--;
					eachgoogler[j][2]++;
					surprising--;
				}
				else if(eachgoogler[j][0] + 2 > p[i] && eachgoogler[j][2] + 2 > p[i])
				{
					eachgoogler[j][0]--;
					eachgoogler[j][2]++;
					surprising--;
				}
				else
				{
				}
			}
			if(eachgoogler[j][0] >= p[i] || eachgoogler[j][1] >= p[i] || eachgoogler[j][2] >= p[i])
				counter++;
		}
		results.push_back(counter);
	}
	for(int i = 0; i < T; i++)
	{
		cout<<"Case #"<<i+1<<": "<<results[i]<<endl;
		outfile<<"Case #"<<i+1<<": "<<results[i]<<endl;
	}
	return 0;
}