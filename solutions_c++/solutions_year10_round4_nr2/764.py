#include <iostream>
#include <cmath>
#define maxn 2050
using namespace std;
int ppow[12]={1,2,4,8,16,32,64,128,256,512,1024,2048};
bool used[maxn];
int path[20],m[maxn],tic[20][maxn];
int tn,p;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B_small.out","w",stdout);
	int i,j;
	cin >> tn;
	for (int t=1;t<=tn;t++)
	{
		cin >> p;
		memset(used,0,sizeof used);	
		for (i=1;i<=ppow[p];i++)
		{
			cin >> m[i];
			m[i]=p-m[i];
		}
		for (i=1;i<=p;i++)
			for (j=1;j<=ppow[p-i];j++)
				cin >> tic[i][j];
		for (i=1;i<=ppow[p];i++)
		{
			memset(path,0,sizeof path);
			for (j=ppow[p]+i-1;j>=1;j/=2)
				path[++path[0]]=j;
			for (j=path[0];j>path[0]-m[i];j--)
				used[path[j]]=true;
		}
		int ans=0;
		for (i=1;i<ppow[p];i++)
			if (used[i]) ans++;
		cout << "Case #" << t << ": " << ans << endl;
	}
}