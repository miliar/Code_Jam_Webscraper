#include<iostream>
#define abs(x) ((x)<0?-(x):(x))
using namespace std;
long t,n,tt;
long d1,d2,t1,t2,nt,ff;
char c;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>t;
	for(tt=1;tt<=t;++tt){
		cin>>n,d1=d2=1,nt=t1=t2=0;
		while(n--){
			cin>>c>>ff;
			if(c=='O'){
				if(abs(ff-d1)<=nt-t1)
					d1=ff,++nt,t1=nt;
				else
					nt+=abs(ff-d1)-(nt-t1)+1,d1=ff,t1=nt;
				}
			else{
				if(abs(ff-d2)<=nt-t2)
					d2=ff,++nt,t2=nt;
				else
					nt+=abs(ff-d2)-(nt-t2)+1,d2=ff,t2=nt;
				}
			}
		cout<<"Case #"<<tt<<": "<<nt<<endl;
		}
	cin>>t;
	return 0;
}
