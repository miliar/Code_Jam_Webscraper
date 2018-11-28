#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;
int compute(vector<int> candy);
bool equalpat(vector <int>sean, vector <int>patrick);
int totalpat(vector<int> pile);
int sum(vector<int>);

int main() {
	int t, n, k;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cin>>n;
		vector<int> candy;
		for(int j=0;j<n;j++) {
			cin>>k;
			candy.push_back(k);			
		}
		int sean = compute(candy);
		if(sean>0) {
			cout<<"Case #"<<i<<": "<<sean<<endl;
		}
		else
			cout<<"Case #"<<i<<": NO"<<endl;	
	}
}

int compute(vector<int> candy) {
	vector<int> sean;
	vector<int> patrick;
	int max = 0;
	for(int mask=0;mask<pow(2.0,candy.size());mask++) {
		sean.clear();
		patrick.clear();
		for(int shift=0;shift<candy.size();shift++) {
			if((1<<shift) & mask) {
				sean.push_back(candy[shift]);
			}
			else {
				patrick.push_back(candy[shift]);
			}
		}
		//Now candies have been divided
		if(equalpat(sean, patrick)) {
			if(sum(patrick)!=0 && sum(sean)!=0)
				max = max>sum(sean)?max:sum(sean);			
		}		
	}
	return max;
}

bool equalpat(vector<int> sean, vector<int> patrick) {
	if(totalpat(sean) == totalpat(patrick))
		return true;
	return false;
}

int totalpat(vector<int> pile) {
	int tot = 0;
	for(int i=0;i<pile.size();i++) {
		tot = tot xor pile[i];		
	}
	return tot;
}

int sum(vector<int> pile) {
	int tot = 0;
	for(int i=0;i<pile.size();i++) {
		tot = tot + pile[i];
	}
	return tot;
}
