#include <string>
#include <cstring>
#include <climits>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
using namespace std;

//ifstream fin("c.in");
//#define cin fin
int P,Q;
int ps[10000];
int qs[100];
long long total;
long long solve(){
	long long cost = 0;
	memset(ps,0,sizeof(ps));
	for(int i = 0; i < Q; i ++){//release one by one
		int person = qs[i] - 1;
		ps[person] = -1;
		int j = person -1;
		while(j >= 0 && ps[j] != -1){
			cost ++;
			j--;
		}
		j = person + 1;
		while(j < P && ps[j] != -1){
			cost ++;
			j ++;
		}
	}
	return cost;
}
void max(int i){
	if(i == Q-1){
		long long cost = solve();
		if(cost < total){
			total = cost;
		}
	}

	for(int j = i; j < Q; j ++){
		int temp = qs[i];
		qs[i] = qs[j];
		qs[j] = temp;
		max(i+1);
		temp = qs[i];
		qs[i] = qs[j];
		qs[j] = temp;
	}
}

int main(){
	int T;
	cin>>T;
	for(int t = 1; t <= T; t ++){
		total = INT_MAX;
		cin>>P>>Q;
		for(int i = 0; i < Q; i ++){
			cin>>qs[i];
		}
		max(0);
		cout<<"Case #"<<t<<": "<<total<<endl;
	}
	return 0;
}
