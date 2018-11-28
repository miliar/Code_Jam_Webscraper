#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXT=55;
const int MAXM=2100000;

int pow10[]={1,10,100,1000,10000,100000,1000000,10000000};
struct ipt_t{
	int n,m;
	int cnt;
};

int calcnum(int num,ipt_t* li){
	if(num<10)return 0;
	int dig=0,tmp=num;
	while(tmp>0){
		tmp/=10;
		dig++;
	}
	int ret=0;
	int bs=num;
	for(int i=0;i<dig;i++){
		int l=bs%10;
		bs/=10;
		bs+=l*pow10[dig-1];
		if(bs>num){
			for(int j=0;j<ret;j++)
				if(li[j].m==bs)
					goto fin;
			li[ret].n=num;
			li[ret].m=bs;
			ret++;
		}
fin:
		1;
	}
	return ret;
};
		

int main(){
	int T;
	ipt_t ipts[MAXT];
	calcnum(104,ipts);
	cin>>T;
	for(int tt=0;tt<T;tt++){
		cin>>ipts[tt].n>>ipts[tt].m;
		ipts[tt].cnt=0;
	}
	int nr=MAXM,mr=-1;
	for(int i=0;i<T;i++){
		if(ipts[i].n<nr)nr=ipts[i].n;
		if(ipts[i].m>mr)mr=ipts[i].m;
	}
	for(int ty=nr;ty<=mr;ty++){
		ipt_t tmps[20];
		int cnt=calcnum(ty,tmps);
		for(int i=0;i<cnt;i++)
			for(int j=0;j<T;j++)
				if(ipts[j].n<=tmps[i].n && tmps[i].m<=ipts[j].m){
					ipts[j].cnt++;
//cout<<tmps[i].n<<" "<<tmps[i].m<<endl;
				}
	}
	for(int i=0;i<T;i++)
		cout<<"Case #"<<i+1<<": "<<ipts[i].cnt<<endl;
	return 0;
}
