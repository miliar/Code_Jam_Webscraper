#include <stdio.h>

#define	UNKNOWN		0
#define	X_WON		1
#define	O_WON		2
#define	DRAW		3

#define COMPARE(A, B, C, D)		((A)&(B)&(C)&(D))

int check_state(int board[4][4]) {
	int result = DRAW;
	
	// check rows
	for (int i = 0; i < 4; i++) {
		result = COMPARE(board[i][0], board[i][1], board[i][2], board[i][3]);
		if (result == X_WON || result == O_WON)
			return result;
	}
	// check colunms
	for (int i = 0; i < 4; i++) {
		result = COMPARE(board[0][i], board[1][i], board[2][i], board[3][i]);
		if (result == X_WON || result == O_WON)
			return result;
	}
	// check diags
	result = COMPARE(board[0][0], board[1][1], board[2][2], board[3][3]);
	if (result == X_WON || result == O_WON)
		return result;
	result = COMPARE(board[0][3], board[1][2], board[2][1], board[3][0]);
	if (result == X_WON || result == O_WON)
		return result;
	
	for (int i = 0; i < 4; i++) {
		for (int j = 0; i < 4; i++) {
			if (board[i][j] == 0x0)	// if there is empty position
				return UNKNOWN;
		}
	}
	
	return DRAW;
}

int main(int argc, char *argv[]) {
    int max_tc, tc = 1;
    char line[80];
    int board[4][4];
    
    scanf("%d", &max_tc);
 
    while(max_tc--) {
    	
        for (int i = 0; i < 4; ) {
            gets(line);
            if(line[0] == '\0')
            	continue;
            for (int j = 0; j < 4; j++) {
            	if(line[j] == '.')
            		board[i][j] = 0x0;
           		else if(line[j] == 'X')
	           		board[i][j] = 0x1;
           		else if(line[j] == 'O')
	           		board[i][j] = 0x2;
           		else if(line[j] == 'T')
	           		board[i][j] = 0x3;
            }
            i++;
        }
        
        int result = check_state(board);
        printf("Case #%d: ", tc++);
        if (result == UNKNOWN)
        	printf("Game has not completed\n");
        else if (result == X_WON)
        	printf("X won\n");
        else if (result == O_WON)
        	printf("O won\n");
        else if (result == DRAW)
        	printf("Draw\n");
    }

    return 0;
}

