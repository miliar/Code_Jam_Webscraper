#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    FILE *inf = fopen("input.in","r");
    FILE *of = fopen("out.out","w");
    int N;
    fscanf(inf,"%d\n",&N);
    for(int i=0;i<N;i++){
        int n;
        fscanf(inf, "%d\n", &n);
        bool ok[1000] = {false};
        int items[1000];
        for(int j=0; j< n; j++){
            int x;
            fscanf(inf,"%d", &x);
            items[j] = x-1;
            if(j==x-1)ok[j] = true;
        }
        int result = 0;
        for(int j = 0; j < n; j++){
            if(!ok[j]){
                int l = 0;
                int poz = j;
                while(!ok[poz]){
                    l++;
                    ok[poz] = true;
                    poz = items[poz];
                }
                result+=l;
            }
        }
        fprintf(of,"Case #%d: %d.000000\n",i+1, result);
        fscanf(inf,"\n");
    }

    fclose(inf);fclose(of);
    return EXIT_SUCCESS;
}

