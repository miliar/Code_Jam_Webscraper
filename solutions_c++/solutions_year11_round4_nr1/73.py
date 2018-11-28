#include<iostream>
#include<stdio.h>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=1002;
int i,j,ca,ti,n;
double x,s,r,b,e,t,len[maxn],speed[maxn];
int main(){
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>x>>s>>r>>t>>n;
		len[0]=x;
		speed[0]=0;
		fr(i,1,n){
			cin>>b>>e>>speed[i];
			len[i]=e-b;
			len[0]-=len[i];
		}
		fr(i,0,n)
			fr(j,i+1,n)
				if(speed[i]>speed[j]){
					swap(speed[i],speed[j]);
					swap(len[i],len[j]);
				}
		double ans=0;
		fr(i,0,n){
			double tmp=double(len[i])/(speed[i]+r);
			if(tmp<=t){
				ans+=tmp;
				t-=tmp;
			}
			else{
				ans+=t+(len[i]-(speed[i]+r)*t)/(speed[i]+s);
				t=0;
			}
		}
		printf("Case #%d: %.8lf\n",ti,ans);
	}
}