#include<iostream>
using namespace std;

int t,T,A1,A2,B1,B2,a,b,c,i,j,ans;
int crnt;

int main() {
	cin>>T;
	for(t=1;t<=T;t++) {
		cin>>A1>>A2>>B1>>B2;
		ans=0;
		for(i=A1;i<=A2;i++) {
			for(j=B1;j<=B2;j++) {
				if(i==j) continue;
				a=i; b=j;
				if(b>a) {
					c=a;
					a=b; b=c;
				}
				crnt=0;
				while(1) {
					if(a/b>1) {
						if(crnt==0) ans++;
						break;
					}
					if(a%b==0&&crnt==0) {
						ans++;
						break;
					}
					c=a; a=b; b=c%b;
					crnt=1-crnt;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}
