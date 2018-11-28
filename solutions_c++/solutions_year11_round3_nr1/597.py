#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

//struct myclass {
//    int i;
//    bool operator() (myclass i,myclass j) { return (i.i<j.i);}
//} myobj;

#define WHITE 46
#define BLUE 35

char** origPic;
int numRows, numCols;

int processing()
{
    int impossible = 0;
    for(int r = 0; r < numRows; r++)
    {
        for(int c = 0; c < numCols; c++)
        {
            if(origPic[r][c] == BLUE)
            {
                if(c == (numCols-1)) 
                {
                    impossible = 1;
                    return impossible;
                }
                if(r == (numRows-1))
                {
                    impossible = 1;
                    return impossible;
                }
                if(origPic[r][c+1] == BLUE && origPic[r+1][c] == BLUE && origPic[r+1][c+1] == BLUE) {
                    origPic[r][c] = '/';
                    origPic[r][c+1] = 92;
                    origPic[r+1][c] = 92;
                    origPic[r+1][c+1] = '/';
                } else {
                    impossible = 1;
                    return impossible;
                }
            }
        }
    }
    
    return impossible;

}

int main ()
{
	int T, TC = 1;
    int rowsC;

    for(scanf("%d", &T); TC <= T; TC++)
    {
        scanf("%d %d", &numRows, &numCols);
        origPic = new char*[numRows];
        
	    for(rowsC = 1; rowsC <= numRows; rowsC++)
		{
            origPic[rowsC-1] = new char[51];
            scanf("%s\n", origPic[rowsC-1]);
      	}
    
    	printf("Case #%d:\n", TC);
        if(processing()) {
            printf("Impossible\n");
        } else {
            for(int r = 0; r < numRows; r++)
            {
                for(int c = 0; c < numCols; c++)
                {
                    printf("%c", origPic[r][c]);
                }
                printf("\n");
            }
        }
        delete origPic;
    }

    return 0;
}
