#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int nt;
int n, m;
int from[2000], to[2000];

vector< set<int> > sets;

int cnt[2000];

vector<int> col;

bool rec(int color, int room)
{
	if (color == -1) return true;
	if (room == sets.size()) return rec(color - 1, 0);
	
	bool ok = false;
	int best = -1;
	
	set<int>::iterator p = sets[room].begin(), q = sets[room].end();
	while(p != q)
	{
		if (col[*p] == color) { ok = true; break;}
		
		if (col[*p] == -1)
		if (best == -1 || cnt[*p] > cnt[best]) best = *p;
		
		p++;
	}
	
	if (ok) return rec(color, room + 1);
	
	// try best
	
	if (best == -1) return false;
	
	col[best] = color;
	if (rec(color, room + 1)) return true;
	col[best] = -1;
	
	// try others
	p = sets[room].begin(), q = sets[room].end();
	while(p != q)
	{
		if (col[*p] == -1 && *p != best)
		{
			col[*p] = color;
			if (rec(color, room + 1)) return true;
			col[*p] = -1;
		}
		p++;		
	}
	
	return false;
}

bool good(int ncol)
{
	col.assign(n, -1);
	
	return rec(ncol - 1, 0);
}

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%d %d", &n, &m);
		
		for(int i = 0; i < m; i++) { scanf("%d", &from[i]); from[i]--;}
		for(int i = 0; i < m; i++) { scanf("%d", &to[i]); to[i]--;}
		
		sets.clear();
		
		set<int> all;
		for(int i = 0; i < n; i++) all.insert(i);
		
		sets.push_back(all);
	
		for(int i = 0; i < m; i++)
		{
			for(int j = 0; j < sets.size(); j++)
			if (sets[j].count(from[i]) && sets[j].count(to[i]))
			{
				set<int> a, b;
				set<int>::iterator p = sets[j].begin(), q = sets[j].end();
				while(*p != from[i] && *p != to[i])
				{
					a.insert(*p);
					p++;
				}
				a.insert(*p);
				b.insert(*p);
				p++;
				while(*p != from[i] && *p != to[i])
				{
					b.insert(*p);
					p++;
				}
				b.insert(*p);
				a.insert(*p);
				p++;
				while(p != q)
				{
					a.insert(*p);
					p++;
				}
				
				sets[j] = a;
				sets.push_back(b);
				
				break;
			}
		}
		
		for(int i = 0; i < n; i++) cnt[i] = 0;
		for(int i = 0; i < sets.size(); i++)
		{
			set<int>::iterator p = sets[i].begin(), q = sets[i].end();
			while(p != q)
			{
				cnt[*p]++;
				p++;
			}
		}
		
		/*for(int i = 0; i < sets.size(); i++)
		{
			set<int>::iterator p = sets[i].begin(), q = sets[i].end();
			puts("");
			while(p != q)
			{
				printf("%d ", *p);
				p++;
			}
			puts("");
		}*/
		
		int ncol = n;
		for(int i = 0; i < sets.size(); i++) if (sets[i].size() < ncol) ncol = sets[i].size();
		
		while(!good(ncol)) ncol--;
		
		printf("%d\n", ncol);
		for(int i = 0; i < n; i++)
		{
			if (i) printf(" ");
			if (col[i] == -1) col[i] = 0;
			printf("%d", col[i] + 1);
		}
		puts("");
	}
	
	return 0;
}