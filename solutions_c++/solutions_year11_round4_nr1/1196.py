#include <stdio.h>
#include <algorithm>

using namespace std;

int X, S, R, t, N;
int Table[1100000];

void Set(int b, int e, int w)
{
	for(int i = b; i < e; i++)
		Table[i] = w;
}

void Read()
{
	scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);
	memset(Table, 0, sizeof(Table));
	for(int i = 0; i < N; i++){
		int B, E, w;
		scanf("%d %d %d", &B, &E, &w);
		Set(B, E, w);
	}
	sort(Table, Table+X);
}

double Solve()
{
	double res = 0, t1 = t;
	for(int i = 0; i < X; i++){
		if(t1 > 0){
			double s = (R+Table[i])*t1;
			if(s > 1){
				double t0 = 1.0/(R+Table[i]);
				res += t0;
				t1 -= t0;
			}else{
				res += t1;
				double t0 = (1.0-s)/(S+Table[i]);
				res += t0;
				t1 = -1;
			}
		}else{
			res += 1.0/(S+Table[i]);
		}
	}
	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		Read();
		printf("Case #%d: %.10f\n", i, Solve());
	}
	return 0;
}

