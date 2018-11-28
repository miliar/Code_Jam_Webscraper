#include<iostream>
using namespace std;

int main(){
	int pd,pg,r,n,c=0,t;
	bool f;
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);

	cin>>r;
	while(r--){
		c++;
		cin>>n>>pd>>pg;
		cout<<"Case #"<<c<<": ";
		if(n>=100){
			f=true;
		}
		else{
			f=false;
			for(t=1;t<=n;t++){
				if((t*pd)%100==0){
					f=true;
					break;
				}
			}
		}
		if(!f||(pg==100&&pd<100)||(pg==0&&pd>0))
			cout<<"Broken"<<endl;
		else
			cout<<"Possible"<<endl;
	}
}