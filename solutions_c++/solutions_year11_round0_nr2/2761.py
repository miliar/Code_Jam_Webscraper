#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#define O 0
#define B 1
using namespace std;
char opp[256],itemlist[100],bpair[36][3];
int ilp,pp,op;
int main(int argc, char **argv)
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	int C,D,N,ilp;
	
	cin>>t;
	for(int i=1;i<=t;i++){
		ilp=pp=op=0;
		memset(opp,0,256);
		bpair[0][0]=0;
		cin>>C;
//		cout<<"Base Pair"<<endl;
		for(pp=0;pp<C;pp++){
			cin>>bpair[pp][0]>>bpair[pp][1]>>bpair[pp][2];
			//cout<<bpair[pp][0]<<bpair[pp][1]<<" "<<bpair[pp][2]<<endl;
		}
		cin>>D;
	//	cout<<"Opposite Pair"<<endl;
		for(op=0;op<D;op++){
			char ch1,ch2;
			cin>>ch1>>ch2;
			opp[ch1]=ch2;
			opp[ch2]=ch1;
			//cout<<ch1<<ch2<<endl;
		}
		cin>>N;
		ilp=0;
		char ch,pch;
		cin>>itemlist[ilp++];
		int replaced=false;
		int n=1;
		while(n<N){
			cin>>ch;n++;
			pch=itemlist[ilp-1];
			replaced=false;
			for(int j=0;j<pp;j++){
				if( (bpair[j][0]==pch&&bpair[j][1]==ch) || (bpair[j][0]==ch&&bpair[j][1]==pch) ){
					itemlist[ilp-1]=bpair[j][2];
					//cout<<"Replacing...with"<<bpair[j][2]<<endl;
					replaced=true;
					break;
				}
			}
			if(replaced)continue;
//			cout<<"Opp.."<<opp[ch]<<endl;
			int opposite=false;
			for(int k=0;k<ilp;k++){
				if(itemlist[k]==opp[ch]){
					opposite=true;
					break;
				}
			}
			if(opposite){
				ilp=0;
//				cout<<n<<ch<<".."<<opp[ch]<<endl;
				if(n<N){
					cin>>itemlist[ilp++];n++;
					continue;
				}
				else
					break;
			} 
			itemlist[ilp++]=ch;
		}
		cout<<"Case #"<<i<<": ";
		cout<<'[';
		int ii;
		if(ilp>0){
			for(ii=0;ii<ilp-1;ii++)
				cout<<itemlist[ii]<<", ";
			cout<<itemlist[ii];
		}
		cout<<']'<<endl;
	}
	return 0;
}