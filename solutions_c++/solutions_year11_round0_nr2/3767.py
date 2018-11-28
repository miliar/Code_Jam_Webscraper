#include <stdio.h>

int main(){
	int T,T_index;
	long long int i,j,k,ans,R_times,k_cap,N_groups,g[2100],next[1100],sum,C_combine,D_oppose,N_char;
	long long unsigned int part_sum[1100];
	int comb[30][30],oppo[30][30],string[1000];
	char a,b,c;
	int len,value,pre,final;
	//printf("%d\n",'A');
	scanf("%d",&T);
	for (T_index = 1 ;T_index <= T;T_index++){

		for (i=0;i<30;i++){
			for (j=0;j<30;j++){
				comb[i][j] = oppo[i][j] = -1;
			}
		}


		scanf("%llu ",&C_combine);
		//printf("c is %llu\n",C_combine);
		for (i=0;i<C_combine;i++){
			scanf("%c%c%c",&a,&b,&c);

			comb[a-65][b-65] = comb[b-65][a-65] = c-65;
		}


		scanf("%llu ",&D_oppose);
		//printf("D is %llu\n",D_oppose);
		for (i=0;i<D_oppose;i++){
			scanf("%c%c",&a,&b);
			oppo[a-65][b-65] = oppo[b-65][a-65] = 1;
		}

		len = 0;
		scanf("%llu ",&N_char);
		//printf("N is %llu\n",N_char);
		for (i=0;i<N_char;i++){
			scanf("%c",&a);
//			printf("char is %c\n",a);
			value = a-65;
//			printf("value is %d\n",value);
			if (len == 0){
				string[len] = value;
				len++;
			}else{
				pre = string[len-1];
				final = comb[value][pre];
//				printf("final is %d\n",final);
				if (final != -1){
					string[len-1] = final;
					//len--;
				}else{
//					printf("len is %d\n",len);
					for (j=len-1;j>=0;j--){
//					for (j=0;j<len;j++){
//						printf("j is %llu\n",j);
						pre = string[j];
						final = oppo[value][pre];
//						printf("oppo result is %d\n",final);
						if (final == 1){
							len = 0;
							break;  //
						}
					}
					if (j<0){
						string[len] = value;
						len++;
					}
				}
			}
//			printf("len is %d\n",len);
			for (j=0;j<len;j++){
//				printf("[%c]",string[j]+65);
			}
			fflush(NULL);
		}		

		printf("Case #%d: [",T_index);
		for (i=0;i<len;i++){
			if (i==0){
				printf("%c",string[i]+65);
			}else{
				printf(", %c",string[i]+65);
			}
		}
		printf("]\n");

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