#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

void eval(){
	int N, sum=0, x=0, m=1e9;
	scanf("%d", &N);
	while(N--){
		int C;
		scanf("%d", &C);
		sum+=C;
		x^=C;
		m=min(m, C);
	}
	if(x!=0)
		cout<<"NO"<<endl;
	else
		cout<<(sum-m)<<endl;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
