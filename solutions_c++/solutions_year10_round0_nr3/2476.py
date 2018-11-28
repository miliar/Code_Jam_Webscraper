#include<iostream>
#include<cstdio>

using namespace std;

__int64 sum,ans;
int T,R,K,N;
int p[1000+2];

int main(){
	freopen("C-small-attempt0.in","r", stdin);
	freopen("C-small-attempt0.out","w", stdout);

	int cas=0;
	cin>>T;
	while(cas++<T){
		
		sum=0;
		cin>>R>>K>>N;
		for(int i=0; i<N; i++){
			cin>>p[i];
		}

		int ind=0,nd=0;
		for(int i=0; i<R; i++){
			ans=0; nd=0;
			while(nd<N&&ans+p[ind]<=K){
				ans+=p[ind];
				ind=(ind+1)%N;
				nd++;
			}
			sum+=ans;
		}

		cout<<"Case #"<<cas<<": ";
		printf("%I64d\n", sum);
	}
	return 0;
}