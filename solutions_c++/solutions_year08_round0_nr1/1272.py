#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("A-small-attempt1.in");
ofstream fout("a.out");
#define INF 10000
int t;
int n, m;
int f[110][1010];
char engine[110][110];

void init()
{
	char s[10];
	fin>>n;
	fin.getline(s,100);
	for (int i=0;i<n;i++) fin.getline(engine[i],1000);
	fin>>m;
	fin.getline(s,100);
	cout<<n<<' '<<m<<endl;
}
void calc()
{
	int i, j, k, index;
	char name[110];

	memset(f[0],0,sizeof(f[0]));		
	for (j=1;j<=m;j++)
	{
		fin.getline(name,1000);
		for (i=0;i<n;i++)
			if (strcmp(engine[i],name)==0)
			{
				index=i;
				break;
			}
		for (i=0;i<n;i++)
			if (i==index)
			{
				f[i][j]=INF;
			}
			else {
				f[i][j]=INF;
				for (k=0;k<n;k++)
					if (k==i) f[i][j]=min(f[i][j],f[i][j-1]);
					else f[i][j]=min(f[i][j],f[k][j-1]+1);
			}			
	}
	int ans=INF;
	for (i=0;i<n;i++) ans=min(ans,f[i][m]);
	fout<<ans<<endl;
	cout<<ans<<endl;
}
int main()
{
	fin>>t;
	for (int i=1;i<=t;i++)
	{
		fout<<"Case #"<<i<<": ";
		init();
		calc();		
	}
}