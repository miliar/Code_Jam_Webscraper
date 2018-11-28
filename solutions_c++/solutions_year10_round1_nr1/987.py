#include<iostream>
#include<cstdio>
#include<cstring>

int space[100][100];
char str[101];
int K,n,walk;
bool soul[2];


void getdata(){
	int i,line[100],valnum=0,k,valspaces,l,j;
	char ch;
	scanf("%d%d",&n,&K);
	for(i=0;i<n;i++){
		scanf("%s\n",str);
		//printf("%s\n",str);
		valnum=0;
		
		for(k=0;str[k]!='\0';k++){
			switch(str[k]){
				case 'R': line[valnum++]=2;
					  break;
				case 'B': line[valnum++]=1;
					  break;
			}
		}
		
		valspaces=n-valnum;

		for(k=0;k<valspaces;k++){
			space[i][k]=0;
		}

		for(l=0;l<valnum;l++){
			space[i][k+l]=line[l];
		}
	}

/*	for(i=0;i<n;i++){
		putchar('\n');
		for(j=0;j<n;j++){
			printf("%d",space[i][j]);		
		}
	}
	putchar('\n');
*/
}

void linearCheck(){
	int i,j,k,current;
	bool isequal=false;
	// horizontal check
	for(i=0;i<n;i++){
		for(j=0;j<walk;j++){
			current=space[i][j];
			isequal=true;
			for(k=0; k<K && isequal ;k++){
				isequal=(space[i][k+j]==current);
			}
			if(isequal && current>0){
				soul[current-1]=true;
			}
		}
	}

	// vertical check
	for(j=0;j<n;j++){
		for(i=0;i<walk;i++){
			current=space[i][j];
			isequal=true;
			for(k=0; k<K && isequal ;k++){
				isequal=(space[i+k][j]==current);
			}
			if(isequal && current>0){
				soul[current-1]=true;
			}
		}
	}

	//down vertical
	for(i=0;i<=n-K;i++){
		for(j=0;j<=n-K;j++){
			current=space[i][j];
			isequal=true;
			for(k=0; k<K && isequal ;k++){
				isequal=(space[i+k][j+k]==current);
			}
			if(isequal && current>0){
				soul[current-1]=true;
			}
		}	
	}

	//up vertical
	for(i=k-1;i<n;i++){
		for(j=0;j<=n-K;j++){
			current=space[i][j];
			isequal=true;
			for(k=0; k<K && isequal ;k++){
				isequal=(space[i-k][j+k]==current);
			}
			if(isequal && current>0){
				soul[current-1]=true;
			}
		}	
	}
}

void printOutput(){
	int checkNum=(int)soul[0]+2*(int)soul[1];
/*	printf("\n%d=checknum\n",checkNum);		*/
	switch(checkNum){
		case 0: printf("Neither\n"); break;
		case 1: printf("Blue\n"); break;
		case 2: printf("Red\n"); break;
		case 3: printf("Both\n"); break;
	}
}

void solve(){
	soul[0]=soul[1]=false;
	getdata();
	walk=n-K+1;

	linearCheck();
	printOutput();
}

main(){
	int testcases,i;
	scanf("%d",&testcases);
	for(i=1;i<=testcases;i++){
		printf("Case #%d: ",i);
		solve();
	}
}
