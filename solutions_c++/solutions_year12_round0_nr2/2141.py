#include<iostream>
#include<string>

using namespace std;

int t,n,s,p,tmp,res;

int rect(int x) {
	if(x>=0)
		return x;
	return 0;	
}

int main() 
{
	cin>>t;
	for(int i=0;i<t;i++) {
		cin>>n>>s>>p;
		res=0;
		for(int j=0;j<n;j++) {
			cin>>tmp;
			if(tmp>= (rect(p)+rect(p-1)+rect(p-1))) {
				res++;
			} else if((tmp== (rect(p)+rect(p-2)+rect(p-2)) || tmp==(rect(p)+rect(p-1)+rect(p-2))) && s>0) {
				res++;
				s--;
			}
		}
		cout<<"Case #"<<i+1<<": "<<res<<"\n";
	}
	return 0;
}
