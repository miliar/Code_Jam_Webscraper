#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <deque>

using namespace std;

struct snapper {
	int power;
	int status;
};

int gc = 1;

int calc(int r, int k, deque<int>& dg) {
	int result = 0, g = 0, t;
	size_t s = dg.size();
	for(int i = 0; i < r ; i++) {
		g = 0;
		for(int j = 0; j < s; j++) {
			t = dg.front();
			if(g + t <= k) {
				g += t;
				dg.pop_front();
				dg.push_back(t);
			} else {
				break;
			}
		}
		result += g;
	}
	return result;
}

int doit(const char* in, const char* out) {
	char buffer[10240] = {0};
	FILE* fo = fopen(out, "w");
	FILE* fi = fopen(in, "r");
	if(!fi) {
		perror("fopen");
		return -1;
	}
	int g = atoi(fgets(buffer,sizeof(buffer),fi));
	for(int i = 0; i < g; i++) {
		int r, k, t;
		char* pos;
		deque<int> dg;
		fgets(buffer, sizeof(buffer), fi);
		sscanf(buffer, "%d %d %d", &r, &k, &t);
		pos = fgets(buffer, sizeof(buffer), fi);
		for(int j = 0; j < t; j++) {
			dg.push_back(atoi(pos));
			pos = strchr(pos, ' ') + 1;
		}
		int result = calc(r, k, dg);
		fprintf(fo, "Case #%d: %d\n", gc++, result);
	}
	fclose(fi);
	fclose(fo);
}

int main() {
	doit("C:/C-small-attempt0.in", "C:/out.in");
	return 0;
}
