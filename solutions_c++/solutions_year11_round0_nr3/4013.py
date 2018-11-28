#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

#define rep(i,n) for(int i=0;i<int(n);i++)

#define mp(a,b) make_pair(a,b)
#define f first
#define s second

int item[20];
int n;
int hav[20]={0};
int ans;

void saiki(int dep){
	if(dep==n){
		
		int a=0,b=0;
		int cont=0;
		
		rep(i,dep){
			if(hav[i]==1){
				cont++;
				a^=item[i];
			}else{
				b^=item[i];
			}
		}
		
		int sum=0;
		if(a==b && cont!=0 && n-cont!=0){
			rep(i,dep){
				if(hav[i]==1){
					sum+=item[i];
				}
			}
			ans = max(ans,sum);
		}
		
		return;
	}
	
	hav[dep]=1;
	saiki(dep+1);
	hav[dep]=2;
	saiki(dep+1);
	
	hav[dep]=0;
}

int main(){
	int T;
	cin>>T;
	
	rep(p,T){
		cin>>n;
		
		rep(i,20)item[i]=0;
		
		rep(i,n){
			cin>>item[i];
		}
		
		printf("Case #%d: ",p+1);
		
		ans=-1;
		saiki(0);
		
		if(ans==-1){
			puts("NO");
		}else{
			printf("%d\n",ans);	
		}
	}
}