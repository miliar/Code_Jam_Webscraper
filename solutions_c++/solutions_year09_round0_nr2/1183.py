#include <iostream>
using namespace std;
int alt[10010];
int pos[10010];
int h, w, n;
void fursort()
{
	int count[10010];
	for(int i=0; i<10010; i++) count[i] = 0;
	for(int i=0; i<n; i++) count[alt[i]] ++;
	for(int i=0; i<10005; i++) count[i+1] += count[i];
	for(int i=n-1; i>=0; i--)
	{
		count[alt[i]] --;
		pos[count[alt[i]]] = i;
	}
}
int dir[4];
bool check(int u, int d)
{
	if(u + dir[d] < 0) return false;
	if(u + dir[d] >= n) return false;
	if(u%w + dir[d]%w != (u+dir[d])%w) return false;
	return true;
}
void work()
{
	int root[10010];
	char glyph[10010];
	for(int i=0; i<n; i++)
	{
		int u = pos[i];
		root[u] = u;
		for(int d=0; d<4; d++) if(check(u, d))
		{
			int v = u + dir[d];
			if(alt[v] < alt[root[u]]) root[u] = v;
		}
		if(root[u] == u)
		{
			glyph[u] = 'a'-1;
		}
		else root[u] = root[root[u]];
	}
	int gcount = 0;
	for(int i=0; i<n; i++)
	{
		if(glyph[root[i]] < 'a')
		{
			glyph[root[i]] = 'a' + gcount;
			gcount ++;
		}
	}
	for(int i=0; i<h; i++)
	{
		for(int j=0; j<w; j++)
		{
			int u = i*w + j;
			cout << glyph[root[u]];
			if(j == w-1) cout << endl;
			else cout << ' ';
		}
	}
}
int main()
{
	int t;
	cin >> t;
	for(int c = 0; c < t; c ++)
	{
		cin >> h >> w;
		dir[0] = -w;
		dir[1] = -1;
		dir[2] = 1;
		dir[3] = w;
		n = h * w;
		for(int i=0; i<n; i++) cin >> alt[i];
		fursort();
		cout << "Case #" << c+1 << ":\n";
		work();
	}
	return 0;
}
