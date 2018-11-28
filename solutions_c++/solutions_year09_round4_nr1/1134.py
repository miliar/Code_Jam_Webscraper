#include <iostream>
#include <algorithm>
using namespace std;

char m[50][50];
int N;

/*
bool cmp(ROW a, ROW b)
{
	return ( strcmp(a.c, b.c) < 0 ) || ( strcmp(a.c, b.c) == 0 && a.rno < b.rno );
}
*/

inline bool isFixed(char row[50], int i)
{
	while ( i<N ) {
		if(row[i] == '1') return false;

		++i;
	}

	return true;
}

int main()
{
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);


	int row[50];
    int T, X, count;
	int i, j, k, t;

    scanf("%d", &T);

	X = 0;
	while (T--)
	{
		scanf("%d", &N);

		for(i=0; i<N; i++) {
			scanf("%s", m[i]);
			row[i] = i;
		}

		///
		count = 0;
		for(i=0; i<N; i++){

			if( ! isFixed(m[ row[i] ], i+1) ){

				for(j=i+1; j<N; ++j){
					if( isFixed(m[ row[j] ], i+1) ){
						count += j-i;
						
						t = row[j];
						for(k=j; k>i; --k) row[k] = row[k-1]; 
						row[i] = t;
						break;
					}
				}
			}
		}

		printf("Case #%d: %d\n", ++X, count);
	}


	fclose(stdin);
    fclose(stdout);

    return 0;
}
