#include<stdio.h>

#include<map>
#include<vector>
#include<queue>

using namespace std;

#define Swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
int cc;

int n, T;
int a[111][111];
int atleast[111];
int ori[111];

int ReTry(void)
{

	int l1;


	map< vector<int>, int > result;
	vector<int> perm(n);
	vector<int> curr(n);
	queue< vector<int> > q;

	for(l1=0;l1<n;l1++) perm[l1] = ori[l1];
	q.push( perm );
	result[perm] = 0;
	int itsme;
	while(!q.empty())
	{
		curr = q.front();
		for(l1=0;l1<n;l1++) if(curr[l1] > l1) break;
		if(l1 == n)
		{
			return result[curr];
		}
		q.pop();
		itsme = result[curr];

		for(l1=0;l1+1<n;l1++)
		{
			Swap(curr[l1], curr[l1+1]);
			if(result.count( curr ) == 0)
			{
				result[curr] = itsme + 1;
				q.push(curr);
			}
			Swap(curr[l1], curr[l1+1]);
		}
	}
}

int main(void)
{
	int l0, l1, l2, l3;
	freopen("A1.in","r",stdin);
	freopen("A1_.out","w",stdout);

//	freopen("input.txt","r",stdin);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&n);
		for(l1=0;l1<n;l1++) for(l2=0;l2<n;l2++) scanf("%1d",&a[l1][l2]);

		for(l1=0;l1<n;l1++)
		{
			atleast[l1] = -1;
			for(l2=0;l2<n;l2++)
			{
				if(a[l1][l2]) atleast[l1] = l2;
			}
			ori[l1] = atleast[l1];
		}

		int ret = 0;

		for(l1=n-1;l1>=0;l1--)
		{
			int cnt = 0;
			for(l2=0;l2<n;l2++)
			{
				if(atleast[l2] == l1) cnt++;
			}
			for(l2=n-1;l2>=0;l2--)
			{
				if(atleast[l2] == l1)
				{
					--cnt;
					if(l2 < l1+cnt)
					{
						for(l3=l2;l3<l1+cnt;l3++)
						{
							Swap(atleast[l3], atleast[l3+1]);
							ret++;
						}
					}
				}
			}
		}

		int hell = ReTry();
		/*
		if(hell != ret)
		{
			printf("......%d %d\n",hell,ret);
			for(l1=0;l1<n;l1++){ for(l2=0;l2<n;l2++) printf("%d",a[l1][l2]); printf("\n"); }
		}
		*/

		printf("Case #%d: %d\n",l0, hell);
	}

	return 0;
}