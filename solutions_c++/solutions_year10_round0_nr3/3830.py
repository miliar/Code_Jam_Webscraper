#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <vector>
#include <queue>
#include <stdint.h>

using namespace std;
bool compareQ(queue<long int>& q1, queue<long int>& q2){
	int sz = q1.size();
	if(sz != q2.size()) return false;
	for(long int i = 0; i<sz;i++){
		
	}
	return false;
}

void solThemePark(long int& R, long int& k, long int& N,queue<long int>& groups){
	uint64_t ret =0, rep =0, count=0;
	
	queue<long int> old = groups;
	for(long int i=1; i<=R;i++){
		long int sum =0;
		vector<long int> cur;
		do{
			long int val = groups.front();
			if(sum+val <= k ){
				sum += val;
				cur.push_back(val);
				groups.pop();
			}
			else{
				ret += sum;
				for(int j=0; j<cur.size();j++){
					groups.push(cur[j]);
				}
				break;
			}
			if(groups.empty()){
				ret += sum;
				for(int j=0; j<cur.size();j++){
					groups.push(cur[j]);
				}
				if(old == groups){
					long int temp = R / i;
					rep = ret; count = temp;
					ret =0;
					temp = R %i;
					i = R-temp;
				}
				break;
			}
		}while(1);
	}
	if(rep ==0){
		cout<< ret;
	}
	else{
		cout<< rep*count + ret;
	}
}


int main(int argc, char* argv[]){
	//cout<<"calling function\n";
	int num;
	cin>>num;
	for(int i=0;i<num;i++){
		long int N,k,R;
		queue<long int> groups;
		cin>>R>>k>>N;
		int val;

		for(long int j=0;j<N;j++){
			cin >> val;
			groups.push(val);
		}
		
		cout<<"Case #"<<i+1<<": ";solThemePark(R,k,N, groups);cout<<endl;
	}
	return 0;	
}
