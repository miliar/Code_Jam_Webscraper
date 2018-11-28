
#include <conio.h>
#include <stdio.h>
#include <math.h>
using namespace std;
typedef long long ll;

const int inf = 1000000009;
//const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

unsigned long pow10(int i)
{
         unsigned long val = 1; 
         for (int j = i; j > 0; j--)
         {
             val = val * 10;
         }
         
         return val;
}

FILE *gfpO = NULL;

unsigned int compute (unsigned int A, unsigned int B)
{
         unsigned int rotated = 0;
         unsigned int countOnce = 0;

         for (int i = A; i < B; i++)
         {
             int count = 0;
             int num = i;
             while(num != 0)
             {
                     num = num /10;
                     count++;
             }
             //printf("count = %d\n", count);
             countOnce = 0;
             unsigned long LastAns[15] = {0};
             for (int j = 1; j < count; j++)
             {
                 unsigned long first = 0;
                 unsigned long second = 0;

                 
                 first = i / pow10(count - j);
                 second = i % pow10(count - j);
               
                 //second = second * (10 ^ (count - j));
                 second = second * pow10(j);
                 

                 second = second + first;
                 

                 //printf("%d\n", second);
                 if (second > i && second <= B)
                 {
                      for(int k = 1; k < j; k++)
                      {
                              if (second == LastAns[k])
                              {
                                         countOnce = 1;                                         
                                         break;                                         
                              }
                      }
                      
                      if (countOnce == 0)       
                         rotated++;
                      //fprintf(gfpO, "roatated = %d, i = %d, second = %d\n", rotated, i, second);      
                 }
                 
                 LastAns[j] = second;                 
             }                                      
         }
         
         return rotated;
}

int main() {
//	freopen("b.in", "r", stdin);

//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);


    unsigned int T, A, B;
    unsigned int Ans;

    FILE *fpI = fopen("C-large.in", "r");
    FILE *fpO = fopen("C-large.out", "w+");
    gfpO = fopen("debug.txt", "w+");
    
    if (NULL == fpI)
    {
             printf("NULL1\n");
             getch();
             return -1;
    }
    
    if (NULL == fpO)
    {
             printf("NULL2\n");
             getch();
             return -1;
    }
    
    if (NULL == gfpO)
    {
             printf("NULL3\n");
             getch();
             return -1;
    }
        
    fscanf(fpI, "%d", &T);
    //printf("%d\n", T);
	for(int i = 0; i < T; i++)
	{
            fscanf(fpI, "%d %d", &A, &B);
            //printf("%d %d\n", A, B);
            Ans = compute(A, B);
            //printf("(%d, %d) -> %d\n", A, B, Ans);
            fprintf(fpO, "Case #%d: %d\n", (i+1), Ans);          
                        
    }
	
	//getch();
	return 0;
}
