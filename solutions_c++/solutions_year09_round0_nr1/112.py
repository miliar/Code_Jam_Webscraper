#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int N,D,L,tot[20];
char s[5005][20],t[20][100],tmp[10000];

inline bool Check(int k)
{
	for (int i=0;i<L;i++) {
		bool flag=0;
		for (int j=0;j<tot[i];j++)
		if (t[i][j]==s[k][i]) {
			flag=1;break;
		}
		if (!flag) return false;
	}
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	for (int i=1;i<=D;i++)
		scanf("%s",s[i]);
	for (int i=1;i<=N;i++) {
		scanf("%s",&tmp);
		memset(tot,0,sizeof(tot));
		for (int j=0,k=0;j<L;j++) {
			if (tmp[k]=='(') {
				for (k++;tmp[k]!=')';k++)
					t[j][tot[j]++]=tmp[k];
				k++;
			} else t[j][tot[j]++]=tmp[k++];
		}
		int ret=0;
		for (int j=1;j<=D;j++)
		if (Check(j)) ++ret;
		printf("Case #%d: %d\n",i,ret);
	}
	return 0;
}
