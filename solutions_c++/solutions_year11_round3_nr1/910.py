#define mset(a) memset(a,0,sizeof(a))

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

int main()
{
int t,r,c;
cin>>t;
for(int tt=1;tt<=t;tt++)
{
	cin>>r>>c;
	string s[100];
	for(int i=0;i<r;i++)
		cin>>s[i];
	for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
		{
			if(s[i][j]=='#')
				if(j==c-1||i==r-1||s[i][j+1]!='#'||s[i+1][j]!='#'||s[i+1][j+1]!='#')
				{
					
	cout<<"Case #"<<tt<<":"<<endl;
					cout<<"Impossible"<<endl;goto next;}
				else
				{
					s[i][j]='/';
					s[i][j+1]='\\';
					s[i+1][j]='\\';
					s[i+1][j+1]='/';
				}
		}
	cout<<"Case #"<<tt<<":"<<endl;
	for(int i=0;i<r;i++)
		cout<<s[i]<<endl;
next:;
}
return 0;
}
