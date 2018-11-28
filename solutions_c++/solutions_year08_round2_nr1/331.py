#include <cstdio>
#include <iostream>
using namespace std;
#include <vector>

int t,n,A,B,C,D,x0,y0,M;
vector<pair<int, int> > a;

long long col[3][3];

long long calc(){
	long long zog = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < i; j++)
			for (int k = 0; k < j; k++)
				if ((a[i].first+a[j].first+a[k].first)%3==0)
					if ((a[i].second+a[j].second+a[k].second)%3==0)
						zog++;
	return zog;
}

long long calc2(){
//	for (int i = 0; i < 3; i++){
//		for (int j = 0; j < 3; j++) printf("%d", col[i][j]);
//		printf("\n");
//	}
	long long zog = 0;
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++)
			for (int k = 0; k < 9; k++){
				pair<int,int> p1 = make_pair(i/3,i%3);
				pair<int,int> p2 = make_pair(j/3,j%3);
				pair<int,int> p3 = make_pair(k/3,k%3);
				if ((p1.first+p2.first+p3.first)%3==0)
				if ((p1.second+p2.second+p3.second)%3==0){
				long long e = 1;
				long long tmp;

				tmp = col[p1.first][p1.second];
				e *= tmp;

				tmp = col[p2.first][p2.second];
				if (p1==p2) tmp--;
				e *= tmp;

				tmp = col[p3.first][p3.second];
				if (p1==p3) tmp--;
				if (p2==p3) tmp--;
				e *= tmp;

				zog += e;
				}


				
			}
	return zog/6;
}

int main(){
	freopen("crop.in", "rt", stdin);
	freopen("crop.out", "wt", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		cerr<<i<<endl;
		a.clear();
		for (int s = 0; s < 3; s++)
			for (int t = 0; t < 3; t++) col[s][t] = 0;
		for (int j = 0; j < n; j++){
			a.push_back(make_pair(x0%3,y0%3));
//			printf("%d %d\n", x0%3, y0%3);
			col[x0%3][y0%3]++;
			long long tmp = x0;
			x0 = (A*tmp+B)%M;
			tmp = y0;
			y0 = (C*tmp+D)%M;
		}
		if (n<10000){
		if (calc()!=calc2()) printf("BUG");
		}
		cout<<"Case #"<<i<<": "<<calc2()<<endl;
	}
}
