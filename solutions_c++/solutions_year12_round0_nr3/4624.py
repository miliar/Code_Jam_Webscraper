#include <cstdio>
#include <cstdlib>
#include <map>

using namespace std;

map<int, int> mp;
int n, m, decounter = 0;
int h[1000], lenght, tmp;
int pw[6] = {1, 10, 100, 1000, 10000, 100000};
int check(int a){
   lenght = 0;
   tmp = a;
   while(a!=0){
      h[lenght] = a%10;
      a/=10;
      lenght ++;
   }
   mp.clear();
   //printf("hi%d\n", lenght);
   //for (int i = lenght-1; i>=0; i--)printf("%d", h[i]);
   //printf("\n");
   int num;
   
   for (int i = 0; i<lenght; i++){
      if (h[(i+lenght-1)%lenght]!=0){
         num = 0;
         for (int j = lenght-1; j>=0; j--)
             num += pw[j]* h[(i+j)%lenght];
             //printf("%d", h[(i+j)%lenght]);
         //printf("%d\n", num);
         if (num!=tmp && num>=n && num<= m && mp[num]==false ) {
            //printf("%d --> %d\n", tmp, num);
            mp[num] = true;
            decounter++;
         }
      }
   }
   //printf("\n");
}
   
int main(){
   FILE *fi = fopen("in.in", "r");
   FILE *fo = fopen("out.out", "w");
   int cnt = 0, t;
   fscanf(fi, "%d", &t);
   for (int l = 0; l!=t; l++){
      decounter = 0;
      fscanf(fi, "%d%d", &n, &m);
      if (n<10) n = 10;
      //printf("%d %d\n", n, m);
      for (int i = n; i<=m; i++)
         check(i);
      fprintf(fo, "Case #%d: %d\n", l+1,decounter/2);//system("pause");
   }
   
}
