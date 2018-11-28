#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAXN = 10050;

int n;
int d[MAXN],l[MAXN];
int f[MAXN];
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		printf("Case #%d: ",tcase);
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf("%d%d",&d[i],&l[i]);
		int tot;
		scanf("%d",&tot);
		memset(f,-1,sizeof(f));
		f[0]=d[0];
		for (int i=0;i<n;i++) if (f[i]!=-1){
			f[i]=min(f[i],l[i]);
			for (int j=i+1;j<n && d[j]-d[i]<=f[i];j++)
				f[j]=max(f[j],d[j]-d[i]);
		}
		bool ok=false;
		for (int i=0;i<n;i++) 
			if (f[i]>=tot-d[i]){
				puts("YES");
				ok=true;
				break;
			}
		if (!ok) puts("NO");
	}
}
