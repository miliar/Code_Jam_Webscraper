#include <stdio.h>
#include <string.h>

#define SIZE 110
#define MAX 100000

int H, W, charFlag;
int X[4] = {-1, 0, 0, 1};
int Y[4] = {0, -1, 1, 0};

typedef struct
{
    int value;
    char sign;
}Grid;

Grid mat[SIZE][SIZE];

bool valid(int a,int b)
{
    return (a >= 0 && a < H && b >= 0 && b < W);        
}

void visit(int x, int y)
{
    int i, nx, ny, minV = MAX, dir = 0;

    for(i=0;i<4;i++)
    {
        nx = x + X[i];
        ny = y + Y[i];
        if(valid(nx, ny) && mat[x][y].value > mat[nx][ny].value)
        {
            if(minV > mat[nx][ny].value)
            {
                minV = mat[nx][ny].value;
				dir = i;
            }            
        }
    }

    // notASink
    if(minV != MAX)
    {
        nx = x + X[dir];
        ny = y + Y[dir];
        if(mat[nx][ny].sign == ' ')
		{
			visit(nx, ny);			        
		}
		mat[x][y].sign = mat[nx][ny].sign;
    }
    else
    {
        mat[x][y].sign = charFlag ++;				
    }	
}

int main()
{
    int T, i, j, kase = 1;

    //freopen("B.in","r",stdin);
	//freopen("B-small.out","w",stdout);
	//freopen("B-small.out","w",stdout);

    scanf("%d",&T);
    while(T --)
    {
        scanf("%d %d",&H, &W);

        charFlag = 'a';
        for(i=0;i<H;i++)
        {
            for(j=0;j<W;j++)
            {
                mat[i][j].sign = ' ';
                scanf("%d",&mat[i][j].value);                
            }
        }

        for(i=0;i<H;i++)
        {
            for(j=0;j<W;j++)
            {
                if(mat[i][j].sign == ' ')
                {
                    visit(i, j);                    
                }                
            }
        }

		printf("Case #%d:\n", kase ++);
        for(i=0;i<H;i++)
        {
            for(j=0;j<W;j++)
            {
				if(j)
					printf(" ");
                printf("%c",mat[i][j].sign);            
            }
            printf("\n");
        }
    }

    return 0;
}