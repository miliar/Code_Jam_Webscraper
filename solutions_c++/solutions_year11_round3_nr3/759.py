#include<iostream>
using namespace std;
bool har(int a,int b){
	return (a%b==0)||(b%a==0);
}
int main(){
	int t,n,l,h;
	int freq[10000];
	cin>>t;
	for(int x=1;x<=t;++x){
		cin>>n>>l>>h;
		for(int i=0;i<n;++i)
			cin>>freq[i];
		for(int i=l;i<=h;++i){
			int j;
			for(j=0;j<n;++j){
				if(!har(i,freq[j]))
					break;
			}
			
			if(j==n){
				printf("Case #%d: %d\n",x,i);
				goto end;
			}
			
		}
		printf("Case #%d: NO\n",x);
		end:
		1==1;
	}
}
