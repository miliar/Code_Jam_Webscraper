#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

struct walkWay{
	double b,e,l,w;
};

double x, s, r, t;
int n;
double time;
walkWay walkway[1001];

bool comp(walkWay a, walkWay b){
	return (a.w < b.w);
}

int main(){
	int tc, tn;
	int i,j;
	double tmp, tmp2;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tc;
	for (tn=0; tn<tc; tn++){
		cin >> x >> s >> r >> t >> n;
		time = 0;
		for (i=0; i<n; i++){
			cin >> walkway[i].b >> walkway[i].e >> walkway[i].w;
			walkway[i].l = walkway[i].e - walkway[i].b;
			x-=walkway[i].l;
			walkway[i].w+=s;
		}
		walkway[n].l = x;
		walkway[n].w = s;

		sort(walkway, walkway+n+1, comp);
		for (i=0; i<=n; i++){
			tmp = (walkway[i].l / (walkway[i].w+r-s));
			if (t >= tmp){
				t -= tmp;
				time += tmp;
			}else{
				time += t;
				tmp2 = walkway[i].l - t*(walkway[i].w+r-s);
				tmp2 /= walkway[i].w;
				time += tmp2;
				t=0;
			}
		}

		printf("Case #%d: %.6f\n", tn+1, time);

	}


	return 0;
}