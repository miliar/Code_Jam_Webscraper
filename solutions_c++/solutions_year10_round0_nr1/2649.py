#include<iostream>
using namespace std;
int nn;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>nn;
	int fl,n,k;
	for (int ii=0;ii<nn;ii++){
		cin>>n>>k;
		fl=1;
		for(int i=0;i<n;i++){
			if(k%2==0){
				fl=0;break;
			}
			k/=2;
		}
		cout<<"Case #"<<ii+1<<": ";
		if(fl)
			cout<<"ON";
		else 
			cout<<"OFF";
		cout<<endl;

	}
	fclose(stdin);
	return(0);
}