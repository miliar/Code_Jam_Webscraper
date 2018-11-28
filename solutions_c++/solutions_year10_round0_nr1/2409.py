#include <iostream>

using namespace std;

#define MAXSNAPPER 10

int main() {
	printf("Program start.\n");
//	if(freopen("A-small-practice.in", "r", stdin)){
//		//freopen("A-small-practice.out","w",stdout);
//	}else{
//		printf("file not found.\n");
//		return 0;
//	}

	if(freopen("A-large-practice.in", "r", stdin)){
		freopen("A-large-practice.out","w",stdout);
	}else{
		printf("file not found.\n");
		return 0;
	}

	int TestCases;
	scanf("%d", &TestCases);

	for(int caseID=1;caseID<=TestCases;caseID++){
		printf("Case #%d: ", caseID);
		int n,k;
		scanf("%d", &n);
		scanf("%d", &k);
		unsigned long s[30];
		s[0] = 1;
		for(int i=1;i<30;i++)
			s[i]=s[i-1]*2+1;
		for(int i=0;i<30;i++)
			s[i]+=1;

		if(k%s[n-1]==s[n-1]-1)
			printf("ON");
		else
			printf("OFF");

		printf("\n");
	}

	fclose(stdin);
	fclose(stdout);
	printf("Program finish.\n");
	return 0;
}
