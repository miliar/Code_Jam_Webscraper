#include<iostream>
using namespace std;

long long in[2000],cyc[2000],use[2000],wei[2000],cwei[2000];

int main(){
	freopen("pc.out","w",stdout);
	freopen("C-large.in","r",stdin);
	long long t,r,k,n,tt,i,j,sum(0),con,cw,pre(0),cycle,ans;
	scanf("%I64d",&t);
	for(tt=1 ; tt<=t ; tt++){
		memset(in,0,sizeof(in));
		memset(cyc,0,sizeof(cyc));
		memset(use,0,sizeof(use));
		memset(wei,0,sizeof(wei));
		memset(cwei,0,sizeof(cwei));
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		for(i=0 ; i<n ; i++){
			scanf("%I64d",&in[i]);
			in[i+n]=in[i];
		}
		for(i=0 ; i<n ; i++){
			sum=0;
			for(j=i ; j<i+n ; j++){
				if(sum+in[j]>k) break;
				sum+=in[j];
			}
			if(j>=n) j-=n;
			cyc[i]=j;
			wei[i]=sum;
		}
		con=1;
		i=0;
		while(1){
			use[i]=con++;
			if(!use[cyc[i]]){
				cwei[cyc[i]]=cwei[i]+wei[i];
			}
			else break;
			i=cyc[i];
		}
	//	cout << i << ' ' << cyc[i] << endl;
		cw=cwei[i]-cwei[cyc[i]]+wei[i];
		cycle=use[i]-use[cyc[i]]+1;
		pre=use[cyc[i]]-1;

		ans=0;
		if(r>pre){
			r-=pre;
			ans+=cwei[cyc[i]];
			ans+=cw*(r/cycle);
			r%=cycle;
			for(i=cyc[i] ; r>0 ; i=cyc[i],r--) ans+=wei[i];
		}
		else{
			j=0;
			for(i=0 ; i<r ; i++){
				ans+=wei[j];
				j=cyc[j];
			}
		}
	//	cout << endl;
	//	for(i=0 ; i<n ; i++) cout << wei[i] << ' ';
	//	cout << endl;
		cout << "Case #" << tt << ": " << ans << endl;
	}
}
