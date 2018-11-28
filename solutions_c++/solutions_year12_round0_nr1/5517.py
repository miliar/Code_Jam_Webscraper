//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>


//Other Includes
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

#define PB push_back
#define MP make_pair
#define MAXIMUM 18446744073709551615ULL
#define MAX 1010

using namespace std;

typedef long long int LL;
typedef unsigned long long int ULL;
typedef unsigned int UI;
typedef pair<int,int> PII;

char d[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char arr[1000];
int main()
{
    freopen("A-in.txt", "rt", stdin);
	freopen("A-out.txt", "wt", stdout);
    
    int t;
    scanf("%d",&t);
    cin.ignore(80,'\n');
    for (int tc=1; tc<=t; tc++)
    {
          gets(arr);
          printf("Case #%d: ",tc);   
          
          for (int i=0; arr[i] != '\0'; i++)
          {
              if (arr[i]>='a' && arr[i]<='z')
              {
                 printf("%c",d[(arr[i]-'a')]);                
              }    
              else
              printf("%c",arr[i]);
          }
          printf("\n");
    }
    return 0;    
}
