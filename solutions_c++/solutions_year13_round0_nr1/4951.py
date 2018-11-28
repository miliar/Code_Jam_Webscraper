#include <iostream>
#include <string>
using namespace std;
const string s[]={"X won","O won","Draw","Game has not completed"};
char a[4][4];
char c[4];
int win()
{
	int k,t1=0,t2=0;
	for (int i=0;i<4;i++)
		if (c[i]=='X')
			t1++;
		else if (c[i]=='O')
			t2++;
		else k=i;
	if (t1==4 || (t1==3 && t2==0 && c[k]=='T'))
		return 1;
	else if (t2==4 || (t2==3 && t1==0 && c[k]=='T'))
		return 2;
	return 0;
}
int acase()
{
	int i,j,rt=0;
	bool ff=0;
	for (i=0;i<4;i++)
	{
		for (j=0;j<4;j++)
		{
			cin>>a[i][j];
			if (a[i][j]=='.')
				ff=1;
			c[j]=a[i][j];
		}
		if (win())
			rt=win();
	}
	if (rt)
		return rt;
	for (j=0;j<4;j++)
	{
		for (i=0;i<4;i++)
			c[i]=a[i][j];
		if (win())
			return win();
	}
	for (i=0;i<4;i++)
		c[i]=a[i][i];
	if (win())
		return win();
	for (i=0;i<4;i++)
		c[i]=a[i][3-i];
	if (win())
		return win();
	if (ff)
		return 4;
	return 3;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("large.out","w",stdout);
	int T;
	cin>>T;
	for (int tT=1;tT<=T;tT++)
	{
		printf("Case #%d: %s\n",tT,s[acase()-1].c_str());
	}
}
