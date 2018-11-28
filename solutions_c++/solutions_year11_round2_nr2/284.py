#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<fstream>
#include<sstream>

using namespace std;

struct st{
	int p;
	int total;
	bool operator < (const st &a)const{
		return p < a.p;
	}
};

st sts[300];
int c;
long long d;

int can(long long time){
	long long sta=(long long)sts[0].p-time;
	for(int i=0;i<c;i++){
		long long tmp=max(sta,sts[i].p-time);
		tmp+=d*((long long)sts[i].total-1LL);
		if(abs(tmp-(long long)sts[i].p)>time)return 0;
		sta=tmp+d;
	}
	return 1;
}

int main(){
	int tn;cin>>tn;
	for(int ttn=1;ttn<=tn;ttn++){
		cout<<"Case #"<<ttn<<": ";
		
		cin>>c>>d;
		d*=2LL;
		for(int i=0;i<c;i++){
			cin>>sts[i].p>>sts[i].total;
			sts[i].p*=2;
		}	
		sort(sts,sts+c);
		long long low=0LL;
		long long high=10000000000000LL;
		while(high-low>1LL){
			long long mid=(high+low)/2LL;
		//	cout<<high<<' '<<low<<' '<<mid<<' '<<can(mid)<<' '<<d<<endl;
			if(can(mid))high=mid;
			else low=mid;
		}
		//cout<<high<<' '<<low<<endl;
		double ans=0.0;
		if(can(low))ans=(double)low/2.0;
		else ans=(double)high/2.0;
		printf("%.2f\n",ans);
	}
	return 0;
}
