#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    FILE *inf = fopen("input.in","r");
    FILE *of = fopen("out.out","w");
    int T;
    fscanf(inf,"%d\n",&T);
    for(int i=0;i<T;i++){
        int N;
        fscanf(inf, "%d", &N);
        char c;
        int x;
        int bpos = 1;
        int opos = 1;
        int btime = 0;
        int otime = 0;
        int totalTime = 0;
        for(int j = 0; j < N; j++){
            fscanf(inf, " %c %d", &c, &x);
            if(c == 'O'){
                totalTime += max(abs(opos - x)+1-otime, 1);
                btime+=max(abs(opos - x)+1-otime, 1);
                otime = 0;
                opos = x;
            }else{
                totalTime += max(abs(bpos - x)+1-btime, 1);
                otime+=max(abs(bpos - x)+1-btime, 1);
                btime = 0;
                bpos = x;
            }
        }
        fprintf(of, "Case #%d: %d\n", i+1, totalTime);
    }
    fclose(inf);fclose(of);
    return EXIT_SUCCESS;
}

