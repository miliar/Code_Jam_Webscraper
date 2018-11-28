#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) (a*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
int cases,z;
int l,d;
string all[5001];
set<char>pat[15];
int main()
{
	#ifdef WIN32
		freopen("A-large.in","r",stdin);
		freopen("A-large.out","w",stdout);
	#endif
////////////////////////////////////////////
	int i,j,k;
	string str;
	scanf("%d%d%d",&l,&d,&cases);
	for(i=0;i<d;i++)
	{
		cin >> all[i];
	}
	
	for(z=0;z<cases;z++)
	{
		int ans;
		ans=0;
		j=0;
		cin >> str;
		for(i=0;i<l;i++)
			pat[i].clear();
		for(i=0;i<str.size();)
		{
			if(str[i]=='(')
			{
				i++;
				while(str[i]!=')')
				{
					pat[j].insert(str[i]);
					i++;
					
				}
				j++;
				i++;
			}
			else
			{
				pat[j].insert(str[i]);
				i++;
				j++;
			}
		}
		for(i=0;i<d;i++)
		{
			for(j=0;j<l;j++)
			{
				if(pat[j].find(all[i][j])==pat[j].end())
					break;
			}
			if(j==l)ans++;
		}
		printf("Case #%d: %d\n",z+1,ans);
	}
	return 0;
}