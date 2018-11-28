#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

const int MAX_N = 12000000;

char cache[11][MAX_N];
int table[1 << 9];

char fill(int base, int x)
{
	assert(x < MAX_N);
	char &res = cache[base][x];
	if (res == 2)
		res = 0;
	if (res != -1)
		return res;
	res = 2;
	int nx = 0;
	while (x > 0) {
		int d = x % base;
		nx += d * d;
		x /= base;
	}
	res = fill(base, nx);
	return res;
}

int main()
{
	memset(cache, -1, sizeof(cache));
	for (int base = 2; base <= 10; ++base) 
		cache[base][1] = 1;
	
	memset(table, -1, sizeof(table));
	
	char buf[256];
	gets(buf);
	int T;
	istringstream(buf) >> T;
	for (int ncases = 1; ncases <= T; ++ncases) {
		gets(buf);
		istringstream iss(buf);
		int b;
		int set = 0;
		while (iss >> b) 
			set |= 1 << (b - 2);
		if (table[set] == -1) {
			int x;
			for (x = 2; x < MAX_N; ++x) {
				bool ok = true;
				for (int i = 0; i < 9; ++i)
					if ((set >> i & 1) == 1 && !fill(i + 2, x)) {
						ok = false;
						break;
					}
				if (ok)
					break;
			}
			table[set] = x;
		}
		printf("Case #%d: %d\n", ncases, table[set]);
	}
	return 0;
}
