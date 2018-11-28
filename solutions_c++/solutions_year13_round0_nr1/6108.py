#include <iostream>
#include <stdio.h>
using namespace std;

int main (){
    int TT;
    int tcase = 1;
    cin>>TT;
    while (TT--) {
        char arr[4][4];
        bool finished = true;
        for (int i=0;i<4;i++)   for (int j=0;j<4;j++)  {
            cin>>arr[i][j];
            if (arr[i][j]=='.') finished = false;
        }
        
        //Check for rows
        bool done = false;
        for (int i=0;i<4;i++) {
            char beg;
            if (arr[i][0]=='T')   beg=arr[i][1];
            else                  beg=arr[i][0];
			if (beg=='.')	continue;
            int j=1;
            for (j=1;j<4;j++) if (!(arr[i][j]==beg || arr[i][j]=='T')) break;
            if (j==4) done = true;
            if (done) {
                if (beg=='X'){
                    printf ("Case #%d: X won\n", tcase++);
					break;
                }
                else if (beg=='O'){
                    printf ("Case #%d: O won\n", tcase++);
					break;
                }
				else
					done = false;
            }
        }
        if (done){
            continue;
        }
        
        //Check for cols
        for (int j=0;j<4;j++) {
            char beg;
            if (arr[0][j]=='T')   beg=arr[1][j];
            else                  beg=arr[0][j];
			if (beg=='.')	continue;
            int i=1;
            for (i=1;i<4;i++) if (!(arr[i][j]==beg || arr[i][j]=='T')) break;
            if  (i==4)   done = true;
            if (done) {
                if (beg=='X'){
                    printf ("Case #%d: X won\n", tcase++);
					break;
                }
                else if (beg=='O'){
                    printf ("Case #%d: O won\n", tcase++);
					break;
                }
				else
					done = false;
            }
        }
        if (done){
            continue;
        }
        
        //Check for forward diagonal
        char beg;
        if (arr[0][0]=='T') beg  = arr[1][1];
        else                beg  = arr[0][0];
        
		if (beg!='.')	{
			int i;
			for (i=1;i<4;i++)   if (!(arr[i][i]==beg || arr[i][i]=='T')) break;
			if (i==4){
				if (beg=='X'){
						printf ("Case #%d: X won\n", tcase++);
						continue;
					}
					else if (beg=='O'){
						printf ("Case #%d: O won\n", tcase++);
						continue;
					}
					else
						done = false;
			}
		}
        
        //Check for backward diagonal
        if (arr[0][3]=='T') beg = arr[1][2];
        else                beg = arr[0][3];
        
		if (beg!='.')	{
			int i;
			for (i=1;i<4;i++)   if (!(arr[i][3-i]==beg || arr[i][3-i]=='T')) break;
			if (i==4){
				if (beg=='X'){
						printf ("Case #%d: X won\n", tcase++);
						continue;
					}
					else if (beg=='O'){
						printf ("Case #%d: O won\n", tcase++);
						continue;
					}
					else
						done = false;
			}
        }
        if (finished){
            printf ("Case #%d: Draw\n", tcase++);
        }
        else {
            printf ("Case #%d: Game has not completed\n", tcase++);
        }
    }
    return 0;
}