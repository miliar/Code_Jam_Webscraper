//google code jam 2011 round 1A
#include <stdio.h>

const char answerStr[2][10]={"Broken", "Possible"};

long long gcd(long long a, long long b){
	long long t;
	if (a<b) {
		t=a;
		a=b;
		b=t;
	}
	while (b>0){
		t=a%b;
		a=b;
		b=t;
	}
	return a;
}

int main(){
	int caseIndex, caseNum;
	long long n;
	int pd,pg;

	scanf("%d", &caseNum);
	for (caseIndex=1; caseIndex<=caseNum; caseIndex++){
		scanf("%lld%d%d", &n, &pd, &pg);

		bool hasAnswer=false;
		int val=100/gcd(100, pd);
		if (n>=val){
			if (pd==100 || (pd<100 && pg<100))
				hasAnswer=true;
		}
		if ((pd==0 && pg>0) || (pd>0 && pg==0)) hasAnswer=false;
		if (pd==0 && pg==0) hasAnswer=true;

		printf("Case #%d: %s\r\n", caseIndex, answerStr[hasAnswer]);
	}
	return 0;
}