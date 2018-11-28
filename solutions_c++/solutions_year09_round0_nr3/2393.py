#include<stdio.h>
#include<string.h>

char str[512];
int l;
int nr_sol;
char search[]="welcome to code jam"; //19


void fatreaba(int i, int k);


int main() {

	//freopen("welcome.in", "r", stdin);
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	
	int N;
	
	scanf("%d", &N);
	
	gets(str);
	
	//N teste
	for(int i=1; i<=N; i++) {
		
		gets(str);
		
		l=strlen(str)-1;
		nr_sol=0;
		
		fatreaba(0,0);
		
		printf("Case #%d: %.4d\n",i,nr_sol);
	}


	return 0;
}


void add_sol() {
	nr_sol++;
	nr_sol%=1000;
}


void fatreaba(int i, int k) {

	if(k==19) {
		add_sol();
		//return;
	}
	
	for(i; i<=l; i++)
		if(str[i]==search[k])
			fatreaba(i+1,k+1);

}
