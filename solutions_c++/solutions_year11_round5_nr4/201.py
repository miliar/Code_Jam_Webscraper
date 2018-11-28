#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<complex>
#define EPS (1e-10)
#define PI (3.141592653589793238)
#define MP make_pair
typedef long long ll;
using namespace std;

bool check(ll x){
	ll i,j;
	ll up=(ll)sqrt((double)x)+100,down=0,mid;
	while(1){
		mid=(up+down)/2;
		if(mid*mid>x){
			up=mid;
		}else{
			down=mid;
		}
		if(up-down<=1)break;
	}
	for(i=mid-2;i<=mid+2;i++){
		if(i*i==x)return true;
	}
	return false;
}

int main(void){
	int T;
	scanf("%d",&T);
	for(int casenum=1;casenum<=T;casenum++){
		ll i,j,k;
		char ch[100];
		scanf("%s",ch);
		string st=string(ch);
		ll n=0;
		ll moto=0;
		for(i=0;i<st.size();i++){
			if(st[st.size()-1-i]=='?')n++;
			if(st[st.size()-1-i]=='1')moto+=(1LL<<i);
		}
		//printf("%lld\n",moto);
		bool owata=false;
		string nst=st;
		for(i=0;i<(1LL<<n);i++){
			ll now=0;
			ll num=moto;
			for(j=0;j<st.size();j++){
				if(st[st.size()-1-j]=='?'){
					if((i&(1LL<<now))!=0){
						num+=(1LL<<j);
						nst[st.size()-1-j]='1';
					}else{
						nst[st.size()-1-j]='0';
					}
					now++;
				}
			}
			if(check(num)){
				printf("Case #%d: %s\n",casenum,nst.c_str());
				owata=true;
				break;
			}
			/*double d=sqrt((double)num);
			ll dd=(ll)d;
			for(j=dd-100;j<=dd+100;j++){
				if(j*j==num){
					printf("Case #%d: %s\n",casenum,nst.c_str());
					owata=true;
					break;
				}
			}
			if(owata)break;*/
		}
	}
	return 0;
}
