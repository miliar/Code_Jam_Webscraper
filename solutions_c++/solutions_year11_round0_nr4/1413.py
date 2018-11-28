#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>

using namespace std;

vector<double> savf, savg;

void count_cycles(vector<int> & a, vector<int> & res){
	for(int i=0; i<a.size(); i++){
		if(a[i]!=i+1 && a[i]>0){
			int tmp=a[i];
			int len=1;
			a[i]=-1;
			while(a[tmp-1]!=-1){
				len++;
				int newtmp = a[tmp-1];
				a[tmp-1]=-1;
				tmp=newtmp;
			}
			res.push_back(len);
		}
	}
}

double f(int n){
	if(n<2) return 0;
	double res = savf[n];
	if(res>0) return res;
	
	res=1;
	for(int i=2; i<=n-1; i++) res+=f(i);
	res*=2.0/(double(n-1));
	savf[n]=res;
	return res;
}

int main(){
	int T, N, C;
	cin>>T;
	for(int i=0; i<T; i++){
		cin>>N;
		vector<int> arr(0);
		for(int j=0; j<N; j++){
			cin>>C;
			arr.push_back(C);
		}
		double res=0;

		vector<int> cyc_len(0); cyc_len.clear(); cyc_len.resize(0);
		count_cycles(arr, cyc_len);
		
		savf.clear(); savf.resize(1002, -1);
		savg.clear(); savg.resize(1002, -1);
		for(int j=0; j<cyc_len.size(); j++){
			res+=f(cyc_len[j]);
		}
		
		cout<<"Case #"<<i+1<<": ";
			cout<<res<<"\n";
	}
	
}
