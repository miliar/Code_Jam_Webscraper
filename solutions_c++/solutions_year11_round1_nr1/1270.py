#include<iostream>
using namespace std;
long n,pd,pg,T,TT,dd;
char s[2][11]={"Broken","Possible"};
inline long gcd(long x,long y){
	static long z;
	while(z=x%y) x=y,y=z;
	return y;
}
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	cin>>T;
	for(TT=1;TT<=T;++TT){
		cin>>n>>pd>>pg;
		cout<<"Case #"<<TT<<": ";
		dd=gcd(pd,100);
		if(n<(100/dd))
			cout<<s[0]<<endl;
		else
			switch (pg){
				case 0:cout<<s[pd==0]<<endl;break;
				case 100:cout<<s[pd==100]<<endl;break;
				default:cout<<s[1]<<endl;
				}
		}
	cin>>T;
	return 0;
}
