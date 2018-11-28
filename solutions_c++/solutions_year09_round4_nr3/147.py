#include <iostream>

using namespace std;

int n, m;
int a[200][30];
int g[200][200];
int d[200], fa[200];
int id[200];
bool check[200];

void init()
{
	cin>>n>>m;
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			cin>>a[i][j];
}
bool smaller(int i, int j)
{
	for (int k=0;k<m;k++)
		if (a[i][k]>=a[j][k]) return false;
	return true;
}
void order()
{
	memset(d,0,sizeof(d));
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++)
			if (g[i][j]==1) d[j]++;
	int t=0;
	for  (int i=0; i<n; i++)
		if (d[i]==0) id[t++] = i;
	for (int i=0;i<n;i++)
		for (int j=0; j<n;j++)
			if (g[id[i]][j]==1) {
				d[j]--;
				if (d[j]==0) id[t++] = j;
			}
}
bool search(int x)
{
	if (check[x]) return false;
	check[x] = true;
	for (int i=0;i<n;i++)
		if (g[x][i]==1)
		{
			if (fa[i]==-1) 
			{
				fa[i] = x;
				return true;
			}
			else if (search(fa[i])) 
			{
				fa[i] = x;
				return true;				
			}
		}
	return false;
}
int calc()
{
	memset(g,0,sizeof(g));
	for (int i=0;i<n;i++)
		for (int j=i+1;j<n;j++)
			if (smaller(i,j))
				g[i][j] = 1;
			else if (smaller(j,i))
				g[j][i] = 1;
	int ans = n;
	memset(fa,-1,sizeof(fa));
	for (int i=0;i<n;i++) {
		memset(check,false,sizeof(check));
		if (search(i)) ans--;
	}
	return ans;
}
int main()
{
	int t;
	cin>>t;
	for (int i=0; i<t;i++)
	{
		init();
		cout<<"Case #"<<i+1<<": "<<calc()<<endl;		
	}	
	return 0;
}
