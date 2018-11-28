#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <set>
#include <map>
#include <deque>
#include <sstream>
#include <cstring>
using namespace std;
typedef vector<string> vs;
typedef vector<vector<string> > vvs;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

int main()
{
   int a,b;
   scanf("%d\n", &a);
   for (b=1; b<=a; b++)
   {
      char str[1000];
      cin.getline(str,1000);
      int l = strlen(str);

      int memo[19] = {0};
      for (int c=0; c<l; c++)
      {
         if (str[c]=='w')
            memo[0]++;
         else if (str[c]=='e')
         {
            memo[1]=(memo[1]+memo[0]) % 10000;
            memo[6]=(memo[6]+memo[5]) % 10000;
            memo[14]=(memo[14]+memo[13]) % 10000;
         }
         else if (str[c]=='l')
            memo[2]=(memo[2]+memo[1]) % 10000;
         else if (str[c]=='c')
         {
            memo[3]=(memo[3]+memo[2]) % 10000;
            memo[11]=(memo[11]+memo[10]) % 10000;
         }
         else if (str[c]=='o')
         {
            memo[4]=(memo[4]+memo[3]) % 10000;
            memo[9]=(memo[9]+memo[8]) % 10000;
            memo[12]=(memo[12]+memo[11]) % 10000;
         }
         else if (str[c]=='m')
         {
            memo[5]=(memo[5]+memo[4]) % 10000;
            memo[18]=(memo[18]+memo[17]) % 10000;
         }
         else if (str[c]=='t')
            memo[8]=(memo[8]+memo[7]) % 10000;
         else if (str[c]=='d')
            memo[13]=(memo[13]+memo[12]) % 10000;
         else if (str[c]=='j')
            memo[16]=(memo[16]+memo[15]) % 10000;
         else if (str[c]=='a')
            memo[17]=(memo[17]+memo[16]) % 10000;
         else if (str[c]==' ')
         {
            memo[7]=(memo[7]+memo[6]) % 10000;
            memo[10]=(memo[10]+memo[9]) % 10000;
            memo[15]=(memo[15]+memo[14]) % 10000;
         }
      }

      memo[18] = memo[18]%10000;
      printf("Case #%d: ",b);
      if (memo[18]<1000) printf("0");
      if (memo[18]<100) printf("0");
      if (memo[18]<10) printf("0");
      printf("%d\n", memo[18]);
   }
   return 0;
}

