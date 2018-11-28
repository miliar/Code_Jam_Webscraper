#include<stdio.h>

char table[100][100];
char intable[100][100];
char tmp[100][100];
int t;
int m,n,k;
int column[100];

void rotate1(){// left
	int i,j;
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			tmp[n-j-1][i]=intable[i][j];
		}
	}
	for(i=0;i<n;i++)for(j=0;j<m;j++)table[i][j]='.';
	for(i=0;i<n;i++)column[i]=m-1;
	for(i=0;i<m;i++){ // column
		for(j=n-1;j>=0;j--){
			if(tmp[j][i]!='.'){
				table[column[i]][i]=tmp[j][i];
				column[i]--;
			}
		}
	}
	/*
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			printf("%c",table[i][j]);
		}
		printf("\n");
	}
	*/
}

void rotate2(){// right
	int i,j;
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			tmp[j][m-i-1]=intable[i][j];
		}
	}
	for(i=0;i<n;i++)for(j=0;j<m;j++)table[i][j]='.';
	for(i=0;i<n;i++)column[i]=m-1;
	for(i=0;i<m;i++){ // column
		for(j=n-1;j>=0;j--){
			if(tmp[j][i]!='.'){
				table[column[i]][i]=tmp[j][i];
				column[i]--;
			}
		}
	}
	/*
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			printf("%c",table[i][j]);
		}
		printf("\n");
	}
	*/
}

void subcheck(int result[],int i,int j){
	int goal;
	// horizontal
	goal=1;
	for(int ktmp=0;ktmp<k;ktmp++){
		if(j+ktmp>=n){goal=0;break;}
		if(table[i][j]!=table[i][j+ktmp])goal=0;
	}
	if(goal==1){
		if(table[i][j]=='R')result[0]=1;
		else if(table[i][j]=='B')result[1]=1;
	}

	goal=1;
	for(int ktmp=0;ktmp<k;ktmp++){
		if(i+ktmp>=n){goal=0;break;}
		if(table[i][j]!=table[i+ktmp][j])goal=0;
	}
	if(goal==1){
		if(table[i][j]=='R')result[0]=1;
		else if(table[i][j]=='B')result[1]=1;
	}
	// diagonal
	goal=1;
	for(int ktmp=0;ktmp<k;ktmp++){
		if(j+ktmp>=n){goal=0;break;}
		if(i+ktmp>=n){goal=0;break;}
		if(table[i][j]!=table[i+ktmp][j+ktmp])goal=0;
	}
	if(goal==1){
		if(table[i][j]=='R')result[0]=1;
		else if(table[i][j]=='B')result[1]=1;
	}

	goal=1;
	for(int ktmp=0;ktmp<k;ktmp++){
		if(j-ktmp<0){goal=0;break;}
		if(i+ktmp>=n){goal=0;break;}
		if(table[i][j]!=table[i+ktmp][j-ktmp])goal=0;
	}
	if(goal==1){
		if(table[i][j]=='R')result[0]=1;
		else if(table[i][j]=='B')result[1]=1;
	}
}

void check(int result[]){
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			subcheck(result,i,j);
		}
	}
}
int main(void){
	int i,j;
	int run;
	int result[2];
	scanf("%d\n",&t);
	for(run=0;run<t;run++){
		scanf("%d %d\n",&m,&k);
		n=m;
		// printf("%d %d %d\n",m,n,k);
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				scanf(" %c",&(intable[i][j]));
				table[i][j]=intable[i][j];
			}
		}
		/*
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				printf("%c",table[i][j]);
			}
			printf("\n");
		}
		*/
		result[0]=0;result[1]=0;
		// rotate1();
		check(result);
		rotate2();
		check(result);
		if(result[0]==1&&result[1]==1)printf("Case #%d: Both\n",run+1);
		else if(result[0]==1)printf("Case #%d: Red\n",run+1);
		else if(result[1]==1)printf("Case #%d: Blue\n",run+1);
		else printf("Case #%d: Neither\n",run+1);
	}
	return 0;
}
