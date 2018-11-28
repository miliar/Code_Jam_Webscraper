#include<iostream>
using namespace std;
int X[1000], V[1000], P[1000];

int main() {
    int t,Ts,N,K,B,T,i,j,cnt,tot;
    cin>>Ts;
    for(t=1;t<=Ts;t++) {
		cin>>N>>K>>B>>T;
		for(i=0;i<N;i++) cin>>X[i];
		for(i=0;i<N;i++) cin>>V[i];
		for(i=0;i<N;i++) P[N-1-i] = (B-X[i] <= V[i]*T);
		cnt = 0;
		tot = 0;
		for(i=0;i<N && cnt<K;i++) {
			if(!P[i]) continue;
			tot += i-cnt;		
			cnt++;
		}
		cout<<"Case #"<<t<<": ";
		if(cnt<K) cout<<"IMPOSSIBLE\n";
		else cout<<tot<<endl;
    }
    return 0;
}
