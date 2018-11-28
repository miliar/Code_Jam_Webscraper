#include <stdio.h>
#include <vector>
#include <deque>
#include <math.h>

using namespace std;

int main(int argc, char **argv){
    long int t,n,k,r,total;;
    deque<int> fila;
    deque<int> roda;

    scanf(" %ld ",&t);
    int i = 1;
    while(t--){
        fila.clear();
        roda.clear();
        total = 0;

        scanf("%ld %ld %ld", &r, &k,&n);

        for(int y = 0; y < n; y++){
            int tmp;
            scanf("%d",&tmp);
            fila.push_back(tmp);
        }

        for(int y = 0; y < r; y++){
               while(!roda.empty()) {
                    fila.push_back(roda.front());
                    roda.pop_front();
               }
               int capacidade = k;
               while(!fila.empty() && fila.front() <= capacidade){
                   capacidade-=fila.front();
                   roda.push_back(fila.front());
                   total+=fila.front();
                   fila.pop_front();
               }


        }

        printf("Case #%d: %d\n",i++,total);
    }
}
