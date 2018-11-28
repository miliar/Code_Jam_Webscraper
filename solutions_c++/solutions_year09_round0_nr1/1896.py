#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;

int l,d,n,i,j,test,ans;
string word[5010];
bool t[20][256];
bool group;
bool ok;
string ts;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

	scanf("%d %d %d\n",&l,&d,&n);
	for (i=1; i<=d; i++)
		cin >> word[i];
	for (test=1; test<=n; test++)
	{
		printf("Case #%d: ",test);
		ans=0;
		memset(t,0,sizeof(t));
		cin >> ts;
		i=0; group=0;

		for (j=0; j<ts.length(); j++)
		{
			if (ts[j]=='(') group=1; else
			if (ts[j]==')') {group=0; i++;} else
			{
				t[i][int(ts[j])]=1;
				if (!group) i++;
			}
		}
		for (i=1;  i<=d; i++)
		{
			ok=1;
			for (j=0; j<l; j++)
				ok&=t[j][word[i][j]];
			if (ok) ans++;
		}

		printf("%d\n",ans);
	}

    return 0;
}
