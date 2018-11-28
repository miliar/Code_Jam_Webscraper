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




int main(void)
{
	int ttt;
	cin >> ttt;
	int ct = 0;
	string s;
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		cin >> s;
		s="0"+s;
		vector <char> lis(s.size(),'0');
		for(i=0; i<s.size(); i++)
		{
			lis[i]=s[i];
		}
		next_permutation(lis.begin(),lis.end());
		if(lis[0]=='0')
		{
			vector <char> lis1(lis.size()-1,'0');
			for(i=0; i<lis1.size(); i++)
				lis1[i]=lis[i+1];
			lis=lis1;
		}
		string ans(lis.size(),'0');
		for(i=0; i<ans.size(); i++)
			ans[i]=lis[i];
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}

	
	return 0;
}

