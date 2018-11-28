#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int T;

int a[111][111], b[111][111];
int f[111];
int check[111];
int n, m;
int flag = 0;

void Go(int Dep)
{
	if(flag) return;
	if(Dep == m)
	{
		int l1, l2;
		for(l1=0;l1<m;l1++)
		{
			for(l2=0;l2<m;l2++)
			{
				if(b[l1][l2] != a[f[l1]][f[l2]]) return;
			}
		}
		flag = 1;
		return;
	}
	else
	{
		int l1;
		for(l1=0;l1<n;l1++)
		{
			if(check[l1] == 0)
			{
				check[l1] = 1;
				f[Dep] = l1;
				Go(Dep + 1);
				check[l1] = 0;
			}
		}
	}
}

int main(void)
{
	int l0, l1, l2, l3;
	int t1, t2;

	//freopen("input.txt","r",stdin);
	freopen("D1.in","r",stdin);
	freopen("D1.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d ",&n);
		for(l1=0;l1<n;l1++)
		{
			for(l2=0;l2<n;l2++)
			{
				a[l1][l2] = b[l1][l2] = 0;
			}
		}
		for(l1=1;l1<n;l1++)
		{
			scanf("%d %d",&t1,&t2);
			t1--;
			t2--;
			a[t1][t2] = 1;
			a[t2][t1] = 1;
		}

		scanf("%d",&m);
		for(l1=1;l1<m;l1++)
		{
			scanf("%d %d",&t1,&t2);
			t1--;
			t2--;
			b[t1][t2] = 1;
			b[t2][t1] = 1;
		}

		flag = 0;
		for(l1=0;l1<n;l1++)
		{
			if(check[l1])
			{
				fprintf(stderr,"-_-\n");
			}
			check[l1] = 0;
		}
		Go(0);

		printf("Case #%d: %s\n",l0,flag?"YES":"NO");
	}
}