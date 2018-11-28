#include<cstdio>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;
int tc,L,t,N,C;
int main(){ 
	scanf("%d",&tc);
	for (int ti = 1; ti <= tc; ti++) {
		scanf("%d %d %d %d\n",&L, &t, &N, &C);
		vector<int> v2;
		vector<int> v3;
		int temp;
		int sum = 0;
		int sum1 = 0;
		for (int i = 1; i <= C; i++) {
			scanf("%d",&temp);
			sum += temp;
			v2.push_back(temp);
			if (i == 1) v3.push_back(temp);
			else v3.push_back(v3[v3.size()-1]+temp);
		}
		sum *= 2;
		int total = 0;
		int current = 0;
		vector<pair<int,int> > v;
		bool flag = false;
		while (true) {

			if (current+C <= N) {
				
				if (total+sum >= t) {
				
					for (int i = 0; i < C; i++) {
						if (flag) v.push_back(make_pair(v2[i], 1));
						else if (total + v2[i]*2 <= t) total += v2[i]*2;
						else {
							flag = true;
							v.push_back(make_pair((total+v2[i]*2-t)/2, 1));							
							total = t;
//							total += t;

						}
					}
					current += C;
				} else {
					total += sum;
					current += C;
				}
			}
			else {
				if (total+v3[N-current] * 2 >= t) {
					for (int i = N-current; i < C; i++) {
						if (flag) v.push_back(make_pair(v2[i], 1));
						else if (total + v2[i]*2 <= t) total += v2[i]*2;
						else {
							flag = true;
							v.push_back(make_pair((total+2*v2[i]-t)/2, 1));
							total = t;
						//	total += t

						}
					}				
					current = N;
				} else {
					total += (v3[N-current])*2;
					current = N;
				}
			}
			
			if (current == N) break;
		
		}
		
		sort (v.begin(),v.end());
		for (int i = v.size()-1; i >= 0; i--) {
			if (L > 0) {
				L--;
				total += v[i].first;
			} else total += v[i].first*2;
		}

		
		printf("Case #%d: %d\n",ti, total);
		
	}
}