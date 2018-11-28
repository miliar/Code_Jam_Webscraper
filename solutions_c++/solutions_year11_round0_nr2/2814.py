#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <string.h>
using namespace std;

int A[30][30],B[30],M[30];

vector <int> R;

int main()
{
	int TestT;
	scanf("%d",&TestT);
	string sstr;
	int sze,Tpoint, i, a , b , p_old, test = 1;
	while(TestT--) {
		scanf("%d",&a);
		memset(A,0,sizeof(A));memset(B,0,sizeof(B));memset(M,0,sizeof(M));
		R.clear();
		for(i=1;i<=a;i++) {
			sstr.clear();cin >> sstr;
			A[sstr[0]-'A'+1][sstr[1]-'A'+1] = sstr[2] - 'A' + 1;A[sstr[1]-'A'+1][sstr[0]-'A'+1] = sstr[2] - 'A' + 1;
		}

		scanf("%d",&b);
		
		for(i=1;i<=b;i++) {
			sstr.clear();cin >> sstr;
			B[sstr[0]-'A'+1] = sstr[1]-'A'+1;B[sstr[1]-'A'+1] = sstr[0]-'A'+1;
		}
		scanf("%d",&sze);sstr.clear();cin >> sstr;
		
		M[sstr[0]-'A'+1]++;
		p_old = sstr[0] -'A'+1;
		R.push_back(sstr[0]-'A'+1);
		Tpoint = 1;
		
		int val;
		
		for(i = 1; i < sze;) {
			val = sstr[i] - 'A' +1;
			
			if(A[p_old][val]) {
				M[p_old]--;R[Tpoint-1] = A[p_old][val];
				p_old = R[Tpoint-1];
				i++;
				continue;
			}
			else if(M[B[val]]) {
				memset(M,0,sizeof(M));
				R.clear();
		
				Tpoint = 0;
				i = i+1;
				if(i < sze) {
					p_old = sstr[i] - 'A' + 1;
					M[p_old]++;
					R.push_back(p_old);
					Tpoint = 1;
					i++;
				}
				continue;
				
			}
			else {
			
				M[val]++;
				R.push_back(val);
				p_old = R[Tpoint];
				Tpoint++;
			}
			i++;
		}
		sze = R.size();
		
		printf("Case #%d: [",test);
		for(i=0;i<=sze-2;i++) {
			printf("%c, ",(char)(R[i]+'A'-1));
		}
		if(sze-1 >= 0)
		printf("%c",(char)(R[sze-1]+'A'-1));

		printf("]\n");
		test++;
	}

		
	return 0;
}
