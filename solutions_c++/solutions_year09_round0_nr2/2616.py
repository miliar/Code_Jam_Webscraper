#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define For(i,b) for(int i = 0; i < (int)b; ++i)
#define Fori(i,a,b) for(int i = a; i < (int)b; ++i)
#define Ford(i,a,b) for(int i = a; i >=b; --i)
#define All(t) t.begin(),t.end()
#define Sort(a) sort(All(a))
#define Fill(a,b) memset(a,b,sizeof(a))
#define Forstl(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define db(x) cout << #x << " = " << x << endl
#define mod(A, B) ((((A) % (B)) + (B)) % (B))
#define Exist(container, element) (container.find(element) != container.end())
#define sz(a) int((a).size()) 
#define valid(i,j) (i>=0 && i<H && j>=0 && j<W)
#define mp make_pair

typedef long long ll;
typedef pair<int,int> pii;

template <class T>
void out(vector<T> v)
{
  cout << "{";
  For(_i,v.size()) {if(_i) cout<<","; cout<<v[_i];}
  cout<<"}"<<endl;
}

const int MAX = 110;

int elevationMap[MAX][MAX];
char ans[MAX][MAX];
//bool G[MAX*MAX][MAX*MAX];
map<pair<pii,pii > ,bool> G;
bool vis[MAX][MAX];
char letter;
int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};
int T, W, H, n;

/*
void dfs(int i)
{
	vis[i] = 1;
	ans[i/H][i%W] = letter;
	For(j,n)
	    if(G[i][j] && !vis[j])
	        dfs(j);
}
*/

int main ()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small.txt");
	
	fin >> T;
	For(z,T)
	{
		fin >> H >> W;
		Fill(elevationMap,-1);
		G.clear();
		For(i,H)
		{
			For(j,W)
			{
				For(ii,H)
				{
					For(jj,W)
					{
                        G[mp(pii(i,j),pii(ii,jj))] = 0;
					}
				}
			}
		}
		For(i,H)
		{
			For(j,W)
			{
				fin >> elevationMap[i][j];
			}
		}
		vector<pii > sinks;
		For(i,H)
		{
			For(j,W)
			{
				int mini = INT_MAX, dir = -1;
				For(d,4)
				{
					int ni = i + di[d], nj = j + dj[d];
					if(!valid(ni,nj)) continue;
					if(mini > elevationMap[ni][nj])
					{
						mini = elevationMap[ni][nj];
						dir = d;
					}
				}
				if(elevationMap[i][j] <= mini)
				{
					sinks.push_back(pii(i,j));
				}
				else
				{
			        int ni = i + di[dir], nj = j + dj[dir];
			        G[mp(pii(i,j),pii(ni,nj))] = 1;
				}
			}
		}

		n = H * W;

		For(ki,H)
		{
			For(kj,W)
			{
				For(ii,H)
				{
					For(ij,W)
					{
						For(ji,H)
						{
							For(jj,W)
							{
								G[mp(pii(ii,ij),pii(ji,jj))] |= (G[mp(pii(ii,ij),pii(ki,kj))] && G[mp(pii(ki,kj),pii(ji,jj))]);
							}
						}
					}
				}
			}
		}

		map<pii ,char> sinkChar;
		char letter = 'a';
		For(i, H) For(j,W)
		{
			pii cur = pii(i,j);
			if(find(All(sinks),cur) != sinks.end())
			{
                if(!sinkChar.count(cur))
				{
					sinkChar[cur] = letter++;
				}
				//printf("sinkChar[%d] = %c\n",i,sinkChar[i]);
				ans[i][j] = sinkChar[cur];
				continue;
			}
			Forstl(it,sinks)
			{
				pii cur2 = pii(it->first,it->second);
				if(G[mp(pii(i,j),cur2)])
				{
					if(!sinkChar.count(cur2))
					{
						sinkChar[cur2] = letter++;
					}
					//printf("sinkChar[%d] = %c\n",sinks[j],sinkChar[sinks[j]]);
					//db(sinkChar[sinks[j]]);
					ans[i][j] = sinkChar[cur2];
					break;
				}
			}
		}
		
		fout << "Case #" << z+1 << ":" << endl;
		For(i,H)
		{
			For(j,W)
			{
				if(j) fout << " ";
				fout << ans[i][j];
			}
			fout << endl;
		}
	}
	db("Done");
	getchar();
	return 0;
}
