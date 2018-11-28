#include<iostream>
#include<cstdio>
using namespace std;
int ab(int a){
	if(a<0)
		return -a;
	return a;
}
int pa,pb;
int n,t;
char ti;
int ni;
int la,lb;
int tt;
int tn;
int main(){
	cin>>t;
	for(int z=1;z<=t;z++){
		cin>>n;
		la=1;
		lb=1;
		pa=0;
		pb=0;
		tn=0;
		for(int y=0;y<n;y++){
			cin>>ti>>ni;
			if(ti=='O'){
				tt=ab(ni-la);
				if(tt<=pa){
					pb++;
					tn++;
				}
				else{
					tn+=(tt-pa+1);
					pb+=tt-pa+1;
				}
				pa=0;
				la=ni;
			}
			else{
				tt=ab(ni-lb);
				if(tt<=pb){
					pa++;
					tn++;
				}
				else{
					tn+=(tt-pb+1);
					pa+=tt-pb+1;
				}
				pb=0;
				lb=ni;
			}
		}
		cout<<"Case #"<<z<<": "<<tn<<endl;
	}
	return 0;
}
