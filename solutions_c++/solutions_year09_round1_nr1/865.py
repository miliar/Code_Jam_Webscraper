#include <stdio.h>
#include <string>
FILE * in = fopen("input.txt","r");
FILE * out = fopen("output.txt","w");
char inp_char[3000];
int check_base[21];


bool check_happy(int num, int bases){
	int dd[3000]={0,};
	int sum=0;


	while(1){
		
		sum=0;
		while(num>0){
			sum+=(num%bases)*(num%bases);
			num/=bases;
		}

		if (sum==1)return true;
		if (dd[sum])break;
		dd[sum]=1;
		num=sum;
	}
	return false;
}
int main(){
	int i,j,k,T,tmp,cnt,len,flag;


	fscanf(in,"%d\n",&T);

	for(k=1;k<=T;k++){
		fgets(inp_char,255,in);
		
		for(i=2;i<=10;i++)check_base[i]=0;
		
		cnt=0;
		len=strlen(inp_char);
		do{
			sscanf(inp_char+cnt,"%d",&tmp);
			if (tmp>=10)cnt+=3;
			else cnt+=2;
			check_base[tmp]=1;
		}while(cnt<len);

		for(i=2;i<=100000;i++){
			flag=0;
			for(j=2;j<=10;j++){
				if (check_base[j]){
					if (!check_happy(i,j)){
						flag=1;
						break;
					}
				}
			}
			if (flag==0){
				fprintf(out,"Case #%d: %d\n",k,i);
				break;
			}
		}
		
		
	}
	return 0;
}