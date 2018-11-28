#include<iostream>
using namespace std;
int main(){
//	freopen("l.in", "r", stdin);
//	freopen("l.out", "w", stdout);
	int T;
	cin>>T;
	int t=1;
	while(t<=T){
		int res=0;
		int nb;
		cin>>nb;
		char b[100];
		int p[100]={0};
		int O[100]={0};
		int B[100]={0};
		int po=0;
		int pb=0;
		int i;
		int fo=0;
		int fb=0;
		int time;
		for(i=0; i<nb; i++){
			cin>>b[i];
			cin>>p[i];
			if(b[i]=='O'){
				O[po++]=p[i];
//				B[i]=0;
			}
			else{
				B[pb++]=p[i];
//				O[i]=0;
			}
		}
//		O[0]=B[0]=1;
		po=pb=1;
		i=0;
		while(i<nb){
			time=0;
			if(b[i]=='O'){
				time = abs(p[i]-po)+1;
				po = p[i];
				fo++;
				if(B[fb]-pb>time){//2,
					pb=pb+time;
				}
				else if(pb-B[fb]>time){
					pb=pb-time;
				}
				else{
					pb = B[fb];
				}
			}
			else{
				time = abs(p[i]-pb)+1;
				pb = p[i];
				fb++;
				if(O[fo]-po>time){//2,
					po=po+time;
				}
				else if(po-O[fo]>time){
					po=po-time;
				}
				else{
					po = O[fo];
				}
			}
			res+=time;
			i++;
		}
		cout<<"Case #"<<t<<": "<<res<<endl;
		t++;
	}
}