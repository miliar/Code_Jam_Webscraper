#include <iostream>
#include <string>
#include <vector>

using namespace std;

int ans = 0;
int T, N;
int S,pb;

struct Tri
{
	int a,b,c;
};
void chk(vector<Tri> cur)
{
	int surprising = 0;
	int b = 0;
	for(int i = 0; i< cur.size(); ++i)
	{
		int tmin = min(cur[i].a,min(cur[i].b,cur[i].c));
		int tmax = max(cur[i].a,max(cur[i].b,cur[i].c));
		if(tmax- tmin == 2)
		{
			surprising ++;
		}
		if(tmax >= pb) b++;
	}
	if(surprising == S)
	{
		ans = max(ans,b);
	}
	return ;
}

void dfs(vector<vector<Tri> > p, vector<Tri> cur, int ci, int n)
{
	if(ci == n)
	{
		chk(cur);
		return ;
	}
	for(int i = 0; i< p[ci].size(); ++i)
	{
		cur[ci] = p[ci][i];
		dfs(p,cur,ci+1,n);
	}
}
int main()
{
	
	cin >> T;
	for(int t = 0; t< T; ++t)
	{
		cin >> N >> S >> pb;
		int *sum = new int[N];
		vector<vector<Tri> > possible;
		for(int i = 0; i< N; ++i)
		{
			cin >> sum[i];
			vector<Tri> np;
			for(int i1 = 0; i1<= 10; ++i1)
			{
				for(int i2 = 0; i2<= 10; ++i2)
				{
					for(int i3 = 0; i3<= 10; ++i3)
					{
						if(i1+i2+i3 == sum[i])
						{
							int tmin = min(i1,min(i2,i3));
							int tmax = max(i1,max(i2,i3));
							
							
							if(tmax-tmin<=2) 
							{
								Tri tmp;
								tmp.a = i1; tmp.b = i2; tmp.c = i3;
								np.push_back(tmp);
							}
						}
					}
				}
			}
			possible.push_back(np);
		}
		vector<Tri> Cur(possible.size());
		ans = 0;
		dfs(possible,Cur,0,possible.size());
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0;
}