#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++){
		int n;
		int s[50];
		memset(s,0,sizeof s);
		cin>>n;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++){
				char ch;
				cin>>ch;
				if(ch=='1')
					s[i]=j;
			}
		int total=0;
		for(int i=0;i<n;i++)
			for(int j=i;j<n;j++)
				if(s[j]<=i){
					int t=s[j];
					for(int k=j;k>i;k--)
						s[k]=s[k-1];
					s[i]=t;
					total+=j-i;
					break;
				}
		cout<<"Case #"<<ii<<": "<<total<<endl;
	}
	return 0;
}