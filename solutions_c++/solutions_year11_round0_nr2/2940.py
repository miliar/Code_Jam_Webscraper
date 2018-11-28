#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <string.h>

using namespace std;

int A[30][30];
int B[30];
int M[30];

vector <int> R;

int main()
{
	int TEST;
	scanf("%d",&TEST);
	string sstr;

	int sze, idx, i, a, b, old;

	int test = 1;

	while(TEST--) {
		scanf("%d",&a);
		memset(A,0,sizeof(A));
		memset(B,0,sizeof(B));
		memset(M,0,sizeof(M));
		R.clear();

		for(i=1;i<=a;i++) {
			sstr.clear();
			cin >> sstr;
			A[sstr[0]-'A'+1][sstr[1]-'A'+1] = sstr[2] - 'A' + 1;
			A[sstr[1]-'A'+1][sstr[0]-'A'+1] = sstr[2] - 'A' + 1;
		}

		scanf("%d",&b);
		
		for(i=1;i<=b;i++) {
			sstr.clear();
			cin >> sstr;
			B[sstr[0]-'A'+1] = sstr[1]-'A'+1;
			B[sstr[1]-'A'+1] = sstr[0]-'A'+1;
		}
		scanf("%d",&sze);
		sstr.clear();
		cin >> sstr;
		
		M[sstr[0]-'A'+1]++;
		old = sstr[0] -'A'+1;
		R.push_back(sstr[0]-'A'+1);
		idx = 1;
		
		int val;
		for(i = 1; i < sze;) {
			val = sstr[i] - 'A' +1;
			if(A[old][val]) {
				M[old]--;
				R[idx-1] = A[old][val];
				old = R[idx-1];
				i++;
				continue;
			}else if(M[B[val]]) {
				memset(M,0,sizeof(M));
				R.clear();
		
				idx = 0;
				i = i+1;
				if(i < sze) {
					old = sstr[i] - 'A' + 1;
					M[old]++;
					R.push_back(old);
					idx = 1;
					i++;
				}
				continue;
				
			}else {
			
				M[val]++;
				R.push_back(val);
				old = R[idx];
				idx++;
			}
			i++;
		}

		sze = R.size();
		
		printf("Case #%d: [",test);

		for(i=0;i<=sze-2;i++)
			printf("%c, ",(char)(R[i]+'A'-1));
	
		if(sze-1 >= 0)
		printf("%c",(char)(R[sze-1]+'A'-1));

		printf("]\n");
		test++;
	}
	return 0;
}
