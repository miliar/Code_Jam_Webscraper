#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;
vector<int> R,K,N;

int calculate(int num,queue<int>& groups) {
	int revenue=0;
	int fullSeats;
	for (int i=0;i<R[num];i++) {
		fullSeats=0;
		vector<int> waitingNext;
		while(fullSeats+groups.front()<=K[num]&&!groups.empty()) {
			int front = groups.front();
			fullSeats+=front;
			groups.pop();
			waitingNext.push_back(front);
		}
		for (int i=0;i<waitingNext.size();i++)
			groups.push(waitingNext[i]);
		revenue+=fullSeats;
	}
	return revenue;
}

int main() {
	int T;
	cin>>T;
	R = vector<int>(T);
	K = vector<int>(T);
	N = vector<int>(T);
	for(int i=0;i<T;i++) {
		cin>>R[i]>>K[i]>>N[i];
		queue<int> groups;
		for (int j=0;j<N[i];j++) {
			int tmp;
			cin>>tmp;
			groups.push(tmp);
		}
		cout<<"Case #"<<i+1<<": "<<calculate(i,groups)<<endl;
	}
	
	
}
