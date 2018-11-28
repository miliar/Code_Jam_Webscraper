#include<stdio.h>
#include<functional>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;
int cs,z;
FILE*in=fopen("B-large.in","r");
FILE*out=fopen("B-large.out","w");
int n,m;
int isone[2009];
class drink{public:
	int t;
	int s;
};
drink adj[2009][2009];
int cadj[2009];
int best;
int arr[2009];
int bitcnt(int x)
{
	int ret=0;
	while(x)
	{
		x&=(x-1);
		ret++;
	}
	return ret;

}
int main()
{
	int i,j,k,bestm;
	fscanf(in,"%d",&cs);
	for(z=0;z<cs;z++)
	{

		fscanf(in,"%d%d",&n,&m);
		memset(arr,0,sizeof(arr));

		best=n+1;
		//bestm=(1<<n)-1;
		memset(isone,-1,sizeof(isone));
		for(i=0;i<m;i++)
		{
			fscanf(in,"%d",&cadj[i]);
			for(j=0;j<cadj[i];j++)
			{
				fscanf(in,"%d %d",&adj[i][j].t,&adj[i][j].s);
				adj[i][j].t--;
				if(adj[i][j].s==1)
					isone[i]=adj[i][j].t;
			}
			
		}
		////scaning
	/*	for(i=0;i<(1<<n);i++)
		{
			if(bitcnt(i)>best)continue;
			for(j=0;j<m;j++)
			{
				for(k=0;k<cadj[j];k++)
					if( bool(i & (1<<adj[j][k].t))==bool(adj[j][k].s))
						break;

				if(k==cadj[j])
					break;
			}
			if(j==m)
			{
				bestm=i;
				best=bitcnt(i);
			}
		}*/
		best=n+1;
		while(1)
		{
			for(i=0;i<m;i++)
			{
				for(j=0;j<cadj[i];j++)
				{
					if( arr[adj[i][j].t]==bool(adj[i][j].s))
						break;
				}
				if(j==cadj[i])
				{
					if(isone[i]==-1)
						goto bara;
					else
						arr[isone[i]]=1;
					break;
				}
			}
			if(i==m)
			{
				best=-1;
				break;
			}
		}
		bara:
		////////printing
		fprintf(out,"Case #%d:",z+1);
		if(best>n)
			fprintf(out," IMPOSSIBLE");
		else
			for(i=0;i<n;i++)
			{
				if(arr[i])
					fprintf(out," 1");
				else
					fprintf(out," 0");
			}
		fprintf(out,"\n");
	}
	return 0;
}