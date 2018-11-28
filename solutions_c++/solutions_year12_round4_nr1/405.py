#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");


int dists[10000];
int lens[10000];

bool havedone[10000];
int maxdone[10000];


int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	cout.precision(9);
	fout.precision(9);
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		
		fin >> n;
		
		for(i=0; i<n; i++)
		{
			fin >> dists[i] >> lens[i];
		}
		
		int target;
		fin >> target;
		
		memset(havedone,0,sizeof(havedone));
		
		havedone[0]=true;
		maxdone[0]=dists[0];
		
		bool isok = false;
		
		int nexttosee = 1;
		
		for(i=0; i<n; i++)
		{
			//cout << i << " " << havedone[i] << " " << maxdone[i] << " " << dists[i] << " " << nexttosee <<  endl;
			if(!havedone[i])
				continue;
			if(dists[i] + maxdone[i] >= target)
			{
				isok=true;
				break;
			}
			
			for( ;nexttosee<n; nexttosee++)
			{
				if(dists[i] + maxdone[i] >= dists[nexttosee])
				{
					havedone[nexttosee]=true;
					maxdone[nexttosee]=min(lens[nexttosee],dists[nexttosee]-dists[i]);
				}
				else {
					break;
				}

			}
		}
		
		
		
		
		cout << "Case #" << ct << ": ";
		fout << "Case #" << ct << ": ";
		
		
		string ans = "YES";
		
		if(!isok)
			ans="NO";
		
		fout << ans << endl;
		cout << ans << endl;
		
	}
	
	
	return 0;
}

