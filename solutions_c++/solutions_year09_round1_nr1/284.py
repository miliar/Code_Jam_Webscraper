#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

FILE * fout = fopen ("round1A A.out", "w");

int result (int num, int base){
    int re = 0;
    while (num > 0){
          re += (num % base) * (num % base);
          num = num / base;
    }
    return re;
}

bool in (int a, int array[], int length){
     for (int i = 0; i < length; i ++){
         if (array[i] == a){
                      return true;
         }
     }
     return false;
}

void work (int n){
     int base[10];
     int num;
     char c;
     for (int i = 0;; i ++){
         scanf ("%d", &base[i]);
         scanf ("%c", &c);
         if  (c != ' '){
             num = i + 1;
             break;
         }
     }
     for (int j = 2;; j ++){
         bool happy = true;
         for (int k = 0; k < num; k ++){
             int occur[10000];
             int length = 1;
             int test = j;
             occur[0] = test;
             while (test != 1){
                   test = result (test, base[k]);
                   if (test == 1){
                           break; 
                   }
                   if (in (test, occur, length)){
                          happy = false;
                          break;
                   }
                   occur[length] = test;
                   length ++;
             }
             if (!happy){
                         break;
             }
         }
         if (happy){
                    fprintf (fout, "Case #%d: %d\n", n, j);
                    break;
         }
     }
}

int main (){
     int t;
     scanf ("%d", &t);
     for (int i = 0; i < t; i ++){
         work (i + 1);
     }
     return 0;
}
