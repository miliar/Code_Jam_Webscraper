#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
bool iso[11000];vector <int> so;
int jo[5]={1,10,100,1000,10000};
int re[12];
string moji(int a){
	string ret="";string r="";int amari;
	if(a==0) return "0";if(a<0) return "-"+moji(-a);
	while(a>0){
		amari=a%10;r+=(amari+'0');a/=10;
	}
	for(int i=0;i<r.size();i++) ret+=r[r.size()-(i+1)];
	return ret;
}
int ch(int p,int a,int k){
	int b=((re[1]-re[0]*a)%p+p)%p,i;
/*	for(i=0;i<k;i++){
		if(re[i]>=p) return -1;
	}
*///	int b=((re[1]-re[0]*a)%p+p)%p,i;
	for(i=1;i<k-1;i++){
		if((re[i]*a+b)%p!=re[i+1]) return -1;
	}
	return b;
}
int main()
{
	int i,j,k,a,b,d,t;vector <string> out;
	memset(iso,false,sizeof(iso));iso[0]=true;iso[1]=true;
	for(i=2;i<10500;i++){
		if(iso[i]) continue;so.pb(i);
		for(j=2;j*i<10500;j++) iso[j*i]=true;
	}
	cin>>t;
	for(i=0;i<t;i++){
		cin>>d>>k;int s=-1,rem=-1,f=0;
		for(j=0;j<k;j++){cin>>re[j];rem>?=re[j];}
		if(k==1){out.pb("I don't know.");continue;}
		for(j=0;so[j]<=jo[d];j++){
			if(so[j]<=rem) continue;
			for(a=0;a<so[j];a++){
				int b=ch(so[j],a,k);
				if(b!=-1){
					int s2=(re[k-1]*a+b)%so[j];
					if(s==-1) s=s2;
					else if(s!=s2){
						out.pb("I don't know.");f=1;break;
					}
				}
			}
			if(f==1) break;
		}
		if(f==0) out.pb(moji(s));
	}
	for(i=0;i<t;i++) cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}
