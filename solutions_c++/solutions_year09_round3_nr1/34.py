#include <iostream>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt,ii,n,i,j,base;
	char c[100];
	int map[200];
	bool mapped[55];
	cin>>tt;
	for(ii=1;ii<=tt;ii++)
	{
		cin>>c;
		n=strlen(c);
		memset(map,-1,sizeof(map));
		memset(mapped,0,sizeof(mapped));
		base=1;
		for(i=0;i<n;i++)
		{
			if(map[c[i]]==-1)
			{
				j=0;
				if(i==0) j=1;
				for(;j<55;j++)
				{
					if(!mapped[j]) break;
				}
				if(j+1>base) base=j+1;
				mapped[j]=true;
				map[c[i]]=j;
			}
		}
		__int64 res=0;
		for(i=0;i<n;i++)
		{
			res*=base;
			res+=map[c[i]];
		}
		printf("Case #%d: %I64d\n",ii,res);
	}
	return 0;
}

