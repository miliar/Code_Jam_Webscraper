#include<cstdio>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
map<string,int> m;
pair<int,pair<int,int>> a[400];
string s;
int t,k;
int n,i,j,c1,c2,c3,nr,rez[10001],r,x,y;

char col[12];
int main()
{
	freopen("Input.txt","r",stdin);
	freopen("Output.txt","w",stdout);
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		m.clear();
		nr=0;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf(" %s %d %d",col,&x,&y);
			a[i].first = x;
			a[i].second.first = y;
			s = col;
			if(m.find(s) != m.end())
				a[i].second.second=m[s];
			else
			{
				nr++;
				a[i].second.second=nr;
				m[s]=nr;
			}
		}

		sort(&a[1],&a[n+1]);
		r=-1;
		
		for(c1=1;c1<=nr;c1++)
			for(c2=c1;c2<=nr;c2++)
				for(c3=c2;c3<=nr;c3++)
				{
					memset(rez,-1,sizeof(rez));
					rez[0]=0;
					for(i=1;i<=n;i++)
						if(a[i].second.second == c1 || a[i].second.second == c2 || a[i].second.second == c3)
							for(j=a[i].first-1;j<a[i].second.first;j++)
								if(rez[j]!=-1 && (rez[a[i].second.first] == -1 || rez[a[i].second.first] > rez[j]+1 ))
									rez[a[i].second.first] = rez[j]+1;
					if(rez[10000]!=-1 && (rez[10000]<r || r==-1))
						r=rez[10000];						
				}
				
		printf("Case #%d: ",k);
		if(r==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",r);
	}
	return 0;
}
