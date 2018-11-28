#include <cstdio>
#include <cstring>

#define MAX 510
#define MOD 10000


char s[MAX];
char tmp[MAX];

int dp[MAX][30];

bool inWord(char x)
{
	if (x=='w'||x=='e'||x=='l'||x=='c'||x=='o'||x=='m'||x==' '||x=='t'||x=='d'||x=='j'||x=='a') return true;
	else return false;
}

void inline add(int &x,int y)
{
	x=(x+y)%MOD;
}

int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
	int i,t,cn;
	scanf("%d",&t);
	getchar();
	for (cn=1;cn<=t;cn++)
	{
		memset(dp,0,sizeof(dp));
		memset(s,0,sizeof(s));
		memset(tmp,0,sizeof(tmp));
		gets(tmp);
		int l=strlen(tmp);
		int ls=0;
		for (i=0;i<l;i++)
		{
			if (inWord(tmp[i])) s[ls++]=tmp[i];
		}
		if (s[0]=='w') dp[0][0]++;
		for (i=1;i<ls;i++)
		{
			if (s[i]=='w') 
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				add(dp[i][0],1);
			}
			else if (s[i]=='e')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][0]!=0) add(dp[i][1],dp[i-1][0]);
				if (dp[i-1][5]!=0) add(dp[i][6],dp[i-1][5]);
				if (dp[i-1][13]!=0) add(dp[i][14],dp[i-1][13]);
			}
			else if (s[i]=='l')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][1]!=0) add(dp[i][2],dp[i-1][1]);
			}
			else if (s[i]=='c')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][2]!=0) add(dp[i][3],dp[i-1][2]);
				if (dp[i-1][10]!=0) add(dp[i][11],dp[i-1][10]);
			}
			else if (s[i]=='o')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][3]!=0) add(dp[i][4],dp[i-1][3]);
				if (dp[i-1][8]!=0) add(dp[i][9],dp[i-1][8]);
				if (dp[i-1][11]!=0) add(dp[i][12],dp[i-1][11]);
			}
			else if (s[i]=='m')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][4]!=0) add(dp[i][5],dp[i-1][4]);
				if (dp[i-1][17]!=0) add(dp[i][18],dp[i-1][17]);
			}
			else if (s[i]==' ')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][6]!=0) add(dp[i][7],dp[i-1][6]);
				if (dp[i-1][9]!=0) add(dp[i][10],dp[i-1][9]);
				if (dp[i-1][14]!=0) add(dp[i][15],dp[i-1][14]);
			}
			else if (s[i]=='t')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][7]!=0) add(dp[i][8],dp[i-1][7]);
			}
			else if (s[i]=='d')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][12]!=0) add(dp[i][13],dp[i-1][12]);
			}
			else if (s[i]=='j')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][15]!=0) add(dp[i][16],dp[i-1][15]);
			}
			else if (s[i]=='a')
			{
				memcpy(dp[i],dp[i-1],sizeof(dp[i-1]));
				if (dp[i-1][16]!=0) add(dp[i][17],dp[i-1][16]);
			}
		}
		printf("Case #%d: %04d\n",cn,dp[ls-1][18]);
	}
	return 0;
}
/*
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
w e l c o m e   t o     c  o  d  e     j  a  m

4
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam
So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam.
*/
