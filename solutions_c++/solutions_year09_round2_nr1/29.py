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
#include <set>
using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");


bool isleaf[10000];


int chds[10000][2];
double mults[10000];
int pars[10000];

int main(void)
{
cout.precision(9);
fout.precision(9);
	cout << "HELLO" << endl;
	
	int ttt;
	cin >> ttt;
	int ct = 0;
	string s;
	string empt;
	vector <string> features(10000,empt);
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		int m;
		cin >> m;
		getline(cin,s);
		string t;
		int curr = 0;
		int sz = 1;
		
		for(i=0; i<m; i++)
		{
			getline(cin,s);
			t+=" "+s;
		}
		//cout << m << endl;
		flush(cout);
		string ss;
		for(i=0; i<t.size(); i++)
		{
			if(t[i]=='(' || t[i]==')')
			{
				ss+=" ";
				ss+=t[i];
				ss+=" ";
			}
			else
				ss+=t[i];
		}
		//cout << ss << endl;
				stringstream sin(ss);
		char c;
		int dep = 0;
		for(i=0; i<10000; i++)
		{
			chds[i][0]=chds[i][1]=-1;
			isleaf[i]=false;
			mults[i]=0.0;
			pars[i]=-1;
		}
		

		sin >> c;
		dep = 1;
		while(true)
		{
			
			
			sin >> mults[curr];
			sin >> s;
			if(s!=")")
			{
				isleaf[curr]=false;
				chds[curr][0]=sz;
				pars[sz]=curr;
				sz++;
				features[curr]=s;
				sin >> c;
				curr = chds[curr][0];
				dep++;
				continue;
			}
			else
			{
				isleaf[curr]=true;
			}
			while(s==")")
			{
				dep--;
				curr=pars[curr];
				sin >> s;
				if(dep==0)
					break;
			}
			if(dep==0)
				break;
			dep++;
			chds[curr][1]=sz;
			pars[sz]=curr;
			sz++;
			curr=chds[curr][1];
		}
	/*	for(i=0; i<sz; i++)
		{
			cout << features[i] << " " << isleaf[i] << " " << chds[i][0] << " "<< chds[i][1] << " " << pars[i] << " " << mults[i] << endl;
		}*/
		cin >> m;
		
			
		
		
		
		cout << "Case #" << ct << ":" << endl;
		fout << "Case #" << ct << ":"  << endl;
		double d = 0.0;
		for(k=0; k<m; k++)
		{
			d=1.0;
			cin >> s >> j;
			set<string> st;
			for(i=0; i<j; i++)
			{
				cin >> s;
				st.insert(s);
			}
			curr =0;
			while(true)
			{
				d*=mults[curr];
				if(isleaf[curr])
					break;
				if(st.count(features[curr])>0)
				{
					curr=chds[curr][0];
				}
				else
				{
					curr=chds[curr][1];
				}
			}
			cout << d << endl;
			fout << d << endl;
		}
		
	}

	
	return 0;
}

