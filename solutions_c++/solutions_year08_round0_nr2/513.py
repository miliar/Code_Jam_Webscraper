#include <iostream>
#include <string>
#include <vector>
#include <fstream>

#define START 0
#define END 1
#define STATION 2

#define A 0
#define B 1

using namespace std;


int sortFunction( const void *a, const void *b)
{
    int intOne = ((int*)a)[START];
    int intTwo = ((int*)b)[START];
    if (intOne < intTwo)
       return -1;
    if (intOne == intTwo)
       return 0;
    return 1;
}

int main()
{
	int N,T,nA,nB;
	int c = 1;
   int count_station[2];
   	
   int trip[1001][3];
   int train[1001][3];
   int count;
   bool found;
   
   string time;
   
	unsigned long long M;
	
	freopen("B-large.in","r",stdin);
	scanf("%d",&N);

	while (N--)
	{
		// Read Input
		scanf("%d\n",&T);
		scanf("%d %d\n",&nA,&nB);		

      for (int i=0;i<nA;i++)
      {
         getline(cin, time);
         trip[i][START] =  (10*(time[0]-48) + time[1] - 48)*60 + 10*(time[3] - 48) + time[4] - 48;
         trip[i][END] =  (10*(time[6]-48) + time[7] - 48)*60 + 10*(time[9] - 48) + time[10] - 48;
         trip[i][STATION] = A;
      }
      
      for (int i=nA;i<nA+nB;i++)
      {
         getline(cin, time);
         trip[i][START] =  (10*(time[0]-48) + time[1] - 48)*60 + 10*(time[3] - 48) + time[4] - 48;
         trip[i][END] =  (10*(time[6]-48) + time[7] - 48)*60 + 10*(time[9] - 48) + time[10] - 48;
         trip[i][STATION] = B;      
      }
      
      count = 0;
      count_station[A] = 0;
      count_station[B] = 0;      
      qsort((void *)trip, nA+nB, sizeof(trip[0]), sortFunction);

      for (int i=0;i<nA+nB;i++)
      {
/*         int min = 3000;
         int i = 0;
         for (int h=0;h<nA+nB;h++)
            if ( (trip[h][START] < min) && (trip[h][STATION] != -1) )
            {
               min = trip[h][START];
               i = h;
            }
*/      
         found = false;
         for (int j=0;j<count;j++)
            if ( (train[j][START] <= trip[i][START]) && (train[j][STATION] == trip[i][STATION] ) )
            {
               found = true;
               train[j][START] = trip[i][END] + T;
               train[j][STATION] = 1 - trip[i][STATION];
               break;               
            }
            
         if (!found)
         {
            train[count][START] = trip[i][END] + T;
            train[count][STATION] = 1 - trip[i][STATION];
            count++;            
            count_station[trip[i][STATION]]++;
         }
//         trip[i][STATION] = - 1;
      }
		     
      cout<<"Case #"<<c++<<": "<<count_station[A]<<" "<<count_station[B]<<endl;
	}	
	
	return 1;
}
