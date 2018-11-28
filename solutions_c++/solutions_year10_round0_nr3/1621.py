#include <iostream>

using namespace std;

int g[1010];
int next[1010];
int money[1010];
bool seen[1010];

int main() {
	int T,R,k,N;
	cin>>T;
	for(int t=0;t<T;t++) {
		long long result = 0LL;
		cin>>R>>k>>N;
		for(int n=0;n<N;n++) {
			cin>>g[n];
		}
		for(int n=0;n<N;n++) {
			money[n] = 0;
			for(int m=0;m<N;m++) {
				int cur = (n+m)%N;
				int nxt = (n+m+1)%N;
				if(money[n]+g[cur]<=k) {
					money[n]+=g[cur];
					next[n] = nxt;
				}
				else break;
			}
		}
		memset(seen,0,sizeof(seen));
		int lid = 0;
		int loopsize = 0;
		int beforeloop = 0;
		long long loopmoney = 0LL;
		int id = 0;
		while(true) {
			if(seen[lid])break;
			seen[lid] = true;
			lid = next[lid];
		}

		id=0;
		while(id!=lid){
			beforeloop++;
			id = next[id];
		}

		id=lid;
		do {
			loopmoney+=money[id];
			id=next[id];
			loopsize++;
		} while (id!=lid);

		id = 0;
		for(int i=0;i<beforeloop;i++) {
			result+=money[id];
			id = next[id];
		}

		if(R>beforeloop) {
			long long looptime = (R-beforeloop)/loopsize;
			result+=looptime*loopmoney;
			int rem = (R-beforeloop)%loopsize;
			id = lid;
			for(int i=0;i<rem;i++) {
				result+=money[id];
				id = next[id];
			}	
		}


		

		cout<<"Case #"<<(t+1)<<": "<<result<<endl;		
	}	
}
