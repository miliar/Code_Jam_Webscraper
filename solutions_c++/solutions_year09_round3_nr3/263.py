#include <iostream>
using namespace std;
#define tiao system("pause")

int n;
int p;
int q;
int a[111];
int b[111];
int ans(0);

bool visited[111];
int main(void)
{
	int i,j,k,ci,cici,cicici;
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	
	scanf("%d",&n);
	for (cicici=1; cicici<=n; cicici++)
	{
		scanf("%d%d",&p,&q);
		for (i=1; i<=q; i++)
			scanf("%d",&a[i]);
		for (i=1; i<=q; i++)
			b[i] = i;
		ans = 1 << 30;
		do 
		{
			int cnt(0);
			memset(visited,0,sizeof(visited));
			visited[0] = visited[p+1] = true;
			for (i=1; i<=q; i++)
			{
				visited[a[b[i]]] = true;
				for (j=a[b[i]]+1; !visited[j]; j++)
					cnt++;
				for (j=a[b[i]]-1; !visited[j]; j--)
					cnt++;
			}
			ans <?= cnt;
		}
		while(next_permutation(b+1,b+1+q));			
		
		printf("Case #%d: %d\n",cicici,ans);
	}
	
//	tiao;
	return 0;
}
