#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

int iswinning(int A, int B){
	if(A<B)
		swap(A, B);
	if(A>=2*B)
		return 1;
	return !iswinning(B, A-B);
}

long long wincount(int A, int B){
	long long res=0;
	int f1=0, f2=1, f3=1, f4=2;
	while(f3<=A && f4<=B){
		for(int x=1; x*f3<=A && x*f4<=B; x++){
			res+=1+min(f1==0 ? 100000000 : (A-f3*x)/f1, (B-f4*x)/f2);
		}
		int f5=f4+f3, f6=f5+f4;
		f1=f3; f2=f4; f3=f5; f4=f6;
	}
	return res;
}

long long wincount2(int A, int B){
	return wincount(A, B)+wincount(B, A);
}

long long eval(){
	int A1, A2, B1, B2;
	cin>>A1>>A2>>B1>>B2;
	return wincount2(A2, B2)-wincount2(A1-1, B2)-wincount2(A2, B1-1)+wincount2(A1-1, B1-1);
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		cout<<eval()<<endl;
	}
	return 0;
}
