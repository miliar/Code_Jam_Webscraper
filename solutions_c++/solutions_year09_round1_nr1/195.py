#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>
using namespace std;
int digs[20];

bool convert(long long num, int base){
	for(int i=0; i<20; i++) digs[i]=0;
	int c=0;
	while(num>0){
		digs[c] = num%base;
		num/=base; c++;
	}
}

bool test(long long num, int base){
	vector<int> vis(1000, 0);
	while(num!=1){
		
		if(num<1000 && vis[num]){
			return false;
		}else if(num<1000){
			vis[num]=1;
		}
		convert(num, base);
		long long res =0 ;
		for(int i=0; i<20; i++){
			res+=digs[i]*digs[i];
		}
		num=res;
	}
	return true;
}



int main(){
	int N;
	cin>>N;
	vector<string> lines(N);
	getline(cin, lines[0]);
	for(int i=0; i<N; i++){
		//cin>>wrds[i]; 
		getline(cin, lines[i]);
		//cout<<lines[i]<<"\n";
		string s = lines[i];
		int res=0;
		stringstream ss(s);
		int b;
		vector<int> bases(0);
		while(ss>>b){
			bases.push_back(b);
		//	cout<<b<<" ";
		}
		int n = bases.size();
		vector<int> digits(20);
		bool happy = false; 
		int num = 2;
		while(!happy){
			happy=true;
			for(int i=n-1; i>=0; i--){
				//cout<<num<<" "<<bases[i]<<"\n";
				bool ttt = test(num, bases[i]);
				if(!ttt){
					happy = false; break;
				}
			}
			num++;
		}
		
		cout<<"Case #"<<i+1<<": " <<num-1<<"\n";
	}
	
}
