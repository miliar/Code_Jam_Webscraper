#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)

int n, m[2024], p[2024];
int mem[2024][20];
int inf = 999999999;

int go(int pos, int cnt) {
	if (mem[pos][cnt] < 0) {
		int tot = (1<<n)-1;
		mem[pos][cnt] = inf;

		if (pos < (1<<(n-1))) {
			int t1 = pos*2, t2 = pos*2+1;
			if (m[t1]-cnt < 0 || m[t2]-cnt<0) return inf;
			if (m[t1]-cnt == 0 || m[t2]-cnt==0) mem[pos][cnt] = p[pos];
			else mem[pos][cnt] = 0;
		} else {
			int p1 = tot-1-((tot-1-pos)*2+1);
			int p2 = tot-1-((tot-1-pos)*2+2);
			int c1 = go(p1,cnt+1)+go(p2,cnt+1);
			if (c1 < mem[pos][cnt]) mem[pos][cnt] = c1;
			c1 = go(p1,cnt)+go(p2,cnt)+p[pos];
			if (c1 < mem[pos][cnt]) mem[pos][cnt] = c1;
		}
	}

	return mem[pos][cnt];
}

int main() 
{
	ifstream fin("b.in");
	ofstream fout("b.out");

	int tc;

	fin >> tc;

	REP(t,tc) {
		fin >> n;
		REP(i,1<<n) fin >> m[i];
		REP(i,(1<<n)-1) fin >> p[i];

		memset(mem, -1, sizeof(mem));
		fout << "Case #" << t+1 << ": " << go((1<<n)-2, 0) << endl;
	}

	fout.close();

	return 0;
}