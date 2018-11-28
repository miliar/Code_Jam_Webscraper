#include <iostream>
#include <vector>
#include <cstdlib>


using namespace std;

#define Wires 1000

int main() {
//	printf("Program start.\n");
//	if(freopen("A-small-practice.in", "r", stdin)){
//		freopen("A-small-practice.out","w",stdout);
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
		int N;
		scanf("%d", &N);
		int A[Wires][2];

		for(int i=0;i<N;i++){
			int H1,H2;
			scanf("%d", &H1);
			scanf("%d", &H2);
			A[i][0] = H1;
			A[i][1] = H2;
		}
		int ic=0;
		for(int i=0;i<N;i++){
			for(int j=i;j<N;j++){
				if((A[i][0]-A[j][0])>0){
					if((A[i][1]-A[j][1])<0)
						ic++;
				}else{
					if((A[i][1]-A[j][1])>0)
						ic++;
				}
			}
		}

		printf("%d", ic);
		printf("\n");
	}

	fclose(stdin);
	fclose(stdout);
	printf("Program finish.\n");
	return 0;
}
