#include<cstdio>

#define max_n 1005

using namespace std;

int t[max_n];
int kolor[max_n];
int wynik=0;
int start;

void f(int k){
    if(k==t[k]){
        kolor[k]=1;
        return;
    }
    kolor[k]=1;
    k=t[k];
    wynik++;
    while(k!=start){
        kolor[k]=1;
        wynik++;
        k=t[k];
    }
}



int main(){
    int Z;
    scanf("%d",&Z);
    for(int z=1;z<Z+1;z++){
        wynik=0;
        int n;
        scanf("%d",&n);
        for(int i=1;i<n+1;i++){
            scanf("%d",&t[i]);
            kolor[i]=0;
        }
        for(int i=1;i<n+1;i++)
            if(kolor[i]==0){
                start=i;f(i);
            }

        printf("Case #%d: %d\n",z,wynik);
    }
}
