#include<iostream>
using namespace std;

int main(){
	int T,r,i,n;
	int small,sum,x,xs;
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(r=1;r<=T;r++){
		cin>>n;
		cin>>small;
		xs=sum=small;
		for(i=1;i<n;i++){
			cin>>x;
			if(x<small)
				small=x;
			sum+=x;
			xs=xs^x;
		}
		cout<<"Case #"<<r<<": ";
		if(xs==0)
			cout<<sum-small<<endl;
		else
			cout<<"NO"<<endl;
	}
}