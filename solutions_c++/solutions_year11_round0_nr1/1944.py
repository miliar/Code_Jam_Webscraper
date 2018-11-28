#include<iostream>
#define ABS(a) ((a)>0?(a):(-(a)))
#define NONEG(a) ((a)<0?0:(a))
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int ca=1; ca<=t ; ++ca){
		int n, O=1, B=1, l;
		char c;
		cin>>n;
		int tb=0,to=0, tr;
		int rtn = 0;
		for(int i=0; i<n; ++i){
			cin>>c>>l;
			if(c=='O'){
				tr = ABS(O-l);
				O=l;
				rtn += NONEG(tr-to)+1;
				tb += NONEG(tr-to)+1;
				to=0;
			} else {
				tr = ABS(B-l);
				B=l;
				rtn += NONEG(tr-tb)+1;
				to += NONEG(tr-tb)+1;
				tb=0;
			}
		}
		cout<<"Case #"<<ca<<": "<<rtn<<endl;
	}
}