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

int words[5000][15];


int main(void)
{
	int l,d;
	cin >> l >> d;
	int ttt;
	cin >> ttt;
	int ct = 0;
	int n,i,j,k;
	for(i=0; i<d; i++)
	{
		string s;
		cin >> s;
		for(j=0; j<l; j++)
		{
			words[i][j]=s[j]-'a';
		}
	}
	
	
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		string s;
		cin >> s;
		int ans = 0;
		int vals[15];
		for(i=0; i<l; i++)
			vals[i]=0;
		k=0;
		int state = 0;
		for(j=0; j<s.size(); j++)
		{
			if(s[j]=='(')
			{
				state=1;
				continue;
			}
			else if(s[j]==')')
			{
				state=0;
				k++;
			}
			else
			{
				vals[k]+=(1<<((int)(s[j]-'a')));
				if(state==0)
					k++;
			}
		}
		for(j=0; j<l; j++)
		{
			cout << vals[j] << " ";
		}
		cout << endl;
		for(i=0; i<d; i++)
		{
			bool isok = true;
			for(j=0; j<l; j++)
			{
				if( (vals[j]&(1<<words[i][j]))==0)
					isok=false;
			}
			if(isok)
				ans++;
		}
		
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}

	
	return 0;
}

