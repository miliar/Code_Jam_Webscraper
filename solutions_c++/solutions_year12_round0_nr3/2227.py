#include<iostream>
#include<cstdio>
#include<cstdlib>

#define forloop(i,a,b) for(int i=(a);i<(b);i++)

short numbers[2000000];
int choose2[]={0,0,1,3,6,10,15,21,28};

int bigger(int a,int b){
	return (a>b)?a:b;
}

int next_num(int num,int mark){
	int temp;
	num*=10;
	temp=num/mark;
	num=num%mark+temp;
	return num;
}

int find_nums(int a,int b){
	int big=bigger(a,b);
	int small=a+b-big;

	int mark=1,temp=small;
	int likes,num_pairs=0,size=0;

	while(temp>0){
		temp/=10;
		mark*=10;
		size++;
	}

	//printf("%d %d %d\n",small,big,mark);

	for(int i=a,j=0;i<=b;i++,j++){
		numbers[j]=0;
	}

	for(int i=a,j=0;i<=b;i++,j++){
		if(! numbers[j]){
			temp=i;			
			likes=1;
			numbers[j]=1;
			for(int k=1;k<size;k++){
				temp=next_num(temp,mark);
				if(temp>i && temp<=b && !numbers[temp-a]){
					//printf("i=%d, temp=%d\n",i,temp);
					likes++;
					numbers[temp-a]=1;
				}
			}
			//printf("for %d likes:%d\n",i,likes);
			num_pairs+=choose2[likes];
		}
	}

	return num_pairs;
}

main(){
	int testcases,a,b;
	scanf("%d",&testcases);
	for(int i=1;i<=testcases;i++){
		scanf("%d%d",&a,&b);	
		printf("Case #%d: %d\n",i,find_nums(a,b));
	}
}
