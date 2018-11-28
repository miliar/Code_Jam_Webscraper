#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    FILE *inf = fopen("small.in","r");
    FILE *of = fopen("out.out","w");
    int T;
    fscanf(inf,"%d\n",&T);
    for(int i=0;i<T;i++){
        long long int res = 0;
        int n;
        int a[1000];
        int b[1000];
        fscanf(inf, "%d\n", &n);
        for(int j = 0; j < n; j++){
            fscanf(inf,"%d %d\n", &a[j], &b[j]);
        }
        for(int j=0; j < n; j++){
            for(int k = j+1; k < n; k++){
                if((a[j] < a[k] && b[j] > b[k])||(a[j] > a[k] && b[j] < b[k])){
                    res++;
                }
            }
        }
        fprintf(of,"Case #%d: %d\n", i+1, res);
    }
    fclose(inf);fclose(of);
    return EXIT_SUCCESS;
}

