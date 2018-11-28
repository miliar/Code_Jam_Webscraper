#include <iostream>
#include <vector>

using namespace std;

main(){
	int T, R, k, N, temp, sum, qsize, money, e;
	vector<int> queue;
	cin >> T;
	for(int i=1;i<=T;++i){
		cin >> R >> k >> N;
		money=0;
		sum=0;
		queue.clear();
		for(int j=0;j<N;++j){
			cin >> temp;
			queue.push_back(temp);
		}
		qsize=queue.size();
		for(int j=0;R!=0;){
			if( (sum+queue[j])<=k && e<qsize){
				sum+=queue[j];
				++j;
				++e;
			}	
			else{
				money+=sum;
				sum=0;
				e=0;
				R--;
			}
			j%=qsize;
		}
		cout << "Case #" << i << ": ";
		cout << money << endl;
	}
}
