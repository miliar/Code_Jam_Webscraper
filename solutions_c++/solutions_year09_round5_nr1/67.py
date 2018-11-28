#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>

#define INF 1000000000

using namespace std;

// vector< pair<int, int> >

set< vector< pair<int, int> > > S;
vector< pair<int, int> > next;
int Sn;

vector< pair<int, int> > curr;
int N = 12, M = 12;
int n;
int show[13][13];
int T;
char str[222];

int DX[4] = {1, -1, 0, 0};
int DY[4] = {0, 0, 1, -1};

int a[13][13];
vector< pair<int, int> > begin;
vector< pair<int, int> > end;

queue< vector< pair<int, int> > > Q;

map< vector< pair<int, int> >, int > D;

void Go(int Dep)
{
	if(Dep ==  n)
	{
		vector< pair<int,int> > theme;
		theme = curr;
		sort(theme.begin(), theme.end());
		if(S.count(theme))
		{
		}
		else
		{
			S.insert(theme);
			/*
			int l1, l2;
			for(l1=0;l1<N;l1++) for(l2=0;l2<M;l2++) show[l1][l2] = 0;
			for(l1=0;l1<n;l1++) show[theme[l1].first][theme[l1].second] = 1;
			for(l1=0;l1<N;l1++)
			{
				for(l2=0;l2<M;l2++)
				{
					if(show[l1][l2]) printf("#");
					else printf(".");
				}
				printf("\n");
			}
			printf("\n");
			*/
		}
	}
	else if(Dep == 0)
	{
		int l1, l2;
		for(l1=0;l1<N;l1++) for(l2=0;l2<M;l2++)
		{
			curr[0].first = l1;
			curr[0].second = l2;
			Go(Dep + 1);
		}
	}
	else
	{
		int l1, l2, l3;
		for(l1=0;l1<N;l1++)
		{
			for(l2=0;l2<M;l2++)
			{
				int wrong = 0;

				for(l3=0;l3<Dep;l3++)
				{
					if(curr[l3].first == l1 && curr[l3].second == l2)
					{
						wrong = 1;
						break;
					}
				}
				if(!wrong)
				{
					int ok = 0;
					for(l3=0;l3<Dep;l3++)
					{
						int dx = curr[l3].first - l1;
						int dy = curr[l3].second - l2;
						if((dx == 1 && dy == 0) || (dx == -1 && dy == 0) || (dx == 0 && dy == -1) || (dx == 0 && dy == 1))
						{
							ok = 1;
							break;
						}
					}
					if(ok)
					{
						curr[Dep].first = l1;
						curr[Dep].second = l2;
						Go(Dep + 1);
					}
				}
			}
		}
	}
}

int main(void)
{
	int l0, l1, l2, l3;

	int T;
	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);

	scanf("%d",&T);


	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d",&N,&M);
		S.clear();
		begin.clear();
		end.clear();
		for(l1=0;l1<N;l1++)
		{
			scanf("%s",str);
			for(l2=0;l2<M;l2++)
			{
				if(str[l2] == '.')
				{
					a[l1][l2] = 1;
				}
				else if(str[l2] == '#')
				{
					a[l1][l2] = 0;
				}
				else if(str[l2] == 'x')
				{
					end.push_back( make_pair(l1, l2) );
					a[l1][l2] = 1;
				}
				else if(str[l2] == 'o')
				{
					begin.push_back( make_pair(l1, l2) );
					a[l1][l2] = 1;
				}
				else if(str[l2] == 'w')
				{
					begin.push_back( make_pair(l1, l2) );
					end.push_back( make_pair(l1, l2) );
					a[l1][l2] = 1;
				}
			}
		}
		n = begin.size();
		curr.resize(n);
		Go(0);

		sort(begin.begin(), begin.end());
		sort(end.begin(), end.end());

		Q.push(begin);

		Sn = S.size();
		D.clear();
		D[ begin ] = 0;


		while(!Q.empty())
		{
			curr=Q.front();
			Q.pop();
			int st1 = S.count(curr);
			int ohyes = D[curr];


			for(l1=0;l1<n;l1++)
			{
				for(l2=0;l2<4;l2++)
				{
					next = curr;
					int ox = next[l1].first - DX[l2];
					int oy = next[l1].second - DY[l2];
					if(ox < 0 || ox >= N || oy < 0 || oy >= M) continue;
					if(a[ox][oy] == 0) continue;
					for(l3=0;l3<n;l3++)
					{
						if(next[l3].first == ox && next[l3].second == oy) break;
					}
					if(l3 < n) continue;
					next[l1].first += DX[l2];
					next[l1].second += DY[l2];
					if(next[l1].first < 0 || next[l1].first >= N || next[l1].second < 0 || next[l1].second >= M)
						continue;
					if(a[next[l1].first][next[l1].second] == 0) continue;
					for(l3=0;l3<n;l3++)
					{
						if(l1 != l3 && next[l1].first == next[l3].first && next[l1].second == next[l3].second) break;
					}
					if(l3 < n) continue;


					sort(next.begin(),next.end());
					int st2 = S.count(next);
					if(st1 == 0 && st2 == 0) continue;

					if(D.count(next) == 0)
					{
						D[next ] =ohyes + 1;
						Q.push(next);
					}
				}
			}


		}

		int the_ret;
		if(D.count(end))
		{
			the_ret = D[end];
		}
		else
		{
			the_ret = -1;
		}
		printf("Case #%d: %d\n",l0,the_ret);
	}

}
