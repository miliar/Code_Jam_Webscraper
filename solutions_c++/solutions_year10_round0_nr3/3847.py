#include <iostream>
#include <queue>
using namespace std;

int main() {
	int testCount = 0;
	cin>>testCount;
	int kazanclar[testCount];

	int R,k,N;
	for(int i = 1 ; i <= testCount;i++){
		int kazanc = 0;

//		cout<<"Test "<<i<<endl;
		cin>>R;
		cin>>k;
		cin>>N;
//		cout<<"R="<<R<<" k="<<k<<" N="<<N<<endl;
		int g[N];

		queue<int> q;

		for(int j = 0; j < N; j++){
			cin>>g[j];
			q.push(g[j]);
		}

		for(int m = 0 ;m < R;m++){
			queue<int> requeue;

			int bindi = 0;
			while(!q.empty()){
				if(bindi+q.front()<=k){
					bindi += q.front();
					kazanc += q.front();
					requeue.push(q.front());
					q.pop();
				} else {
					break;
				}
			}

			while(!requeue.empty()){
				q.push(requeue.front());
				requeue.pop();
			}
		}


		kazanclar[i-1] = kazanc;
		kazanc=0;
	}

	for(int j= 0 ; j < testCount;j++){
		cout<<"Case #"<<j+1<<": "<<kazanclar[j]<<endl;
	}
}
