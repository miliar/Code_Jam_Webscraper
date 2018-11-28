#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;

struct snapper {
	int power;
	int status;
};

int gc = 1;

void dump(vector<snapper>& vs) {
	return;
	puts("--------P-------S--------------------------------");
	for(int i = 0; i < vs.size(); i++) {
		printf("%d):\t%d\t%d\n", i, vs[i].power, vs[i].status);	
	}
	puts("-------------------------------------------------");
}

// 1. from 1 ... n; if snap have power, then switch status, 
//    until the first unpowered snap, turn all of the rest to power off
// 2. if the first one have power and status on; then next one have power too

int snap(vector<snapper>& vs) {
	size_t s = vs.size();
	for(int i = s - 1; i > 0; i--) {
		if(vs[i - 1].power && vs[i - 1].status) {
			vs[i].status = !vs[i].status;
		}
	}
	vs[0].status = !vs[0].status;
	for(int i = 1; i < s; i++) {
		if(vs[i - 1].power && vs[i - 1].status) {
			vs[i].power = 1;
		} else {
			vs[i].power = 0;
		}
	}
}

int calc(int  n, int k) {
	vector<snapper> vs;
	snapper s = {0};
	for(int i = 0; i < n; i++) {
		vs.push_back(s);
	}
	vs[0].power = 1;
	for(int i = 0; i < k; i++) {
		snap(vs);
	}
	if(vs.back().power && vs.back().status) {
		return 0;
	}
	return -1;
}

int doit(const char* in, const char* out) {
	char buffer[32] = {0};
	FILE* fo = fopen(out, "w");
	FILE* fi = fopen(in, "r");
	if(!fi) {
		perror("fopen");
		return -1;
	}
	int total = atoi(fgets(buffer,sizeof(buffer),fi));
	int n, k;
	for(int i = 0; i < total; i++) {
		fgets(buffer, sizeof(buffer), fi);
		sscanf(buffer, "%d %d", &n, &k);
		if(calc(n, k) == 0) {
			fprintf(fo, "Case #%d: ON\n", gc++);
		} else {
			fprintf(fo, "Case #%d: OFF\n", gc++);
		}
	}
	fclose(fi);
	fclose(fo);
}

int main() {
	doit("C:/A-small-attempt2.in", "C:/out.in");
	return 0;
}
