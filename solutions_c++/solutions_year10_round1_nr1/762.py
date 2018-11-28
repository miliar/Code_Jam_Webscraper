/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2010, Online Round 1 /
/  Sub-round A, Task 'Rotate' */ 
#include <cstdio>
#include <cstring>

#define SIZE 60

//#define DEBUG

using namespace std;

struct SField
{
    unsigned int dl,dr,left,down;	//down left, down right, left, down
};

char input[SIZE][SIZE];
char matrix[SIZE][SIZE];
SField map[SIZE][SIZE];
unsigned int n;

void rotate()
{
    int i,j,temp;
    for(i=n-1;i>=0;--i)
    {
	for(j=n-1,temp=0;j>=0;--j)
	    if(input[i][j]!='.')
	    {
		matrix[n-temp-1][n-i-1]=input[i][j];
		++temp;
	    }
	while(temp<n)
	{
	    matrix[n-temp-1][n-i-1]='.';
	    ++temp;
	}
    }
    return;
}

int main()
{
    unsigned int t,k,l;
    int i,j;
    bool fred,fblue;
    scanf("%u",&t);
    for(l=1;l<=t;++l)
    {
	fred=fblue=false;
	scanf("%u%u",&n,&k);
	--k;
	for(i=0;i<n;++i)
	    scanf("%s",input[i]);
	
	rotate();
	#ifdef DEBUG
	for(i=0;i<n;++i)
	    printf("%s\n",matrix[i]);
	#endif

	for(i=n-1;i>=0;--i)
	    for(j=0;j<n;++j)	//we push everything...
		if(matrix[i][j]!='.')
		{
		    #ifdef DEBUG
		    printf("Matrix[%d][%d]: %u %u %u %u\n",i,j,map[i][j].left,map[i][j].down,map[i][j].dl,map[i][j].dr);
		    #endif
		    if(i>0 && matrix[i-1][j]==matrix[i][j])	//up
		    {
			map[i-1][j].down=map[i][j].down+1;
			if(map[i-1][j].down>=k)
			{
			    if(matrix[i][j]=='R')
				fred=true;
			    else
				fblue=true;
			}
		    }
		
		    if(j<n-1 && matrix[i][j+1]==matrix[i][j])	//right
		    {
			map[i][j+1].left=map[i][j].left+1;
			if(map[i][j+1].left>=k)
			{
			    if(matrix[i][j]=='R')
				fred=true;
			    else
				fblue=true;
			}
		    }
		    
		    if(i>0 && j>0 && matrix[i-1][j-1]==matrix[i][j])	//left up
		    {
			map[i-1][j-1].dr=map[i][j].dr+1;
			if(map[i-1][j-1].dr>=k)
			{
			    if(matrix[i][j]=='R')
				fred=true;
			    else
				fblue=true;
			}
		    }
		    
		    if(i>0 && j<n-1 && matrix[i-1][j+1]==matrix[i][j])	//right up
		    {
			map[i-1][j+1].dl=map[i][j].dl+1;
			if(map[i-1][j+1].dl>=k)
			{
			    if(matrix[i][j]=='R')
				fred=true;
			    else
				fblue=true;
			}
		    }
	    }
	    
	for(i=0;i<n;++i)
	    for(j=0;j<n;++j)
		map[i][j].dl=map[i][j].dr=map[i][j].left=map[i][j].down=matrix[i][j]=input[i][j]=NULL;
	    
	printf("Case #%u: ",l);
	if(fblue && fred)
	{
	    printf("Both\n");
	    continue;
	}
	
	if(fblue)
	{
	    printf("Blue\n");
	    continue;
	}
	
	if(fred)
	{
	    printf("Red\n");
	    continue;
	}
	
	printf("Neither\n");
	    
    }
    return 0;
}
