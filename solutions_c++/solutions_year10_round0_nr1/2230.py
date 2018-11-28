#include <iostream>

#define TASK "a"
#define SMALL "small-attemption" 
#define NUM "0"
#define LARGE "large"

int test;
int numtest;
int n,k;
int ans;

void readinput(){

	scanf("%i %i",&n,&k);


}

void writeoutput(){
	printf("Case #%i: ",numtest);

	if (ans){
		printf("ON\n");
	}else{
		printf("OFF\n");
	}
}

void solve(){
	int power = 1<<n;
	k%=power;
	if (k==power-1) ans = 1;
	else ans = 0;
}

int main(void){
	//freopen(TASK"-"SMALL""NUM".in","r",stdin);
	//freopen(TASK"-"SMALL""NUM".out","w",stdout);
	freopen(TASK"-"LARGE".in","r",stdin);
	freopen(TASK"-"LARGE".out","w",stdout);
	scanf("%i\n",&test);
	for (int q=0;q<test;q++){
        numtest=q+1;
		readinput();
		solve();
		writeoutput();
	}

	return 0;
}
