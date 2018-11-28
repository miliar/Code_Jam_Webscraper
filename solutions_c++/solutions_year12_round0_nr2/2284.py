
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

unsigned int calc(unsigned int N, unsigned int S, unsigned int p, unsigned int Total[])
{
         unsigned int val;
         unsigned int count = 0;
         for(int i = 0; i < N; i++)
         {
                 val = Total[i];
                 
                 if (val < p)
                 {
                         continue;
                 }
                 
                 if (val >= (3 * p))
                 {
                     count++;
                 }
                 else if (val == (3*p) - 1)
                 {
                      count++;
                 }
                 else if (val == (3*p) - 2)
                 {
                      count++;
                 }
                 else if ((val == (3*p) - 3) && (S))
                 {
                      count++;
                      S--;
                 }
                 else if ((val == (3*p) - 4) && (S))
                 {
                      count ++;
                      S--;
                 }
                 else
                 {
                     //printf("I can't satisify the condition");
                 }                 
         }
         
         return count;
}


int main() {
//	freopen("b.in", "r", stdin);

//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);


    unsigned int T;
    unsigned int N;
    unsigned int S;
    unsigned int p;
    unsigned int Total[101];
    unsigned int Ans;
    
    FILE *fpI = fopen("B-large.in", "r");
    FILE *fpO = fopen("B-large.out", "w+");
    
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
    
    fscanf(fpI, "%d", &T);
    //printf("%d\n", T);
	for(int i = 0; i < T; i++)
	{
        fscanf(fpI, "%d %d %d", &N, &S, &p);
        //printf("%d %d %d", N, S, p);
        for(int j = 0; j < N; j++)
        {
            fscanf(fpI, "%d" , &Total[j]);
            //printf("%d", Total[j]);    
        }
        
        Ans = calc(N, S, p, Total);
        
        fprintf(fpO, "Case #%d: %d\n",  i + 1, Ans);                       
    }

	return 0;
}
