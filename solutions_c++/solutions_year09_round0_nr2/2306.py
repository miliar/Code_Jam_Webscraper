#include<cstdio>
#include<string>
#include<vector>
#include<utility>
#include<queue>

using namespace std;

int main() {
  int T,n,m,x,xx,y,yy,alt;
  int M[105][105];
	char label[105][105],cc;
  int dx[] = {-1,0,0,1};
  int dy[] = {0,-1,1,0};
  vector<pair<int,int> > P[101][101];
	queue<pair<int,int> > Q;

  scanf("%d\n",&T);
  for(int ii = 1;ii <= T;++ii)
  {
    for(int i = 0;i < 101;++i) for(int j = 0;j < 101;++j) P[i][j].clear();

    scanf("%d %d\n",&n,&m);
    for(int i=0;i< n;++i) for(int j =0;j < m;++j) scanf("%d",M[i]+j);

    for(int i = 0;i < n;++i) for(int j = 0;j < m;++j)
    {
			xx = -1, yy= -1, alt = M[i][j];
      for(int k=0;k<4;++k)
      {
        x = i + dx[k];
        y = j + dy[k];
				if(x >= 0 && x < n && y >= 0 && y < m && M[x][y] < alt)
				{
					xx = x, yy = y, alt = M[x][y];
				}
      }
			if(alt < M[i][j])
			{
				P[i][j].push_back(pair<int,int>(xx,yy));
				P[xx][yy].push_back(pair<int,int>(i,j));
				//printf("(%d,%d) --> (%d,%d)\n",i,j,xx,yy);
			}
    }

		memset(label,0,sizeof(label));
		cc = 'a';
		
		for(int i = 0;i < n;++i) for(int j = 0;j < m;++j) if(label[i][j] == 0)
		{
			label[i][j] = cc;
			cc++;
			Q.push(pair<int,int>(i,j));
			while(!Q.empty())
			{
				x = Q.front().first;
				y = Q.front().second;
				for(int k=0;k<P[x][y].size();++k)
				{
					if(label[P[x][y][k].first][P[x][y][k].second] == 0)
					{
						Q.push(pair<int,int>(P[x][y][k].first,P[x][y][k].second));
						label[P[x][y][k].first][P[x][y][k].second] = label[x][y];
					}
				}
				Q.pop();
			}
		}

		printf("Case #%d:\n",ii);
		for(int i = 0;i < n;++i)
		{
			for(int j = 0;j < m-1;++j) printf("%c ",label[i][j]);
			printf("%c\n",label[i][m-1]);
		}
	}
  return 0;
}

