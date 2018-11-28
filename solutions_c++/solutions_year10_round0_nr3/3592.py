#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <queue>
#include <stack>
using namespace std;

void read(char *a)		{	freopen(a,"r",stdin);	}
void write(char *a)		{	freopen(a,"w",stdout);	}
//-----------------------------------------------------------------

int main()
{
    int T , m ;
    read("C-small-attempt0.in");
    write("C-small-attempt0.out");
    while(cin >> T)
    {
         for(m = 1 ; m <= T ; m++)
         {
                 int i , j , R , k , N ;
                 int a[1001];
                 cin >> R >> k >> N ;
                 for(i = 1 ; i <= N ; i++)
                     cin >> a[i];
                 int flag = 1 ;
                 int cnt = 0;//
                 for(i = 1 ; i <= R ;i++)
                 {
                       int sum = 0,count = 0;//
                       for(j = flag ; j <= N; j++)
                       {
                            sum += a[j];
                            count ++;
                            if(sum > k||count>N)   //
                            {
                                   sum -= a[j];
                                   flag = j ;
                                   break;
                            }
                            if(j == N)
                            {
                                j = 0;//
                            }
                       }
                       cnt+=sum;
                 }
                 cout << "Case #" << m << ": " << cnt << endl ;
         }
    }         
    return 0;
}
