#include<iostream>
#include<set>
#include<map>
using namespace std;
int a,b;
typedef pair<int,int> P;
set<P> st;
bool check(int x,int p,int t){
	int f=x/(p*10),g=x%(p*10);
	t/=p;
	int n=f+g*t;
	if(b<n)
		return 0;
	if(n>x){
		st.insert(P(n,x));
		return 1;
	}else
		return 0;
}
int main(){
	int t;
	cin>>t;
	int now=1;
	while(t--){
		st.clear();
		cin>>a>>b;
		for(int i=a;i<=b;i++){
			int p=10;
			int temp=1;
			for(;i/temp;temp*=10);
			temp/=10;
			for(int j=0;(i/p);j++,p*=10){
				check(i,p/10,temp);
			}
		}
		cout<<"Case #"<<now++<<": ";
		cout<<st.size()<<endl;
	}
	return 0;
}