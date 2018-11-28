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
		
		int tot  = 0;
		int min = 10000000;
		int totweird = 0;
		
		fin >> n;
		
		
		for(int i=0; i<n; i++)
		{
			fin >> j;
			tot+=j;
			totweird^=j;
			if(j<min)
				min=j;
		}
		
		
		if(totweird==0)
		{
			int ans = tot - min;
			cout << "Case #" << ct << ":" << " " << ans << endl;
			fout << "Case #" << ct << ":" << " " << ans << endl;
		}
		else {
			cout << "Case #" << ct << ":" << " " << "NO" << endl;
			fout << "Case #" << ct << ":" << " " << "NO" << endl;

		}

		
	}
	
	
	return 0;
}

