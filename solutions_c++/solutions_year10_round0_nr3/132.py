#include<iostream>
#include<cstring>
using namespace std;

typedef long long LL;
int ar[1001];
LL upto[1001];
int at[1001];
bool used[1001];

int main(){
	int cas;
	cin>>cas;
	int r,k,n;
	for(int ca=1; ca<=cas; ca++){
		LL rtn=0;
		LL rtot=0;
		cin>>r>>k>>n;
		for(int i=0; i<n; ++i){
			cin>>ar[i];
		}
		int cur=0;
		bool found=false;
		int cr=0;
		memset(used, 0, sizeof(used));
		while(1){
			LL sum=0;
		//	cout<<cur<<endl;
			if(cr==r) break;
			if(used[cur]){
				found=true;
				break;
			}
			used[cur]=true;
			upto[cur]=rtot;
			at[cur]=cr;
			int kk=0;
			while(1){
				if(sum+ar[cur]>k)
					break;
				sum+=ar[cur++];
				cur%=n;
				kk++;
				if(kk==n)
					break;
			}
			rtot+=sum;
			cr++;
		}
	//	cout<<"cur: "<<cur<<" cr: "<<cr<<" rtot: "<<rtot<<endl;
	//	cout<<"at: "<<at[cur]<<" upto: "<<upto[cur]<<" "<<endl;
		if(!found){
			cout<<"Case #"<<ca<<": "<<rtot<<endl;
			continue;
		}
		rtn= (((r-at[cur])/(cr-at[cur]))-1)*(rtot-upto[cur])+rtot;
		//cout<<rtn<<endl;
		r-=at[cur];
		r%=(cr-at[cur]);
		cr=0;
		while(1){
			LL sum=0;
			if(cr==r) break;
			int kk=0;
			while(1){
				if(sum+ar[cur]>k)
					break;
				sum+=ar[cur++];
				cur%=n;
				kk++;
				if(kk==n)
					break;
			}
			rtn+=sum;
			cr++;
		}
		cout<<"Case #"<<ca<<": "<<rtn<<endl;
	}
}
