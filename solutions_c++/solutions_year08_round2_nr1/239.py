#include <iostream>
#include <vector>

using namespace std;

const int MAXN=9;

int N,n;
int A,B,C,D;
long long x0,y0;
int M;
long long count;
int x[MAXN],y[MAXN],num[MAXN];
int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>N;
	for(int i=0;i<3;++i){
		for(int j=0;j<3;++j){
			x[i*3+j]=i;
			y[i*3+j]=j;
		}
	}
	for(int casetime=0;casetime<N;++casetime){
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		memset(num,0,sizeof(num));
		count=0;
		for(int i=0;i<n;++i){
			++num[(x0%3)*3+(y0%3)];
			x0=(A*x0+B)%M;
			y0=(C*y0+D)%M;
		}
		for(int i=0;i<MAXN;++i){
			for(int j=i;j<MAXN;++j){
				for(int k=j;k<MAXN;++k){
					if((x[i]+x[j]+x[k])%3==0 && (y[i]+y[j]+y[k])%3==0){
						if(i<j && j<k){
							count+=(long long)num[i]*num[j]*num[k];
						}else if(i==j && j<k){
							count+=(num[i]<2 ? 0 : (long long)num[i]*(num[i]-1)/2)*(long long)num[k];
						}else if(i<j && j==k){
							count+=(num[j]<2 ? 0 : (long long)num[j]*(num[j]-1)/2)*(long long)num[i];
						}else if(i==j && j==k){
							count+=num[i]<3 ? 0 :(long long)num[i]*(num[i]-1)*(num[i]-2)/6;
						}
					}
				}
			}
		}
		cout<<"Case #"<<casetime+1<<": "<<count<<endl;
	}
	return 0;
}

