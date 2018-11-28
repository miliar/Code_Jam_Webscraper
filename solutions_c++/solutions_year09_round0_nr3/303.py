#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;

char s[505],an[20]="welcome to code jam";
int len,yes[19][505];

void f(int lay)
{
	int i,j;
	if(lay == 18)
	{
		for (i = 0 ; i < len ; i++) yes[18][i] = (s[i]==an[18]);
		return;
	}
	for (i = 0 ; i < len ; i++)
	{
		if(s[i] == an[lay])
		{
			for (j = i+1 ; j < len ; j++) yes[lay][i]+=yes[lay+1][j];
			yes[lay][i] %= 10000;
		}
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T, ca, i , j,ans;
	gets(s);
	sscanf(s,"%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		gets(s);
		len = strlen(s);
		memset(yes, 0 , sizeof yes);
		for (i = 0 ; i < 19 ; i++) f(18-i);
		for (i = ans = 0 ; i < len ; i++) ans+= yes[0][i];
		printf("Case #%d: %04d\n",ca,ans%10000);
	}
	return 0;
}
