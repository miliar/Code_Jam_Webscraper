#include <stdio.h>
// C
int main(){
	int T,T_index;
	long long unsigned int i,j,k,ans,R_times,k_cap,N_groups,g[2100],next[1100],sum,N_inters,min,xor_sum;
	long long unsigned int N_array[1100];
	
	scanf("%d",&T);
	for (T_index = 1 ;T_index <= T;T_index++){
		scanf("%llu ",&N_inters);
		ans = 0;
		min = 0;
		xor_sum =0;
		for (i=0;i<N_inters;i++){
			scanf("%llu",&N_array[i]);
			ans += N_array[i];
			if (min == 0 || min > N_array[i]){
				min = N_array[i];
			}
			xor_sum ^= N_array[i];
			//printf("xor_sum is %llu\n",xor_sum);
		}

		// all people can fit in
		if (xor_sum != 0 ){
			printf("Case #%d: NO\n",T_index);
		}else{
			printf("Case #%d: %llu\n",T_index,ans-min);
		}
	}
	return 0;
}
/*
	i=3;
	printf("i is %d\n",i);

j = 1234567890123456789;
	printf("%lld\n",j);

	j = 18446744073709551615;
	printf("%llu\n",j);

	k = 9223372036854775808;
	printf("%lld\n",k);
*/