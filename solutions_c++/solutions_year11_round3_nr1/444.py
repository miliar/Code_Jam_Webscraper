#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int nCases, iCases;
	cin >> nCases;
	
	for (iCases=1; iCases<=nCases; iCases++){
		int r, c;
		scanf("%d %d", &r, &c);
		char string[r][c+1];
		
		int i, j;
		for (i=0; i<r; i++){
			scanf("%s", string+i);
		}
		
		bool impossible = false;
		for (i=0; i<r; i++){
			for (j=0; j<c; j++){
				if (string[i][j] == '#'){
					if (i==r-1 or j==c-1){
						impossible = true;
						break;
					}
					else if (string[i+1][j]!='#' or string[i+1][j+1]!='#' or string[i][j+1]!='#'){
						impossible = true;
						break;
					}
					else {
						string[i][j] = string[i+1][j+1] = '/';
						string[i+1][j] = string[i][j+1] = '\\';
					}
				}
			}
					
			if (impossible)
				break;
		}
		
		printf("Case #%d:\n", iCases);
		if (impossible)
			printf("Impossible\n");
		else
			for (i=0; i<r; i++)
				printf("%s\n", string[i]);
	}
	
	return 0;
}
