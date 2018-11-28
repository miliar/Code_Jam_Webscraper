#include <iostream>
#include <map>
using namespace std;
string ANS[2];

int t, n, k;

int main(){
	freopen("b.in", "r",stdin);	
	freopen("a.txt", "w",stdout);
	cin>>t;
	long long a;
	int i;
	ANS[1]="ON";
	ANS[0]="OFF";
	for(int L=1; L<=t; ++L){
		cin>>n>>k;
		a=(1<<n)-1;
		if (a>k) i=0; else {
			if ((k+1)%(a+1)==0) i=1; else i=0;
		}
		cout<<"Case #"<<L<<": "<<ANS[i]<<endl;
	//	if (L==10000) break;
	}	
}
