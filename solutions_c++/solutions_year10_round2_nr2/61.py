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

int locs[50];
int speeds[50];

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
		int b,t;
		
		fin >> n >>k >> b >> t;
		for(i=0; i<n; i++)
		{
			fin >> locs[i];
		}
		for(i=0; i<n; i++)
			fin >> speeds[i];
		int oks=0;
		int noks=0;
		int ans = 0;
		for(int x=n-1; x>=0; x--)
		{
			bool isok=false;
			if(locs[x]+t*speeds[x]>=b)
				isok=true;
			if(isok)
			{
				oks++;
				ans+=noks;
				if(oks>=k)
					break;
			}
			else{
				noks++;
			}
		}
		
		if(oks==k)
		{
			cout << "Case #" << ct << ":" << " " << ans << endl;
			fout << "Case #" << ct << ":" << " " << ans << endl;
		}
		else {
			cout << "Case #" << ct << ":" << " " << "IMPOSSIBLE" << endl;
			fout << "Case #" << ct << ":" << " " << "IMPOSSIBLE" << endl;
		
		}

	}
	
	
	return 0;
}

