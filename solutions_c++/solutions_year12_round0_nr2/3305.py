#include <iostream>
#include <cstdio>
using namespace std;

#define gout case_number++, printf("Case #%d: ", case_number), cout
#define REP(i,n) for(i=0;i<n;i++)

int case_number;
void main2()
{
	int n, s, p;
	int score[101];
	scanf ("%d %d %d", &n, &s, &p);
	
	int i, count = 0;
	REP(i,n){
		scanf ("%d", &score[i]);
		int x = score[i];
		
		if (x % 3 == 0){
			if (x/3 >= p){
				count++; continue;
			}
			
			if (s && x && (x/3+1 == p)){
				count++; s--;
			}
		}
		else if (x % 3 == 1){
			if (x/3+1 >= p) count++;
		}
		
		else{
			if (x/3+1 >= p) { count++; continue; }
			if (s && (x/3+2 == p)) { count++; s--;}
		}
	}
	
	gout << count << endl;
}

int main()
{
	int test_case, i;
	scanf ("%d", &test_case);

	REP(i,test_case) main2();
	return 0;
}
