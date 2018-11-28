#include <cstdio>
#include <queue>
using namespace std;

#define MAXM 10100

int mem[MAXM][2];
char gate[MAXM];
char changeable[MAXM];
char tree[MAXM];
int M;

int doit(int i, char v) {
	if(i > M)
		return -1;
	if(tree[i] == v)
		return 0;
	if(gate[i] == 2)
		return -1;
	if(mem[i][(int)v] > -2)
		return mem[i][(int)v];

	int a = doit(2*i,v);
	int b = doit(2*i+1,v);
	if(!changeable[i]) {
		if(v && gate[i]) {
			if(a == -1 || b == -1) {
				mem[i][(int)v] = -1;
				return -1;
			}
			mem[i][(int)v] = a+b;
			return a+b;
		}
		if(v && !gate[i]) {
			if(a == -1 && b == -1) {
				mem[i][(int)v] = -1;
				return -1;
			}
			if(a == -1) {
				mem[i][(int)v] = b;
				return b;
			}
			if(b == -1) {
				mem[i][(int)v] = a;
				return a;
			}
			mem[i][(int)v] = min(a,b);
			return min(a,b);
		}
		if(!v && gate[i]) {
			if(a == -1 && b == -1) {
				mem[i][(int)v] = -1;
				return -1;
			}
			if(a == -1) {
				mem[i][(int)v] = b;
				return b;
			}
			if(b == -1) {
				mem[i][(int)v] = a;
				return a;
			}
			mem[i][(int)v] = min(a,b);
			return min(a,b);
		}
		if(!v && !gate[i]) {
			if(a == -1 || b == -1) {
				mem[i][(int)v] = -1;
				return -1;
			}
			mem[i][(int)v] = a+b;
			return a+b;
		}
	}

	if(v) {
		int c;
		if(a == -1 || b == -1)
			c = -1;
		else
			c = a+b;
		int d;
		if(a == -1 && b == -1)
			d = -1;
		else if(a == -1)
			d = b;
		else if(b == -1)
			d = a;
		else
			d = min(a,b);

		if(c == -1 && d == -1) {
			mem[i][(int)v] = -1;
			return -1;
		}
		if(c == -1) {
			mem[i][(int)v] = d + gate[i];
			return d + gate[i];
		}
		if(d == -1) {
			mem[i][(int)v] = c + 1 - gate[i];
			return c + 1 - gate[i];
		}
		
		mem[i][(int)v] = min(c + 1 - gate[i], d + gate[i]);
		return min(c + 1 - gate[i], d + gate[i]);
	}

	int c;
	if(a == -1 || b == -1)
		c = -1;
	else
		c = a+b;
	int d;
	if(a == -1 && b == -1)
		d = -1;
	else if(a == -1)
		d = b;
	else if(b == -1)
		d = a;
	else
		d = min(a,b);

	if(c == -1 && d == -1) {
		mem[i][(int)v] = -1;
		return -1;
	}
	if(c == -1) {
		mem[i][(int)v] = d + 1 - gate[i];
		return d + 1 - gate[i];
	}
	if(d == -1) {
		mem[i][(int)v] = c + gate[i];
		return c + gate[i];
	}

	mem[i][(int)v] = min(c + gate[i], d + 1 - gate[i]);
	return min(c + gate[i], d + 1 - gate[i]);
}

int main() {
	int N;
	scanf("%d", &N);
	for(int t = 1; t <=N; ++t) {
		int V;
		scanf("%d %d", &M, &V);

		for(int i = 0; i < M; ++i) {
			tree[i+1] = 2;
			gate[i+1] = 2;
			mem[i+1][0] = -2;
			mem[i+1][1] = -2;
		}
		for(int i = 0; i < (M-1)/2; ++i) {
			int a,b;
			scanf("%d %d", &a, &b);
			gate[i+1] = (char)a;
			changeable[i+1] = (char)b;
		}
		for(int i = (M-1)/2; i < M; ++i) {
			int a;
			scanf("%d", &a);
			tree[i+1] = (char)a;
		}
		
		for(int i = M; i > 0; --i)
			if(tree[i] == 2) {
				if(gate[i] == 0)
					tree[i] = tree[2*i] || tree[2*i+1];	
				else {
					tree[i] = tree[2*i] && tree[2*i+1];
				}
			}
		
		int ret = doit(1,V);
		if(ret >= 0)
			printf("Case #%d: %d\n", t, ret);
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}

	return 0;
}
