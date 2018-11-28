#include <stdio.h>
#include <string>
FILE * in = fopen("input.txt","r");
FILE * out = fopen("output.txt","w");
int L,D,N;
int arr[30][5001],arr_cnt[30];
char dic[5001][256];
char str[256];

char str2[30][30];
int str2_cnt[30];
int main(){
	int i,j,k,len,ind,flag,l;
	fscanf(in,"%d %d %d",&L,&D,&N);
	for(k=0;k<D;k++){
		fscanf(in,"%s",dic[k]);
	}
	for(k=0;k<N;k++){
		
		fscanf(in,"%s",&str);
		len=strlen(str);
		ind=0;
		flag=0;
		
		for(i=0;i<L;i++){
			str2_cnt[i]=0;
		}
		
		for(i=0;i<len;i++){
			if (str[i]=='('){
				flag=1;				
			}	
			else if (str[i]==')'){
				flag=0;
			}
			else{
				str2[ind][str2_cnt[ind]++]=str[i];
			}
			if (flag==0)ind++;
		}

		for(i=0;i<D;i++){
			arr[0][i]=i;
		}
		for (i=0;i<=L;i++)
		{
			arr_cnt[i]=0;
		}
		arr_cnt[0]=D;

		for(i=0;i<L;i++){
			for(l=0;l<arr_cnt[i];l++){
				for(j=0;j<str2_cnt[i];j++){
					if (str2[i][j]==dic[arr[i][l]][i]){
						arr[i+1][arr_cnt[i+1]++]=arr[i][l];
						break;
					}
				}
			}
		}
		fprintf(out,"Case #%d: %d\n",k+1,arr_cnt[L]);
	}
	return 0;
}