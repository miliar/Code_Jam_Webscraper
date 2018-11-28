#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;

const int MAXN=205;

string cha[MAXN],opo[MAXN];
int c,d,n;
string a;
char stack[MAXN];
int sd;
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%d",&c);
		for (int i=1;i<=c;i++) cin >> cha[i];
		for (int i=1;i<=c;i++)
		{
			cha[i+c]=cha[i];
			swap(cha[i+c][0],cha[i+c][1]);
		}
		c*=2;
		scanf("%d",&d);
		for (int i=1;i<=d;i++) cin >> opo[i];
		for (int i=1;i<=d;i++)
		{
			opo[i+d]=opo[i];
			swap(opo[i+d][0],opo[i+d][1]);
		}
		d*=2;
		scanf("%d",&n);
		cin >> a;

		sd=0;
		bool flag;
		for (int i=0;i<n;i++)
		{
			stack[++sd]=a[i];
			flag=true;
			while (sd>=2 && flag)
			{
				flag=false;
				for (int j=1;j<=c;j++)
				if (cha[j][0]==stack[sd-1] &&
				    cha[j][1]==stack[sd])
			   	    {
					    sd--; stack[sd]=cha[j][2];
					    flag=true;
					    break;
				    }
			}
			for (int j=1;j<sd;j++)
			for (int t=1;t<=d;t++)
			   if (opo[t][0]==stack[j] &&
			       opo[t][1]==stack[sd])
			   {
				   sd=0;
				   break;
			   }
		}

		printf("Case #%d: [",tcase);
		for (int i=1;i<=sd;i++)
		{
			printf("%c",stack[i]);
			if (i<sd) printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
