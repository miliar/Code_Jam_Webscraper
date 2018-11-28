#include<iostream>
using namespace std;
#define N 10

int main(){
	freopen("A.IN","r",stdin);
	freopen("A.OUT","w",stdout);
	int casenum;
	scanf("%d",&casenum);
	int casenum1=casenum;
	while(casenum--){
		int n,k;
		scanf("%d %d",&n,&k);
		n=1<<n;
		if(k%n == n-1)printf("Case #%d: ON\n",casenum1-casenum);
		else printf("Case #%d: OFF\n",casenum1-casenum);
						 
    }
    //system("pause");
    return 0;
}
