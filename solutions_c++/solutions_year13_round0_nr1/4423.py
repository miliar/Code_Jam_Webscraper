#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <deque>
#include <iterator>	
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>	
#include <stack>
#include <utility>
#include <sstream>
#include <string>

using namespace std;

const int IX[]={1,0,-1,0,1,1,-1,-1};
const int IY[]={0,1,0,-1,-1,1,1,-1};

int DAT,n,m,i,j,k,a,b,c;
string s[4];

void g(char c)
{
	cout<<c<<' '<<"won"<<endl;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>DAT;
	for (int cas=1;cas<=DAT;cas++)
	{
		c=0;
		cout<<"Case #"<<cas<<": ";
		for (i=0;i<4;i++)
			cin>>s[i];
		for (i=0;i<4;i++)
		{
			a=b=0;
			for (j=0;j<4;j++)
			{
				c+=s[i][j]=='.';
				a+=(s[i][j]=='X')+(s[i][j]=='T');
				b+=(s[i][j]=='O')+(s[i][j]=='T');
			}
			if (a==4) {g('X');break;}
			if (b==4) {g('O');break;}
			a=b=0;
			for (j=0;j<4;j++)
			{
				a+=(s[j][i]=='X')+(s[j][i]=='T');
				b+=(s[j][i]=='O')+(s[j][i]=='T');
			}
			if (a==4) {g('X');break;}
			if (b==4) {g('O');break;}
			a=b=0;
		}
		if (i<4) continue;
		a=b=0;
		for (j=0;j<4;j++)
		{
			a+=(s[j][j]=='X')+(s[j][j]=='T');
			b+=(s[j][j]=='O')+(s[j][j]=='T');
		}
		if (a==4) {g('X');continue;}
		if (b==4) {g('O');continue;}
		a=b=0;
		for (j=0;j<4;j++)
		{
			a+=(s[3-j][j]=='X')+(s[3-j][j]=='T');
			b+=(s[3-j][j]=='O')+(s[3-j][j]=='T');
		}
		if (a==4) {g('X');continue;}
		if (b==4) {g('O');continue;}
		if (c==0)
		{
			cout<<"Draw"<<endl;
			continue;
		}
		cout<<"Game has not completed\n";
	}
	return 0;
}
