#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef struct{
	int beg;
	int end;
	int spd;
}workway;

int X, S, R;;
double T;
int N;
const int maxn = 1000;
workway w[maxn+5];
workway way[2*maxn+5];
int M;

bool cmp( workway a, workway b ){
	return a.beg < b.beg;
}

bool cmp2( workway a, workway b ){
	return a.spd < b.spd;
}

void Solve()
{
	sort( w, w+N, cmp);
	M = 0;
	int start = 0;
	for( int i = 0; i < N; i++ ){
		if( w[i].beg != start ){
			way[M].beg = start; way[M].end = w[i].beg; way[M].spd = S; M++;
		}
		way[M].beg = w[i].beg; way[M].end = w[i].end; way[M].spd = w[i].spd;
		start = w[i].end;
		M++;
	}
	if( way[M-1].end != X ){
		way[M].beg = way[M-1].end; way[M].end = X; way[M].spd = S; M++;
	}

	sort( way, way+M, cmp2 );
	
	/*
	for( int i = 0; i < M; i++ ){
		cout << way[i].beg << " " << way[i].spd << endl;
	}
	cout << endl;
	*/

	double ans = 0;
	int left = M;
	for( int i = 0; i < M; i++ ){
		double l = way[i].end-way[i].beg;
		double t = l/(way[i].spd+R-S);
		if( t <= T ){
			ans += t;
			T -= t;
		}
		else{
			double v = way[i].spd+R-S;
			double _l = l-v*T;
			ans += T;
			ans += _l / (way[i].spd);
			T = 0;
			left = i+1;
		}
		//cout << way[i].beg << " " << way[i].end << " " << way[i].spd << " " << ans << endl;
	}
	for( ;left < M; left++ ){
		ans += (way[left].end-way[left].beg)/way[left].spd;
		//cout << way[left].beg << " " << way[left].end << " " << way[left].spd << " " << ans << endl;
	}
	//cout << ans << endl;
	printf("%.8f\n",ans);

}

int main()
{
	freopen("A.in","r",stdin);

	int C;
	cin >> C;

	for( int i = 1; i <= C; i++ ){
		cin >> X >> S >> R >> T >> N;
		for( int j = 0; j < N; j++ ){
			cin >> w[j].beg >> w[j].end >> w[j].spd;
			w[j].spd += S;
		}
		printf("Case #%d: ", i);
		Solve();
	}
			
	return 0;
}
