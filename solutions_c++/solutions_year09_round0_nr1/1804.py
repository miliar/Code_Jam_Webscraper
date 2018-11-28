#include<iostream>
#include<cstring>
using namespace std;

int n,l,d;

void fill(unsigned long *x){
	int t=(d/32)*4;
	memset(x,255,t);
	memset(x+t,0,160-t);
	x[t]=(1<<(d%32))-1;
}

int main(){
	unsigned long mask[10][26][160];
	cin>>l>>d>>n;
	memset(mask,0,sizeof mask);
	for(int i=0;i<d;i++)
		for(int j=0;j<l;j++){
			char ch;
			cin>>ch;
			mask[j][ch-'a'][i/32]|=1<<(i%32);
		}
	for(int i=0;i<n;i++){
		unsigned long ans[160];
		fill(ans);
		for(int j=0;j<l;j++){
			char ch;
			cin>>ch;
			if(ch=='('){
				unsigned long cur[160];
				memset(cur,0,sizeof cur);
				while(cin>>ch,ch!=')'){
					int t=ch-'a';
					for(int k=0;k<160;k++)
						cur[k]|=mask[j][t][k];
				}
				for(int k=0;k<160;k++)
					ans[k]&=cur[k];
			}
			else{
				int t=ch-'a';
				for(int k=0;k<160;k++)
					ans[k]&=mask[j][t][k];
			}
		}
		int s=0;
		for(int k=0;k<160;k++){
			ans[k]=((ans[k]&0xaaaaaaaa)>>1)+(ans[k]&0x55555555);
			ans[k]=((ans[k]&0xcccccccc)>>2)+(ans[k]&0x33333333);
			ans[k]=((ans[k]&0xf0f0f0f0)>>4)+(ans[k]&0x0f0f0f0f);
		}
		for(int k=0;k<160;k+=20){
			for(int l=1;l<20;l++)
				ans[k]+=ans[k+l];
			ans[k]=((ans[k]&0xff00ff00)>>8)+(ans[k]&0xff00ff);
			s+=((ans[k]&0xffff0000)>>16)+(ans[k]&0xffff);
		}
		cout<<"Case #"<<i+1<<": "<<s<<endl;
	}
	return 0;
}
