#include<cstdio>

using namespace std;

int T;
char W[4][4];

int Xw[4],Xh[4],p1,p2;

void test(){
	printf("Case #%d: ",++T);
	for(int i=0;i<4;i++)
		scanf("%s",W[i]);
	
	char A='X';
	int C=0;
	for(int i=0;i<4;i++){
		Xw[i]=0;
		Xh[i]=0;
	}
	p1=0;
	p2=0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(W[i][j]==A || W[i][j]=='T'){
				Xw[i]++;
				Xh[j]++;
				if(i==j) p1++;
				if(i+j==3) p2++;
				if(Xw[i]==4 || Xh[j]==4 || p1==4 || p2==4) C=1;
			}
	if(C){
		printf("%c won\n",A);
		return;
	}
	
	
	A='O';
	for(int i=0;i<4;i++){
		Xw[i]=0;
		Xh[i]=0;
	}
	p1=0;
	p2=0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(W[i][j]==A || W[i][j]=='T'){
				Xw[i]++;
				Xh[j]++;
				if(i==j) p1++;
				if(i+j==3) p2++;
				if(Xw[i]==4 || Xh[j]==4 || p1==4 || p2==4) C=1;
			}
	if(C){
		printf("%c won\n",A);
		return;
	}
	
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(W[i][j]=='.'){
				printf("Game has not completed\n");
				return;
			}
	printf("Draw\n");
	return;
}

int main(){
	int n;
	scanf("%d",&n);
	while(n--) test();
	return 0;
}
