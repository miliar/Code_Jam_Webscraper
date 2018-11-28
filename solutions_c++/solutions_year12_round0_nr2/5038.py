#include <iostream>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		int n;
		int s;
		int p;
		cin>>n;
		cin>>s;
		cin>>p;
		int t[n];
		int c=0;
		for(int j=0;j<n;j++)
			cin>>t[j];
		for(int k=0;k<n;k++)
			if((p*3-2)<=t[k]){
				c++;
				t[k]=0;
			}	
		int l=0;
		while(s&&l<n){
			if((p*3-4)<=t[l]&&(p*3-4)>0){
				c++;	
				s--;
			}
			l++;
		}
		cout<<"Case #"<<i+1<<": "<<c<<endl;
	}
	return 0;
}	
