#include<iostream>
#include<vector>
#include<cmath>
#include<sstream>
#define for(a,b,c) for(int a=b; a<c; a++)
using namespace std;

typedef vector<int>vi;
typedef vector<char>vc;

string solve(vi& in){
	ostringstream out;
	int m=in[0];
	int sum=m;
	for(i,1,in.size()){
		sum+=in[i];
		if(m>in[i])
			m=in[i];
	}
	out<<(sum-m);

	return out.str();
}

int main(){
	int t;
	istream& in = cin;
//istringstream in("2 5 1 2 3 4 5 3 3 5 6");
	in>>t;
	for(i,0,t){
		int n;
		in>>n;
		
		vi v(n);
		
		int sum=0;
		for(j,0,n){
			in>>v[j];
			sum ^= v[j];
		}
		
		cout<<"Case #"<<(i+1)<<": ";
		if(sum)
			cout<<"NO";
		else cout<<solve(v);
		
		cout<<endl;
	}
	system("PAUSE >void.out");
	return 0;
}
