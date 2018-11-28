#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;


int price;
int total;
vector<int> qts;
void go(int a1, int a2){
	if(a1 == a2-1){
		if(qts[a1] || qts[a2])
			total+=price;
		return;
	}

	int sz = (a2-a1)+1;
	int lastmid = a1+sz/2;
	bool tem=false;
	for(int i = a1; i <= a2; i++){
		if(qts[i] > 0) tem = true;		

	}

	if(!tem) return;
	total += price;
	for(int i = a1; i <= a2; i++) if(qts[i]) qts[i]--;
	go(a1,lastmid-1);
	go(lastmid, a2);
}


int main(void){
	int N;
	cin >> N;
	for(int cas = 1; cas <= N; cas++){
		int n;
		cin >> n;
		qts = vector<int>(1<<n);
		for(int i = 0; i < (1<<n); i++){
			cin >> qts[i];
			qts[i] = n - qts[i];
		}

		vector<vector<int> > prices(n);
		for(int i = 0; i < n; i++){
			int qt = (1<<(n-i-1));
			vector<int> at(qt);
			for(int j = 0; j < qt; j++) cin >> at[j];
			prices[i] = at;
		}

		price=prices[0][0];
		total = 0;
		go(0,(1<<n)-1);

		printf("Case #%d: %d\n",cas,total);


	}

	return 0;
}
