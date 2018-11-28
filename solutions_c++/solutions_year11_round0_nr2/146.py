#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <complex>
#include <cmath>
#include <vector>
#include <list>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <set>
#include <map>
#include <ctime>
using namespace std;
int T,casenum,c,d,n,i;
string s;
char ch;
char combine[300][300];
bool opposed[300][300];
void check()
{
	int l=s.size();
	if (l<=1) return;
	if (combine[s[l-1]][s[l-2]]!=0)
	{
		ch=combine[s[l-1]][s[l-2]];
		s.erase(l-2,2);
		s=s+ch;
	}
	for (int i=0;i<l-1;i++)
		if (opposed[s[i]][s[l-1]])
		{
			s.clear();
			break;
		}
}
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		memset(combine,0,sizeof(combine));
		memset(opposed,0,sizeof(opposed));
		cin>>c;
		for (i=1;i<=c;i++)
		{
			cin>>s;
			combine[s[0]][s[1]]=combine[s[1]][s[0]]=s[2];
		}
		cin>>d;
		for (i=1;i<=d;i++)
		{
			cin>>s;
			opposed[s[0]][s[1]]=opposed[s[1]][s[0]]=true;
		}
		s.clear();
		cin>>n;
		for (i=1;i<=n;i++)
		{
			cin>>ch;
			s=s+ch;
			check();
		}
		cout<<"[";
		for (i=0;i<s.size();i++)
		{
			if (i==0) cout<<s[i];
			else cout<<", "<<s[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}
