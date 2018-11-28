#include<stdio.h>
#include<algorithm>
#include<vector>
#include<time.h>
#include<math.h>

int test_cases;
int case_n;
char A[300];                //?        ?
char key[] = "yhesocvxduiglbkrztnwjpfmaq"; // qz

int main(){
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);

	scanf("%d\n",&test_cases);
	for(case_n = 1; case_n <= test_cases; case_n++){
		gets(A);
		printf("Case #%d: ",case_n);
		for(int i=-1; A[++i];) putchar(A[i] == ' '?' ':key[A[i]-'a']);
		puts("");
	}
	return 0;
}