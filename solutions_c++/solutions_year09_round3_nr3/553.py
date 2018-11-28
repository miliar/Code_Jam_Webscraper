#include<stdio.h>
#include<set>
#include<algorithm>
#include<limits.h>
#include<vector>
using namespace std;
#define N 7
int rez,n;
int p,q;
int v[N];
set<int> s;
int aici[N];
inline void rezolva()
{
	scanf("%d%d",&p,&q);
        for(int i=0; i<q; ++i)
		scanf("%d",&v[i]);
	rez=INT_MAX;
	int rez1;
	set<int>::iterator it1,it2;
        do
        {
	       // s.clear();
	      //  s.insert(0);
	      //  s.insert(p+1);
	       // if(s.find(0)!=s.end())
	      //  	fprintf(stderr,"DA\n");
		rez1=0;
        	for(int i=0; i<q; ++i)
		{
                      //  it1=s.lower_bound(v[i]);
		      //  it2=s.upper_bound(v[i]);
		      //  s.insert(v[i]);
		      //  fprintf(stderr,"%d %d %d\n",*it1,*it2,v[i]);
			int x1=0,x2=p+1;
			for(int j=0; j<i; ++j)
			{
                        	if(v[j]<v[i] && v[j]>x1)
					x1=v[j];
				if(v[j]>v[i] && v[j]<x2)
					x2=v[j];
			}
			rez1+=x2-x1-2;
		}
	      //  for(int i=0; i<q; ++i)
	      //  	fprintf(stderr,"%d ",v[i]);
	      //  fprintf(stderr,"-> %d\n",rez1);
		if(rez1<rez)
			rez=rez1;
        }while(next_permutation(v,v+q));
	printf("%d\n",rez);
}	
int main()
{
	freopen("pc.in","r",stdin);
	freopen("pc.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; ++i)
	{
		printf("Case #%d: ",i);
		rezolva();
	}
	return 0;
}

