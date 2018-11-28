#include <iostream>
#include <queue>

using namespace std;

int main(){
	int TEST; cin >> TEST;
	static int cnt[10001];
	for(int test=1;test<=TEST;test++){
		int N; cin >> N;
		memset(cnt, 0, sizeof(cnt));
		for(int i=0;i<N;i++){
			int t; cin >> t;
			cnt[t-1]++;
		}
		int res = (N==0 ? 0 : N);
		queue<int> qu;
		int cur = 0;
		for(int i=0;i<10001;i++){
			if(cnt[i] > cur){
				for(int j=cur;j<cnt[i];j++) qu.push(i);
			}
			else if(cnt[i] < cur){
				for(int j=cnt[i];j<cur;j++){
					int t = qu.front(); qu.pop();
					res = min(res, i-t);
				}
			}
			cur = cnt[i];
		}
		printf("Case #%d: %d\n", test, res);
	}
}
