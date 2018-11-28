#include <stdio.h>
#include <stdlib.h>

#include <algorithm>
#include <string>
#include <vector>

using namespace std;

#define ll long long

int abs(int n){
	return n<0?-n:n;
}
int sgn(int n){
	return n<0?-1:(n>0?1:0);
}
string decToBin(ll dec){
	string bin("");
	for(;dec>0;dec/=2){
		bin=string(1,dec%2+'0')+bin;
	}
	if(!bin.compare(""))bin=string("0");
	return bin;
}
ll binToDec(string bin){
	ll dec=0;
	for(int i=0;i<bin.length();i++){
		dec=2*dec+bin[i]-'0';
	}
	return dec;
}
ll sum(vector<ll>v){
	ll s=0;
	for(int i=0;i<v.size();i++)s+=v[i];
	return s;
}
string Padd(string a,string b){
	string sum=a;
	if(a.length()<b.length()){
		sum=b;
		b=a;
		a=sum;
	}
	for(int i=0;i<b.length();i++){
		sum[sum.length()-i-1]=(sum[sum.length()-i-1]!=b[b.length()-i-1])+'0';
	}
	return sum;
}
ll Pmath(vector<ll>yum){ //Patrick Math!!! :D
	vector<string>yum_2;
	for(int i=0;i<yum.size();i++)yum_2.push_back(decToBin(yum[i]));
	ll sum=0;
	string sum_2("0");
	for(int i=0;i<yum_2.size();i++){
		sum_2=Padd(sum_2,yum_2[i]);
	}
	sum=binToDec(sum_2);
	return sum;
}
int main(){
	int T;
	scanf("%d\n",&T);
	for(int Case=0;Case<T;Case++){
		int N;
		scanf("%d\n",&N);
		vector<ll>yummies;
		for(int i=0;i<N;i++){
			ll C;
			scanf("%lld",&C);
			yummies.push_back(C);
		}
		sort(yummies.begin(),yummies.end());
		ll MAX=-1;
		vector<ll>order(N,0);
		order[0]=1;
		while(true){
			vector<ll>S,P;
			for(int i=0;i<N;i++){
				if(order[i])P.push_back(yummies[i]);
				else S.push_back(yummies[i]);
			}
			ll Psum=Pmath(P),Ssum=Pmath(S);
			if(Psum==Ssum){
				ll s=sum(S);
				MAX=s>MAX?s:MAX;
				break;
			}
			if(sum(order)>=N)break;
			for(int i=0,carry=1;carry;i++){
				order[i]+=carry;
				carry=order[i]/2;
				order[i]%=2;
			}
		}
		
		if(MAX<0)printf("Case #%d: NO\n",Case+1);
		else printf("Case #%d: %lld\n",Case+1,MAX);
	}
	return 0;
}