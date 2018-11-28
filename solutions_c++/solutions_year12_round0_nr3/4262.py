#include<iostream>
#include<queue>
#include<vector>
#include<string>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#define pb push_back
#define INF (1 << 28)
#define EPS (1e-9)
#define mp(x,y) make_pair(x,y)
#define rep(i,n) for(int i = 0; i < n; i++)
#define REP(i,n) for(int i = 0; i <= n; i++)



using namespace std;

int main(){
	int T;
	cin >> T;
	for(int Case = 1; Case <= T; Case++){
		set<pair<int,int> > ans;
		int A,B;
		int digit = 0;
		cin >> A >> B;
		int t = A;
		while(t){
			digit++;
			t /= 10;
		}

		for(int i = A; i <= B; i++){
			for(int k = 1; k < digit; k++){
				int n = 0;
				for(int j = digit - 1; j >= 0 ; j--){
					n *= 10;
					n += i / (int)pow((double)10,(double)((k + j) % digit)) % 10;
				}
				if(n >= A && n <= B && i < n){
						ans.insert(make_pair(i,n));
				}
						


			}

		}
		cout << "Case #" << Case << ": " << ans.size() << endl;
	}


	return 0;
}

