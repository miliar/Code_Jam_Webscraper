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

ofstream fout("output.txt");
ifstream fin("input.txt");


string ss = "welcome to code jam";

int main(void)
{
	int ttt;
	cin >> ttt;
	int ct = 0;
	string s;
	getline(cin,s);
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		getline(cin,s);
		int ans[20];
		for(i=0; i<20; i++)
			ans[i]=0;
		ans[0]=1;
		for(k=0; k<s.size(); k++)
		{
			for(i=18; i>=0; i--)
			{
				if(ss[i]==s[k])
				{
					ans[i+1]=(ans[i]+ans[i+1])%1000;
				}
			}
		}
		
		stringstream sin("");
		sin << ans[19];
		string t;
		sin >> t;
		while(t.size()<4)
		{
			t="0"+t;
		}
		
		
		cout << "Case #" << ct << ":" << " " << t << endl;
		fout << "Case #" << ct << ":" << " " << t << endl;
		
	}

	
	return 0;
}

