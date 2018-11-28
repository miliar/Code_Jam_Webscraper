#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<string>
#include<cstring>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<bool> vb;

struct span{
	int bits;
	int sum;
	bool operator<( const span & n ) const {
		return this->sum < n.sum;   // for example
	}
};

int maxbitpow, n;

vector<span> sets;
span curr;
int nums[500 + 5];
#define For(i,a,b) for(i=a;i<b;i++)


void printset(int bits){
	int index = 0;
	int currbit;
	while(bits > 0){
		currbit = bits % 2;
		bits/=2;
		if(currbit == 1)
			cout<<nums[index]<<" ";
		index++;
	}
	cout<<endl;
}

void explore(int sum, int index, int bits){
	if(index < n){
		explore(sum, index + 1, bits);
		sum += nums[index];
		bits += pow(2, index);
		curr.bits = bits;
		curr.sum = sum;
		sets.push_back(curr);
		//cout<<"Bits: "<<bits<<endl<<"Set: ";
		//printset(bits);
		explore(sum, index + 1, bits);
	}	
}

int main ()
{
	int t;
	cin>>t;
	span currsum, prevsum;
	for(int i=1; i<=t;i++){
		sets.clear();
		cin>>n;
		for(int j = 0; j < n; j++){
			cin>>nums[j];
		}
		//maxbitpow = pow(2, n);
		/*
		for(int j = 0; j < n; j++){
			sum = 0;
			curr.p1 = j;
			for(int k = j; k < n; k++){
				sum += nums[k];
				curr.p2 = k;
				curr.sum = sum;
				spans.push_back(curr);
			}
		}*/
		explore(0, 0, 0);
		sort(sets.begin(), sets.end());
		currsum.sum = -1;
		cout<<"Case #"<<i<<":\n";
		while(!sets.empty()){
			prevsum = currsum;
			currsum = sets.back();
			if(prevsum.sum == currsum.sum){
				//cout<<prevsum.bits<<endl;
				printset(prevsum.bits);
				//cout<<currsum.bits<<endl;
				printset(currsum.bits);
				break;
			}
			sets.pop_back();
		}
		if(sets.empty())
			cout<<"Impossible\n";
	}
	return 0;
}
