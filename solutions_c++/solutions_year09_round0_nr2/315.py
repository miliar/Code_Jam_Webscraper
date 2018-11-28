#include<cstring>
#include<string>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<cstdio>
using namespace std;

int box[102][102];
int H, W;
char res[102][102];
bool done[102][102];

typedef pair<int, int> pint;


map <pint, set<pint> > m;
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};



void start(int x, int y)
{
	set<pint> q;
	int tx, ty;
	while(1)
	{
		done[x][y] = 1;
		q.insert(pint(x,y));

		int mind = box[x][y];
		for(int i=0; i<4; i++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if(!(nx>=0 && nx<H && ny>=0 && ny<W))
				continue;
		
			if(box[nx][ny] < mind)
			{
				tx = nx;
				ty = ny;
				mind = box[nx][ny];
			}
		}
		if(mind == box[x][y]) // (x, y) is a sink
		{
			if(m.find(pint(x,y))==m.end())
				m.insert(make_pair(pint(x,y), q));
			else
				m[pint(x,y)].insert(q.begin(), q.end());
			break;
		}
		x = tx;
		y = ty;
	}
}
void flood()
{
	memset(res, 0, sizeof(res));

	for(int i=0; i<H; ++i)
		for(int j=0; j<W; ++j) if(!done[i][j])
		{
			start(i, j);
		}

	vector<vector<pint> > v;
	map<pint, set<pint> >::iterator it;
	for(it=m.begin(); it!=m.end(); ++it)
	{
		v.push_back(vector<pint>(it->second.begin(), it->second.end()));
	}
	sort(v.begin(), v.end());
	for(int i=0; i<v.size(); ++i)
	{
		for(int j=0; j<v[i].size(); j++)
		{
			res[v[i][j].first][v[i][j].second] = i+'a';
		}
	}
}

void init()
{
	m.clear();
	memset(done, 0, sizeof(done));
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; ++c)
	{

		init();
		scanf("%d %d",&H, &W);
		for(int i=0; i<H; ++i)
			for(int j=0; j<W; j++)
			{
				scanf("%d", &box[i][j]);
			}
		flood();
		printf("Case #%d:\n", c);

		for(int i=0; i<H; ++i)
		{
			for(int j=0; j<W; j++)
			{
				if(j>0)
					printf(" ");
				putchar(res[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}