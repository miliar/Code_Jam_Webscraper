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


int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		
		int m;
		
		fin >> m;
		
		int ans = 0;
		
		int lastop,lastbp, lastot, lastbt;
		
		lastop=lastbp=1;
		lastot=lastbt=0;
		
		char c;
		
		for(i=0; i<m; i++)
		{
			fin >> c >> k;
			
			if(c=='B')
			{
				j = lastbt + abs(k-lastbp) + 1;
				if(j<=lastot)
					j=lastot+1;
				lastbt=j;
				lastbp=k;
			}
			else {
				j  = lastot + abs(k-lastop) + 1;
				if(j<=lastbt)
					j=lastbt+1;
				lastot=j;
				lastop=k;
			}
		}

		ans = max(lastot,lastbt);
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}
	
	
	return 0;
}

