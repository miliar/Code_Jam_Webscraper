#pragma warning(disable : 4996)
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#define F(i,a) for(int i=0;i<int((a).size());i++)
#define INF 1000000000
#define MP make_pair
#define ALL(a) (a).begin(), (a).end()
#define X first
#define Y second
#define LL long long
#define LD long double
#define SQR(a) ((a)*(a))
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE 
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);
#endif
	int t;
	cin >> t;
	for (int iii=1; iii<=t; ++iii)
	{
		int c;
		cin >> c;
		map< pair<char,char>,int > com;
		for (int i=0; i<c; ++i)
		{
			string s;
			cin >> s;
			com[MP(s[0],s[1])]=s[2];
			com[MP(s[1],s[0])]=s[2];
		}
		int d;
		cin >> d;
		set< pair<char,char> > op;
		for (int i=0; i<d; ++i)
		{
			string s;
			cin >> s;
			op.insert(MP(s[0],s[1]));
			op.insert(MP(s[1],s[0]));
		}
		int n;
		cin >> n;
		string s;
		cin >> s;
		vector<int> a;
		F(i,s)
		{
			if (!a.empty())
			{
				map< pair<char,char>,int >::iterator it=com.find(MP(a.back(),s[i]));
				if (it!=com.end())
				{
					a.erase(a.end()-1); 
					a.push_back(it->second);
				}
				else
				{
					bool tf=false;
					F(j,a) 
						if (op.find(MP(a[j],s[i]))!=op.end())
						{
							a.clear();
							tf=true;
							break;
						}
					if (!tf)
						a.push_back(s[i]);
				}			
			}else
				a.push_back(s[i]);
		}
		cout << "Case #" << iii << ": [";
		F(i,a)
		{
			cout << (char)a[i];
			if (i!=a.size()-1)
				cout << ", ";
		}
		cout << "]\n";
	}
	return 0;
}
