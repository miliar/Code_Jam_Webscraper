#include <cstdio>
#include <iostream>
using namespace std;

#define MAX 10011

string s[MAX];

class V{
public:
	int a[27],id;
	
};
	bool operator<(const V &a, const V &b){
		int i;
		for (i=0; i<27; i++){
			if (a.a[i]<b.a[i]) return 1;
			if (a.a[i]>b.a[i]) return 0;
		}
		return 0;
	}

/*	bool operator>(const V &a, const V &b){
		int i;
		for (i=0; i<27; i++)
			if (a.a[i]>b.a[i]) return 1;
		return 0;
	}
*/

V li[MAX],now[MAX];
int mx,mxid;

void recur1(int lev, int lo, int hi, int pt){
	int i,j;
//	cout<<lev<<","<<lo<<"-"<<hi<<"="<<pt<<endl;
	if (lev==27||hi<=lo+1){
		if (pt>mx){
			mx=pt;
			mxid=now[lo].id;
		}
		else if (pt==mx && now[lo].id<mxid){
			mxid=now[lo].id;
		}
		return;
	}
	for (i=lo; i<hi; i=j){
		for (j=i; j<hi && now[i].a[lev]==now[j].a[lev]; j++);
		recur1(lev+1,i,j,pt+(now[i].a[lev]==0&&now[j].a[lev]!=0&&j<hi));
	}
}

void recur(int n){
	int i,j;
	for (i=0; i<n; i=j){
		for (j=i; j<n&&now[i].a[0]==now[j].a[0]; j++);
		recur1(1,i,j,0);
	}		
}

int main(){
	int t,u,n,m,i,j,k;
	string seq;
	cin>>t;
	for (u=0; u<t; u++){
		cin>>n>>m;
		for (i=0; i<n; i++){
			cin>>s[i];
			li[i].a[0]=s[i].length();
			for (j=0; j<26; j++){
				int b=0;
				for (k=0; s[i][k]; k++)
					b|=((s[i][k]==(j+'a'))?(1<<k):0);
				li[i].a[j+1]=b;
//				cout<<b<<"|";
			}
//			cout<<endl;
		}
		cout<<"Case #"<<(u+1)<<":";
		while(m--){
			cin>>seq;
			for (j=0; j<n; j++){
				now[j].a[0]=li[j].a[0];
				now[j].id=j;
				for (i=0; i<26; i++)
					now[j].a[i+1]=li[j].a[1+(seq[i]-'a')];
			}
//			for (i=0; i<n; i++){
	//			for (j=0; j<27; j++) cout<<now[i].a[j]<<"|";
		//		cout<<endl;
			//}
			sort(now,now+n);//,less<V>());
//			cout<<endl;
//			for (i=0; i<n; i++){
	//			for (j=0; j<27; j++) cout<<now[i].a[j]<<"|";
		//		cout<<endl;
			//}
			mx=-1;
			recur(n);
//			cout<<" "<<mx<<"="<<mxid<<","<<m;//<<s[mxi];
			cout<<" "<<s[mxid];
		}
		cout<<endl;
	}
	return 0;
}
