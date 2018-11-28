#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

#define llong long long
const int N = 1005;
int n,step[N];
llong pro[N],d[N],R,K;


int find_next(int s,llong &val){
	int i,j,k;
	llong sum = 0;
	while(1){
		if(sum+d[s]>K)break;
		sum += d[s];
		s = (s+1)%n;
	}
	val = sum;
	return s;
}
int main(){
	//freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	int i,j,k,t,nc = 0;
	cin>>t;
	while(t--){
		cin>>R>>K>>n;
		llong sum = 0;
		for(i = 0;i<n;i++){
			cin>>d[i];
			sum += d[i];
		}
		llong ans = 0;
		if(sum<=K){
			ans = sum*R;
		}else{
			memset(pro,0,sizeof(pro));
			memset(step,-1,sizeof(step));
			int st = 0;
			k = 0;
			llong now = 0;
			step[0] = st++;
			while(1){
				llong tmp;
				i = find_next(k,tmp);
				now += tmp;
				if(i==k){
					ans = now;
					break;
				}else if(step[i]==-1){
					step[i] = st++;
					pro[i] = now;
					if(step[i]==R){
						ans = now;
						break;
					}
				}else {
					int a = step[i];
					int b = st-a;
					ans = pro[i]+(now-pro[i])*((R-a)/b);
					int c = R-a-(R-a)/b*b+step[i];
					for(j = 0;j<n;j++){
						if(step[j]==c)break;
					}
					ans += pro[j]-pro[i];
					break;
				}
				k = i;
			}
		}
		cout<<"Case #"<<++nc<<": "<<ans<<endl;
	}
	return 0;
}