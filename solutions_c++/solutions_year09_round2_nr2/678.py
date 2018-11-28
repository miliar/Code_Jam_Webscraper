#define MD(x) if (0) {x;}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <string>
void MyAssert(int p){ while (!p) printf("error\n"); };
#define O1(S,A,n) MD(cout<<S<<":";for (int i=0; i<n; i++)cout<<A[i]<<" ";cout<<endl;)
#define O2(S,A,n) MD(cout<<S<<"\n";for (int i=0; i<n; i++){for (int j=0; j<n; j++)cout<<A[i][j]<<" ";cout<<endl;})
using namespace std;

void change(vector<int> &A){
	if (A[0]==0){
		int k = A.size()-1;
		for (int i=0; i<A.size(); i++)
			if (A[i]>0 && A[k]>A[i])
				k = i;
		int t = A[k];
		A.erase(A.begin()+k);
		A.insert(A.begin(),t);
	}
}


int main(){
	string s;
	vector<int>A;
	int tc;
	cin>>tc;
	for (int ti=1; ti<=tc; ti++){
		cout<<"Case #"<<ti<<": ";
		cin>>s;
		A.clear();
		for (int i=0; i<s.size(); i++)
			A.push_back(s[i]-'0');
		O1("A",A,A.size());
		if (!next_permutation(A.begin(),A.end())){
			MD(cout<<"insert!\n";)
			sort(A.begin(),A.end());
			change(A);
			A.insert(A.begin()+1,0);
		}
		for (int i=0; i<A.size(); i++)
			cout<<A[i];
		cout<<endl;
	}
	return 0;
}
