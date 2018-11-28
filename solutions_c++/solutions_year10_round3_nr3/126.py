#include <iostream>
using namespace std;
int map[600][3000];
bool check(int x,int y,int size)
{
	int i,j;
	if(map[x][y]==-1)return false;
	for(i=x;i<x+size;i++)
	{
		for(j=y;j<y+size;j++)
		{
			if(i-1>=x && map[i][j]+map[i-1][j]!=1)return false;
			if(i+1<=x+size-1 && map[i][j]+map[i+1][j]!=1)return false;
			if(j-1>=y && map[i][j]+map[i][j-1]!=1)return false;
			if(j+1<=y+size-1 && map[i][j]+map[i][j+1]!=1)return false;
		}
	}
	for(i=x;i<x+size;i++)
		for(j=y;j<y+size;j++)
			map[i][j]=-1;
	return true;
}
int main()
{
	freopen("out.txt","w",stdout);
	int t,n,m,a;
	char c;
	cin>>t;
	int i,j,k,s;
	bool find;
	int ca=0,cnt;
	int ans[600],mm;
	while(t--)
	{
		cin>>m>>n;
		for(i=0;i<m;i++)
		{
			for(j=0;j<n/4;j++)
			{
				cin>>c;
				if(c>='0' && c<='9')
					a=c-'0';
				else
					a=c-'A'+10;
				s=j*4;
				for(k=s+3;k>=s;k--)
				{
					map[i][k]=a%2;
					a/=2;
				}
			}
		}
		memset(ans,0,sizeof(ans));
		mm=n<m?n:m;
		cnt=0;
		for(k=mm;k>=1;k--)
		{
			find=0;
			for(i=0;i<=m-k;i++)
			{
				for(j=0;j<=n-k;j++)
				{
					if(check(i,j,k))
					{
						find=1;
						ans[k]++;
					}

				}
			}
			if(find==1)
				cnt++;
		}
		printf("Case #%d: %d\n",++ca,cnt);
		for(i=mm;i>=1;i--)
		{
			if(ans[i]!=0)
			{
				cout<<i<<" "<<ans[i]<<endl;
			}
		}
	}
	return 0;
}




