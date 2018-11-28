#include <iostream>
using namespace std;
int flag[3010][2];
int c[2000][2];
int ans[2000];
int main()
{
	freopen("B-large.in","r",stdin);	
	freopen("B-large.out","w",stdout);
	int i,N,j,k,n,m,p,r;
	bool ff,anf,che;
	cin>>N;
	for(i=1;i<=N;i++)
	{
		cin>>n>>m;
		for(j=0;j<n;j++) ans[j]=0;
		p=0;
		for(j=0;j<m;j++)
		{
			cin>>c[j][0];
			c[j][1]=p;
			for(k=0;k<c[j][0];k++)
			{
				cin>>flag[p][0]>>flag[p][1];
				flag[p][0]--;
				p++;
			}			
		}
		for(j=0;j<m;j++)
		{
			if(c[j][0]==1&&flag[c[j][1]][1]==1)
				ans[flag[c[j][1]][0]]=1;
		}		
		che=true;
		while(che)
		{
			che=false;
			anf=true;
			for(j=0;j<m;j++)
			{
				ff=false;
				p=c[j][1];
				r=-1;
				for(k=0;k<c[j][0];k++)
				{
					if(ans[flag[p][0]]==flag[p][1])
					{
						ff=true;
						break;
					}
					if(flag[p][1]==1) r=p;
					p++;
				}
				if(ff==false)
				{
					if(r>-1&&ans[flag[r][0]]==0)
					{
						ans[flag[r][0]]=1;
						che=true;
					}
					else
					{
						anf=false;
						break;
					}
				}
			}
		}
		cout<<"Case #"<<i<<":";
		if(anf==false)
			cout<<" IMPOSSIBLE"<<endl;
		else
		{
			for(j=0;j<n;j++) cout<<" "<<ans[j];
			cout<<endl;
		}
	}
	return 0;
}