#include <iostream>
#include <vector>
#define SCAN(i) scanf("%d",&i);
#define SCANS(i) scanf("%s",&i);
#define REP(i,n) for(i=0;i<n;i++)
using namespace std;

int testcase;
unsigned int long noofswitches, clicks;
int states[30]={0};
int run(){
	// OFF == 0
	// ON == 1
	int power[30]={0};
	for (int var = 0; var < noofswitches; ++var) {
		states[var]=0;
	}
	power[0]=1;
	for (unsigned long int i = 0; i < clicks; ++i) {
		for (int j = 0; j < noofswitches; ++j) {
			if(power[j]){
				if(states[j])
					states[j]=0;
				else
					states[j]=1;
			}

		}
		// update power matrix
		for (int i = 0; i < noofswitches; ++i) {
			if(power[i]&& states[i]){
				power[i+1]=1;
			}
			else
				power[i+1]=0;
		}

	}
	for (int var = 0; var < noofswitches; ++var) {
		if(power[var]&& states[var])
			continue;
		else
			return 0;
	}
	return 1;
}
int main(){
	register int i=0,j=0,temp=0;
	char str[1000]={0};
	freopen("D:\input.in","r",stdin);
	freopen("D:\output.in","w",stdout);
	SCAN(testcase);
	REP(i,testcase){
		scanf("%u",&noofswitches);
		scanf("%u",&clicks);
		temp=run();
		if(temp)
			printf("Case #%d: ON\n",i+1);
		else
			printf("Case #%d: OFF\n",i+1);
		fflush(stdout);
	}
	return 0;
}
