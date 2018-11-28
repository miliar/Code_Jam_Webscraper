#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)

int Min,Max;
int currentnumber;
int last;
map<int,int> pairs;

/*int possible(int a, int b) {
 int i = min(a,b);
 return (i-1)*(i-2)/2;
 }*/

int digitize(int n, int *digits) {
   int count = 0;
   while (n/10 > 0) {
      digits[count] = n%10;
      n/=10;
      count++;
   }
   digits[count] = n;
   return count+1;
}

int wrap(int *digits, int len, int p) {
   int ret = 0;
   int mask = 1;
   for (int i = p; i < len; i++) {
      ret += digits[i]*mask;
      mask*=10;
   }
   for (int i = 0; i < p; i++) {
      ret += digits[i]*mask;
      mask*=10;
   }
   return ret;
}

int check(int *dg, int l, int i) {
   int num = wrap(dg,l, i);
   if (num >= Min && num <= Max) {
      if (!pairs[num] && (last < 0 || num != last)) {
         //printf("[%d,%d]\n",currentnumber,num);
         //printf("[%d,%d]\n",num,currentnumber);
         last = num;
         return 1;
      }
   }
   return 0;
}

int swaps(int n) {
   int count = 0;
   int digits[9];
   pairs[n] = 1;
   last = -1;
   //currentnumber = n;
   int num = digitize(n,digits);
   FR(i,1,num) {
      count += check(digits,num, i);
   }
   return count;
}


int main() {
   int T;
   cin >> T;
   
   FOR(t,T) {
      cin >> Min;
      cin >> Max;
      
      printf("Case #%d: ", t+1);
      int count = 0;
      FR(n,Min,Max+1) {
         count += swaps(n);
      }
      printf("%d\n", count);
      pairs.clear();
   }
   return 0;
}

