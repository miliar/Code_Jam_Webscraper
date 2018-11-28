#include <iostream>
using namespace std;
int ans[105][105];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt,ii,p,q,i,j,nom[105],k,temp,len;
	cin>>tt;
	for(ii=1;ii<=tt;ii++)
	{
		cin>>p>>q;
		nom[0]=0;
		for(i=1;i<=q;i++) cin>>nom[i];
		nom[q+1]=p+1;
		memset(ans,0,sizeof(ans));
		for(len=2;len<=q+1;len++)
		{
			for(i=0;i+len<=q+1;i++)
			{
				j=i+len;
				ans[i][j]=1000000000;
				for(k=1;k<=q;k++)
				{
					if(nom[k]>nom[i] && nom[k]<nom[j])
					{
						temp=ans[i][k]+ans[k][j]+(nom[k]-nom[i]-1)+(nom[j]-nom[k]-1);
						if(temp<ans[i][j]) ans[i][j]=temp;
					}
				}
			}
		}
		cout<<"Case #"<<ii<<": "<<ans[0][q+1]<<endl;
	}
	return 0;
}

