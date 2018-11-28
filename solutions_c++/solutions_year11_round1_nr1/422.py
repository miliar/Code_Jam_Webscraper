#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
long long n,d,g;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("2.txt","w",stdout);
	int t,pd,pg;
	cin>>t;
	for(int tt=0;tt<t;++tt){
		cin>>n>>pd>>pg;
		if((pg==0&&pd>0)||(pg==100&&pd<100)){
			cout<<"Case #"<<tt+1<<": Broken"<<endl;
			continue ;
		}
		int tmp=0;
		for(int i=1;i<=100;++i)
			if(i*pd%100==0){
				tmp=i;
				break;
			}
		if(tmp<=n)
			cout<<"Case #"<<tt+1<<": Possible"<<endl;
		else cout<<"Case #"<<tt+1<<": Broken"<<endl;
	}
	return 0;
}
