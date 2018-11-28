#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>

#define REP(i,n) for(int i=0; i<n; ++i)
#define REPE(i,n) for(int i=0; i<=n; ++i)

using namespace std;

int gcd(int x, int y)
{
	if(y==0) 
		return (x); 
	else 
		return gcd(y,x%y);
}

char data[100][100];

int main ()
{
	int caseNum;
	scanf("%d", &caseNum);
	for (int caseId=1; caseId<=caseNum; caseId++){
		int row, col;
		scanf("%d %d", &row, &col);
		REP(r, row) {
			scanf("%s", data[r]);
		}
		bool isOK=true;
		REP(r, row) {
			REP(c, col) {
				if (data[r][c]!='#') {
					continue;
				}
				else {
					if ( data[r][c+1]!='#' ||
						data[r+1][c]!='#' ||
						data[r+1][c+1]!='#' || r+1>=row || c+1 >= col
						) 
					{
						isOK=false;
						break;					
					}
					data[r][c]='/';
					data[r][c+1]='\\';
					data[r+1][c]='\\';
					data[r+1][c+1]='/';
				}
			}
			if (!isOK){
				break;
			}
		}

		if (!isOK)
		{
			printf("Case #%d:\nImpossible\n", caseId);
		}
		else {
			printf("Case #%d:\n", caseId);
			REP(r, row){
				printf("%s\n", data[r]);
			}
		}	
	}
	return 0;
}