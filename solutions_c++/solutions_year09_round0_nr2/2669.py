#include <iostream>
#include <cstdlib>
using namespace std;

#define MAX_SIZE		100
#define INF				10001
#define kNorth			1
#define kWest			2
#define kEast			3
#define kShouth			4

int nTest;
int testID;
char result[MAX_SIZE][MAX_SIZE];
int h, w;
int arr[MAX_SIZE][MAX_SIZE];
char current_char;
int add_x[4] = {-1,0,0,1};
int add_y[4] = {0,-1,1,0};

void input()
{
 	 scanf("%d %d", &h, &w);
 	 for(int i = 0; i < h; i++)
 	 {
	     for(int j = 0; j < w; j++)
		 {
		  		 scanf("%d", &arr[i][j]);
		 } 		 
     }
     memset(result, 0, sizeof(result));
     current_char = 'a';
}



void output()
{
 	 printf("Case #%d:\n", testID);
 	 for(int i = 0; i < h; i++)
	 {
	  		 for(int j = 0; j < w - 1; j++)
			 {
			  		 printf("%c ", result[i][j]);
			 }
			 printf("%c\n",result[i][w-1]);
	 }
}

bool checkXY(int x, int y) 
{
   if(x < 0 || x >= h || y < 0 || y >= w) return false;
   else return true;
}

char dfs(int x, int y)
{
   result[x][y] = current_char;
   int val = INF;
   int dir;
   for(int i = 0; i < 4; i++)
   {
   		   if(checkXY(x+add_x[i],y+add_y[i]))
		   {
				 if(val > arr[x+add_x[i]][y+add_y[i]])
				 {
					 val = arr[x+add_x[i]][y+add_y[i]];
					 dir = i;
				 }
		   }
   }
   if(val >= arr[x][y])
   {
	    return current_char;
   }
   if(result[x+add_x[dir]][y+add_y[dir]] != 0)
   {
		 result[x][y] = result[x+add_x[dir]][y+add_y[dir]];
		 return result[x+add_x[dir]][y+add_y[dir]];
   }
   else
   {
   	    result[x][y] = dfs(x+add_x[dir],y+add_y[dir]);
   	    return result[x][y];
   }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("WaterSheds.out","w",stdout);
    scanf("%d",&nTest);
    for(testID = 1; testID <= nTest; testID++)
    {
         input();
         for(int i = 0; i < h; i++)
	 	 {
		     for(int j = 0; j < w; j++)
			 {
			  		 if(result[i][j] == 0)
					 { 				 	     
					  	 if(current_char != dfs(i,j)) current_char--;
					  	 current_char++;
					 }
			 } 		 
	     }
         output();
    }
 return 0;
}
