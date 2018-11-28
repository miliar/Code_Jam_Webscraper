#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <ctime>

using namespace std;

#define SQR(x) ((x) * (x))
struct point{
	long long x;
	long long y;
	long long r;
	point (){}
	point (double _, double __, long long ___) : x(_), y(__), r(___){}
	bool isOverlap(point a){
		return sqrt(SQR((x - a.x)) + SQR((y - a.y))) + 1 < r + a.r;
	}
};

int main(){
	int tcase;
	cin >> tcase;
	
	srand(time(NULL));
	for(size_t casen = 0; casen < tcase; ++casen)
	{
		int N, W, L;
		cin >> N >> W >> L;
		pair<int,int> R[N];
		for (int i = 0 ; i < N ; i++){
			cin >> R[i].first;
			R[i].second = i;
		}
		
		vector< point > V;
		sort(R, R + N, greater<pair < int, int > >());
		
		int tr = 10;
		for (int i = 0 ; i < N ; i++){
			// int x = rand() % (int)(W * 100);
			// int y = rand() % (int)(L * 100);
			// point t((double)x/100, (double)y/100, R[i].first);
			long long x = rand() % W;
			long long y = rand() % L;
			point t((long long)x, (long long)y, R[i].first);

			bool isOverlapped = false;
			for (int j = 0 ; j < V.size() ; j++){
				if (t.isOverlap(V[j])) {isOverlapped = true; break;}
			}
			
			if (isOverlapped){
				i--;
				tr--;
			}else{
				V.push_back(t);
				tr = 10;
			}
			
			if (tr == 0){
				V.clear();
				i = -1;
			}
		}
		
		assert(V.size() == N);
		
		vector <point> VR(N);
		for (int i = 0 ; i < N ; i++){
			VR[R[i].second] = V[i];
		}
		
		
		cout << "Case #" << casen + 1 << ": ";
		
		for (int i = 0 ; i < N ; i++){
			if (i > 0) cout << " ";
			printf("%lld %lld", VR[i].x,VR[i].y);
		}
		cout << endl;
		
	}
	

	return 0;
}
