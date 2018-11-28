#define DIGITS 7
#include <stdio.h>
#include <hash_map.h>
#include <string.h>
#include <stdlib.h>
using namespace std;

struct TrainTime
{
   int departure;
   int arrival; 
};

struct TrainAvailability
{
   int time;
   int availability;
};

//int compare_function(const void*,const void* );

int compare_function1(const void* a, const void* b)
{
    TrainTime* x = (TrainTime *)a;
    TrainTime* y = (TrainTime *)b;
    return (*x).departure - (*y).departure;    
}

int compare_function2(const void* a,const void* b)
{
   TrainAvailability* x = (TrainAvailability *)a;
    TrainAvailability* y = (TrainAvailability *)b;
    if((*x).time == (*y).time)
        if((*x).availability > (*y).availability)
            return -1;
        else
            return 1;
    return (*x).time - (*y).time;  
}

int main(void)
{
freopen("E:\\B-small-attempt1.in" ,"r",stdin);
freopen("E:\\TTOutput.txt","w",stdout);
int n;
scanf("%d",&n);
//printf("%d\n",n);
//hash_map <const char *, int> searchEngines;
for(int i = 0; i< n ; i++)
{
     //searchEngines.clear();
     int m;
     scanf("%d",&m);
     //printf("%d\n",m);
     //char ch;
     //scanf("%c",ch);
     int a,b;
     scanf("%d",&a);
     scanf("%d",&b);
     //printf("%d,%d\n",a,b);
     struct TrainTime* stationA = new TrainTime[a];
     struct TrainTime* stationB = new TrainTime[b];
     char temp1[100];
     gets(temp1);
     for(int j =0; j< a; j++) 
     {
      char tempString[100];            
      //scanf("%[^\r^\n]",temp);
      gets(tempString);
      char* temp = tempString;
      //printf("%s\n", temp);
      stationA[j].departure = 0;
      stationA[j].arrival = 0;
      stationA[j].departure += 1000 * (*(temp++)- '0');
      stationA[j].departure += 100 * (*(temp++)- '0');
      temp++;
      stationA[j].departure += 10 * (*(temp++)- '0');
      stationA[j].departure += (*(temp++)- '0');
      temp++;
      stationA[j].arrival += 1000 * (*(temp++)- '0');
      stationA[j].arrival += 100 * (*(temp++)- '0');
      temp++;
      stationA[j].arrival += 10 * (*(temp++)- '0');
      stationA[j].arrival +=  (*(temp++)- '0');
      //printf("%s -> %d %d\n",tempString,stationA[j].departure, stationA[j].arrival);      
     }
     
     for(int j =0; j< b; j++) 
     {
      char tempString[100];            
      //scanf("%[^\r^\n]",temp);
      gets(tempString);
      char* temp = tempString;
       stationB[j].departure = 0;
      stationB[j].arrival = 0;
      stationB[j].departure += 1000 * (*(temp++)- '0');
      stationB[j].departure += 100 * (*(temp++)- '0');
      temp++;
      stationB[j].departure += 10 * (*(temp++)- '0');
      stationB[j].departure += (*(temp++)- '0');
      temp++;
      stationB[j].arrival += 1000 * (*(temp++)- '0');
      stationB[j].arrival += 100 * (*(temp++)- '0');
      temp++;
      stationB[j].arrival += 10 * (*(temp++)- '0');
      stationB[j].arrival +=  (*(temp++)- '0');
      //printf("%s -> %d %d\n",tempString,stationB[j].departure, stationB[j].arrival); 
      //printf("%s -> %d\n",temp,j);      
     }
     
     qsort(stationA, a, sizeof(TrainTime), compare_function1);
     qsort(stationB, b, sizeof(TrainTime), compare_function1);
     
     struct TrainAvailability* trainAtA = new TrainAvailability[a+b];
     struct TrainAvailability* trainAtB = new TrainAvailability[a+b];
     
     int c = m / 60;
     int d = m % 60;
     
     for(int j= a-1; j>=0; j--)
     {
             trainAtA[a-1-j].availability = -1;
             trainAtA[a-1-j].time = stationA[j].departure;
             
             trainAtB[a-1-j].availability = 1;             
             trainAtB[a-1-j].time = stationA[j].arrival + c * 100 + d;
     }
     
     for(int j= b-1; j>=0; j--)
     {
             trainAtB[a+ b-1 -j].availability = -1;
             trainAtB[a+ b-1 -j].time = stationB[j].departure;
             
             trainAtA[a + b-1-j].availability = 1;
             trainAtA[a + b-1-j].time = stationB[j].arrival + c *100 + d;
     }
     
     qsort(trainAtA, a+b, sizeof(TrainAvailability), compare_function2);
     qsort(trainAtB, a+b, sizeof(TrainAvailability), compare_function2);
     
     int tempSum = 0;
     int minSum = 2000;
     for(int j=0; j<a+b; j++)
     {    
          tempSum += trainAtA[j].availability;
          //printf("%d,%d -> %d\n",j,trainAtA[j].time, tempSum);
          if(tempSum < minSum)
                     minSum = tempSum;
     }
     if(minSum > 0)
        minSum = 0;
     printf("Case #%d: %d",i+1, minSum * -1);
     tempSum = 0;
     minSum = 2000;
     for(int j=0; j<a+b; j++)
     {    
          tempSum += trainAtB[j].availability;
          //printf("%d,%d -> %d\n",j, trainAtB[j].time, tempSum);
          if(tempSum < minSum)
                     minSum = tempSum;
     }
     if(minSum > 0)
        minSum = 0;
     printf(" %d\n", minSum * -1);
     free(stationA);
     free(stationB);
}                

//hash_map <const char *, int> searchString;
//searchString["first"] = 1;
//printf("%d", searchString["first"]);
//searchString.clear();
//scanf("%d",&n);
return 0;

}
