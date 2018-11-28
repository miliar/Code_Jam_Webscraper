#include<stdio.h>
#include<algorithm>
#include<vector>
#include<time.h>
#include<math.h>

#define MAX 2000000
using namespace std;
vector<int> R[MAX+1];
int test_cases, case_n;
int A, B;


int main(){
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);

	/*scanf("%d\n",&test_cases);

	for(case_n = 1; case_n <= test_cases; case_n++){
		scanf("%d%d",&A,&B);
		
		int tmp = A;
		for(dig=0;tmp>0; tmp/=10) dig++;
		p10dig = (int)pow(10.,(double)(dig-1));

		int res = 0;
		for(int i=A; i<=B; i++){
			for(int j=i+1; j<=B; j++) res += is_true(i,j);
		}
		printf("Case #%d: %d\n",case_n,res);
	}*/

	int i,j,ipow10=10;
	for(i=10; i<=MAX; i++){
		if(i == ipow10 * 10) ipow10 *= 10;
		int tmp = i;
		for(;;){
			tmp = (tmp/10) + (tmp%10) * ipow10;
			if(tmp == i) break;
			if(tmp > i && tmp <= MAX) R[i].push_back(tmp);
		}
		sort(R[i].begin(), R[i].end());
	}
	scanf("%d\n",&test_cases);

	for(case_n = 1; case_n <= test_cases; case_n++){
		scanf("%d%d",&A,&B);
		unsigned long long res = 0;
		for(i=A; i<=B; i++){
			res += upper_bound(R[i].begin(), R[i].end(), B) - R[i].begin();
		}
		printf("Case #%d: %llu\n",case_n,res);
	}
	return 0;
}