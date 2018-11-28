#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n,W,L,r[1005],d[2][1005],ax[1005],ay[1005],ansx[1005],ansy[1005];

struct Node
{
	int r,i;
}node[1005];
bool cmp(Node p1, Node p2)
{
	return p1.r > p2.r;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas=0;scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d",&n,&W,&L);
		int ss = 0;
		if(W<L)swap(W,L),ss=1;
		for(int i = 0; i < n; i++)
			scanf("%d",&node[i].r),node[i].i=i;
		sort(node,node+n,cmp);
		for(int i = 0; i < n; i++)
			r[i] = node[i].r;
		int pos = 0, x = 0;
		while(pos < n && x+r[pos]*2 <= W)
		{
			ax[pos]=x+r[pos],ay[pos]=0;
			d[0][pos] = r[pos];
			x += r[pos]*2;
			pos++;
		}
		int id = 0, m = pos, q;
		while(pos < n)
		{
			int nid = id^1;
			for(int i = 0; i < m; i++)
				d[nid][i] = 0;
			if(id==0)
			{
				q = m-1;
				x = W;
				while(pos<n && q>=0)
				{
					if(x-2*r[pos] < ax[q]-r[q])
						q--;
					else
					{
						x -= 2*r[pos];
						ax[pos] = x+r[pos];
						ay[pos] = d[id][q]+r[pos];
						d[nid][q] = max(d[nid][q], ay[pos]+r[pos]);
						pos++;
					}
				}
			}
			else
			{
				q = 0;
				x = 0;
				while(pos<n && q<m)
				{
					if(x+2*r[pos] > ax[q]+r[q])
						q++;
					else
					{
						x += 2*r[pos];
						ax[pos] = x-r[pos];
						ay[pos] = d[id][q]+r[pos];
						d[nid][q] = max(d[nid][q], ay[pos]+r[pos]);
						pos++;
					}
				}
			}
			id ^= 1;
		}
		printf("Case #%d:",++cas);
		for(int i = 0; i < n; i++)
			ansx[node[i].i]=ax[i],ansy[node[i].i]=ay[i];
		for(int i = 0; i < n; i++)
		{
			if(ss)swap(ansx[i],ansy[i]);
			printf(" %.6f %.6f",(double)ansx[i],(double)ansy[i]);
		}
		puts("");
	}

	return 0;
}
