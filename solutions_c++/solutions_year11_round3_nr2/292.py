#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int cmp(const void * a , const void * b){
if(*(double*)a > *(double*)b)
	return -1;
	return 1;
}

double star[1000005];
int main(){
	long long int T;
	int Times;
	long long int t,i,j,k,C;
	long long int N , L;
	int count=0;
	long long int dis[1005]; 
	long long int max =0;
	scanf("%lld",&T);
	double temp;
	int build=0;
	double total=0;
	double ans =0.0;
	double total_temp=0.0;
	double temp_total=0.0;
	for(Times=1;Times<=T;Times++){
		max = -21478;
		ans =0;
		total = temp_total=0.0;
		memset(dis,0,sizeof(dis));
		memset(star,0,sizeof(star));
		scanf("%lld %lld %lld %lld",&L,&t,&N,&C);
		for(i=0;i<C;i++)
			scanf("%lld",&dis[i]);
		for(i=0;i<N;i++){
			star[i] = (double)dis[i%C];
			total +=star[i];
		}
		if((double)t*0.5 > (double)total){
			for(i=0;i<N;i++)
				ans+=(star[i]*2);
		}else{
			total_temp = t*0.5;
			ans+=(double)t;
		
			for(i=0;i<N;i++){
				if(total_temp >= (double)star[i]){
					total_temp -= (double)star[i];
				}else{
					star[i] -=total_temp;
					break;
				}
			}
			qsort(&star[i],N-i,sizeof(double),cmp);
			for(j=i;j<N;j++){
				if(L>0){
					L--;
					ans+=star[j];
				}else{
					ans+=(star[j]*2);
				}
			}
		}
		printf("Case #%d: ",Times);
		printf("%lld\n",(long long int)ans);
	}


	return 0;
}
