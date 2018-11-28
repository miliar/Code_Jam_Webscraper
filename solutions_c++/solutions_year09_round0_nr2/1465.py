#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};

int a[101][101];
char res[101][101];
char cur;
int n,m;

void solve(int x,int y)
{
	if (res[x][y]!='0')
		return;

	vector<pair<int,int> > v;
	for (int i=0;i<4;i++)
	{
		int nx=x+dx[i];
		int ny=y+dy[i];
		if (nx<0||nx>=n||ny<0||ny>=m)
			continue;

		v.push_back(make_pair(a[nx][ny],i));
	}

	sort(v.begin(),v.end());
	if (v.size()==0||v[0].first>=a[x][y])
	{
		res[x][y]=cur++;
		return;
	}

	int nx=x+dx[v[0].second];
	int ny=y+dy[v[0].second];
	solve(nx,ny);
	res[x][y]=res[nx][ny];
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d\n",&T);
	for (int test=0;test<T;test++)
	{
		vector<pair<int,int> > v;

		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				scanf("%d",&a[i][j]);

		memset(res,'0',sizeof(res));
		cur='a';
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				solve(i,j);

		printf("Case #%d:\n",test+1);
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				printf("%c%c",res[i][j],(j==m-1?'\n':' '));
	}
	return 0;
}