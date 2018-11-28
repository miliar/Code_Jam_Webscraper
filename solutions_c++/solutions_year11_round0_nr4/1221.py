#include <string>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
vector<int> factorize(int *A, int n){
	vector<int> sol;
	int *used=new int[n+1];
	memset(used, 0, sizeof(int)*(n+1));
	for(int c=1;c<=n;++c)if(!used[c]){
		int current=c;
		int len=0;
		while(!used[current]){
			++len;
			used[current]=1;
			current=A[current];
		}
		sol.push_back(len);
	}
	return sol;
}

int main(int argc, char *argv[]){
	int A[1001];
	int numCases;
	cin>>numCases;
	for(int c=0;c<numCases;++c){
		int n;
		cin>>n;
		for(int i=1;i<=n;++i){
			cin>>A[i];
		}
		vector<int> v=factorize(A,n);
		double sol=0;
		for(unsigned i=0;i<v.size();++i)if(v[i]>1){
			sol+=v[i];
		}
		cout<<"Case #"<<c+1<<": "<<sol<<endl;
	}
	return 0;
}
