#include<iostream>
 
#include<cmath>
#include<string>
#include<cstdio> 
#include<vector> 
#include<queue> 
#include<algorithm> 
#include<cstring>
#include<map>
#include<iostream>
 
using namespace std;

int d[100];
char num[100];

void solve(){
	int i,j,k;
	int ok=0;
	int n=strlen(num);
	for(i=n-2;i>=0;i--){
		int t=-1;
		for(j=i+1;j<n;j++){
			if( num[j] > num[i] ){
				
				if( t==-1 || num[j] < num[t] ){
					t=j;ok=1;
				}
			}
		}

		if( t!=-1 ){
			swap(num[i],num[t]);
			sort(num+i+1,num+n);
			cout<<num<<endl;
			return ;
		}
	}

	sort(num,num+n);
	int t=-1;
	if( n>1 && num[0]=='0' ){
		for(i=1;i<n;i++)if( num[i]!='0' )break;
		swap(num[0],num[i]);
	}
	string ans(num);
	ans = ans.substr(0,1) + "0" + ans.substr(1,n);
	cout<<ans<<endl;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,k,T;
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++){
		cin>>num;
		printf("Case #%d: ",ca);
		solve();
	}
}