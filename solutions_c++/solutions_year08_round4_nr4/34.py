#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;

int n, k;
char orig[100000];
char mod[100000];
int perm[20];
int marked[20];
int teste, t;
int resp;

void calc() {
     int i, j;
     char last = 0;
     int aux=0;
     for (i=0; i<n; i+=k){
         for (j=0; j<k; j++){
             mod[i+j]=orig[i+perm[j]];
         }
     }
     for (i=0; i<n; i++){
         if (mod[i]!=last) {
             last = mod[i];
             aux++;
         }
     }
     resp = min(resp,aux);     
}

void gen(int pos) {
     int i;
     if (pos == k) calc();
     for (i=0; i<k; i++) {
         if (marked[i]==1) continue;
         marked[i]=1;
         perm[pos]=i;
         gen(pos+1);
         marked[i]=0;
     }
}

int main() {
    int i;
    int z;
    scanf("%d\n", &teste);
    for (t=0; t<teste; t++){
        scanf("%d\n", &k);
        scanf("%s\n", orig);
        n = strlen(orig);
        resp = 10000;
        for (i=0; i<k; i++) marked[i]=0;
        gen(0);
        printf("Case #%d: %d\n", t+1, resp);
    }
    return 0;    
}
