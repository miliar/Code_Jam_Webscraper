#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

FILE * fout = fopen ("a.out", "w");

void work (int num){
     int n;
     scanf ("%d", &n);
     int count[50];
     for (int i = 0; i < n; i ++){
         count[i] = 0;
         for (int j = 0; j < n; j ++){
                  char t;
                  cin >> t;
                  if (t == '1'){
                        count[i] = j;
                     }
         }
     }
     int re = 0;
     for (int i = 0; i < n; i ++){
         for (int j = i; j < n; j ++){
             if (count[j] <= i){
                for (int k = j; k > i; k --){
                    int temp = count[k];
                    count[k] = count[k - 1];
                    count[k - 1] = temp;
                }
                re += (j - i);
                break;
             }
         }
     }
     fprintf (fout, "Case #%d: %d\n", num, re);
     return;
}

int main (){
    int t;
    scanf ("%d", &t);
    for (int i = 0; i < t; i ++){
        work (i + 1);
    }
    return 0;
}
