#include <cstdio>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

char flood(int x, int y, vector <vector <int> > &map, vector <string> &p, char l)
{
	if (p[y][x] != '-') {
		return p[y][x];
	}
	int newd = -1;
	int minl = map[y][x];
	const int dx[] = { 0,-1, 1, 0};
	const int dy[] = {-1, 0, 0, 1};
	for (int d = 0; d < 4; d++) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		if (nx >= 0 && nx < map[0].size() &&
		    ny >= 0 && ny < map.size() &&
		    map[ny][nx] < minl) {
			newd = d;
			minl = map[ny][nx];
		}
	}
	if (newd >= 0) {
		p[y][x] = flood(x + dx[newd], y + dy[newd], map, p, l);
		return p[y][x];
	}
	return p[y][x] = l;
}

vector <string> Watersheds(vector <vector <int> > map)
{
	vector <string> p(map.size(), string(map[0].size(), '-'));
	char l = 'a';
	for (int y = 0; y < map.size(); y++) {
		for (int x = 0; x < map[0].size(); x++) {
			if (flood(x, y, map, p, l) == l) {
				l++;
			}
		}
	}
	return p;
}


int main()
{
	char inp[999];

	int cases;
	gets(inp); sscanf(inp, "%d", &cases);

	for (int caseno = 1; caseno <= cases; caseno++) {
		int H, W;
		gets(inp); sscanf(inp, "%d%d", &H, &W);
		
		vector <vector <int> > map(H);
		for (int y = 0; y < H; y++) {
			gets(inp); stringstream ss(inp);
			int v;
			while (ss >> v) {
				map[y].push_back(v);
			}
		}

		vector <string> ret = Watersheds(map);

		printf("Case #%d:\n", caseno);
		for (int y = 0; y < ret.size(); y++) {
			for (int x = 0; x < ret[y].size(); x++) {
				if (x != 0) {
					printf(" ");
				}
				printf("%c", ret[y][x]);
			}
			printf("\n");
		}
	}

	return 0;
}
