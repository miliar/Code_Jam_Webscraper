

#include<iostream>

using namespace std;

int main() {
	int T, z;
	cin>>T;
	z=T;
	int N, S, p, x, num;
	while(T) {
		cin>>N;
		cin>>S;
		cin>>p;
		num=0;
		//if(p==0) {cout<<"Case #"<<z-T+1<<": "<<N<<" "<<S<<" "<<p<<endl; T--; continue;}
		while(N) {
			cin>>x;
			if(p==0) num++;
			else if(p==1) { if(x>=1) num++;}
			else {
				if(x >= (p+(2*(p-1)))) num++;
				else if( x >= (2*(p-1)+(p-2))) {
					if(S>0) {
						num++;
						S--;
					}
				}
			}
			N--;
		}
		cout<<"Case #"<<z-T+1<<": "<<num<<endl;
		T--;
	}
	return 0;
}
