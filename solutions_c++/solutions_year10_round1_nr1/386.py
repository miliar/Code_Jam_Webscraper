#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int t, n, kk;
char board[100][100];

int done(char cc, int kk)
{
    int i, j, k;
    
    for (i = 0; i < n; i++)
    	for (j = 0; j < n; j++) {
    	    if (board[i][j] != cc)
    	    	continue;
    	    if (j + kk <= n) {
    	        for (k = 0; k < kk; k++)
    	        	if (board[i][j + k] != cc)
    	        		break;
  	        	if (k == kk)
  	        		return (1);
    	    }
    	    if (i + kk <= n) {
    	        for (k = 0; k < kk; k++)
    	        	if (board[i + k][j] != cc)
    	        		break;
  	        	if (k == kk)
  	        		return (1);
    	    }
    	    if (i - kk + 1 >= 0 && j + kk <= n) {
    	        for (k = 0; k < kk; k++)
    	        	if (board[i - k][j + k] != cc)
    	        		break;
  	        	if (k == kk)
  	        		return (1);
    	    }    
    	    if (i + kk <= n && j + kk <= n) {
    	        for (k = 0; k < kk; k++)
    	        	if (board[i + k][j + k] != cc)
    	        		break;
  	        	if (k == kk)
  	        		return (1);
    	    }    
    	}    
   	return (0);
}    

int main()
{
    int i, j, k, l;
    
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d %d", &n, &kk);
        for (j = 0; j < n; j++) {
        	scanf("%s", board[j]);
        	k = n - 1;
        	for (l = n - 1; l >= 0; l--)
        		if (board[j][l] != '.')
        			board[j][k--] = board[j][l];
 			while (k >= 0)
 				board[j][k--] = '.';
        }
       	int red = done('R', kk);
       	int blue = done('B', kk);
       	if (red && blue)
       		printf("Case #%d: Both\n", i + 1);
   		else if (red)
   			printf("Case #%d: Red\n", i + 1);
 		else if (blue)
 			printf("Case #%d: Blue\n", i + 1);
		else
			printf("Case #%d: Neither\n", i + 1);
    }    
    
    return (0);
}
    
