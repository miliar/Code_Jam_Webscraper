#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>

using namespace std;

int T,tot,i,j,sum,A[4],a[4][4];
char s[11];

inline bool Xun(int t)
{	int i,j;
	for (i=0;i<4;i++)
	{	memset(A,0,sizeof(A));
		for (j=0;j<4;j++) A[a[i][j]]++;
		if (A[t]==4) return true;
		if ((A[t]==3)&&(A[3]==1)) return true;
		memset(A,0,sizeof(A));
		for (j=0;j<4;j++) A[a[j][i]]++;
		if (A[t]==4) return true;
		if ((A[t]==3)&&(A[3]==1)) return true;
		}
	memset(A,0,sizeof(A));
	for (i=0;i<4;i++) A[a[i][i]]++;
	if (A[t]==4) return true;
	if ((A[t]==3)&&(A[3]==1)) return true;
	memset(A,0,sizeof(A));
	for (i=0;i<4;i++) A[a[i][3-i]]++;
	if (A[t]==4) return true;
	if ((A[t]==3)&&(A[3]==1)) return true;
	return false;
}

int main()
{
//	freopen("A.in","r",stdin);
//	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (tot=1;tot<=T;tot++)
	{	printf("Case #%d: ",tot);
		for (i=0;i<4;i++)
		{	scanf("%s",s);
			for (j=0;j<4;j++) a[i][j]=(s[j]=='.')?0:(s[j]=='X')?1:(s[j]=='O')?2:3;
			}	//scanf("%s",s);
		if (Xun(1)) { printf("X won\n"); continue; } else
		if (Xun(2)) { printf("O won\n"); continue; }
		sum=0; for (i=0;i<4;i++) for (j=0;j<4;j++) if (a[i][j]==0) sum++;
		if (sum>0) printf("Game has not completed\n"); else printf("Draw\n");
		}
	return 0;
}
