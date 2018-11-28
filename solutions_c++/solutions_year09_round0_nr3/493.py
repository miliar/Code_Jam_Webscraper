#include <cstdio>
#include <cstring>

using namespace std;

#define MAXL 5000

int n, ln;
char codejam[20] = "welcome to code jam";
int f[MAXL + 1][27];
char now[MAXL + 1];
int test = 0;

void ini(void)
{
     int i, j;
     
     memset(f, 0, sizeof(f));
     gets(now); ln = strlen(now);
     
     return;
} 

void work(void)
{
     int i, j, k;
     char tmp;
     
     for(j=0; j<20; j++)
     {
              for(i=0; i<ln; i++)
              {
                       if (now[i] == codejam[j])
                       {
                                  if (j - 1 >= 0)
                                 	 for (k=0; k<i; k++)
                                     { 
                                        	if(now[k] == codejam[j - 1])
                    						{
					                  			f[i][j] += f[k][j - 1];
                            					f[i][j] %= 10000;
							                }
                                     }
                                  else
                                    f[i][j] = 1;
						}
              }
     }
     
  	int res = 0;
	for (i=0; i<ln; i++)
	{
		res += f[i][18];
		res %= 10000;
	}
	test++;
	printf ( "Case #%d: %04d\n", test, res);
     
     
    return;
}

int main(void)
{
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
   
    int p, i;
    scanf("%d\n", &p);
    
    for(i=1; i<=p; i++)
    {
     ini();
     work();
    }
    return 0;
}
