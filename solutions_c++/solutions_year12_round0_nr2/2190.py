#include<iostream>
#include<cstdio>
#include<cstdlib>

#define forloop(i,a,b) for(int i=(a);i<(b);i++)
char *in_buffer = NULL;
int array[150];

int create_array(){
	int value=0,flag=0,is_digit,index=0;	
	char ch;
	for(int i=0;in_buffer[i]!=0;i++){
		ch = in_buffer[i];		
		is_digit=isdigit(ch);
		if(flag){
			if(is_digit){
				value=value*10+ch-'0';
			}else{
				array[index++]=value;
				flag=0;
			}				
		}else{
			if(is_digit){
				value=ch-'0';
				flag=1;
			}
		}
	}

	return index;
}

int run(){
	size_t len = 0;
    ssize_t read;
	read = getline(&in_buffer, &len, stdin);
	int size=create_array();		
/****************************************************
	forloop(i,0,size){
		printf("%d ",array[i]);
	}
	printf(": %d\n",size);
/*****************************************************/

	int n=array[0],s=array[1],p=array[2];
	int bench1=3*p-2,bench2=(3*p-4);
	int num_bench1=0,num_bench2=0;
	
	bench1=(bench1 < 0)?0:bench1;
	bench2=(bench2 < 0)?0:bench2;

	for(int i=3;i<size;i++){
		if(array[i] < p){

		}
		else if(array[i]>=bench1){
			num_bench1++;
		}else if(array[i]>=bench2){
			num_bench2++;
		}
	}
	
//	printf("%d %d %d\n",n,s,p);
//	printf("%d %d\n",bench1,bench2);
//	printf("%d %d\n",num_bench1,num_bench2);
	num_bench1+=(s<num_bench2)?s:num_bench2;
	return num_bench1;
}


main(){
	int testcases,i;
	scanf("%d\n",&testcases);
	for(int i=1;i<=testcases;i++){
		printf("Case #%d: %d\n",i,run());
	}
	free(in_buffer);
}
