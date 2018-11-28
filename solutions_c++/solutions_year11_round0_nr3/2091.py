#include <cstdlib>
#include <cstdio>
#include <cstring>

int main(int argc, char* argv[])
{
    if(argc < 3)
        return 1;
    FILE* in = fopen(argv[1], "r");
    FILE* out = fopen(argv[2], "w");

    const int INF = 100000000;
    unsigned int T,N,low,sum,xorsum;
    fscanf(in, "%d", &T);
    for(int t=0; t<T;t++){
        fscanf(in,"%d", &N);
        low = INF;
        sum = 0;
        xorsum = 0;
        for(int n=0; n<N; n++){
            unsigned int c;
            fscanf(in, "%d", &c);
            if(c<low)
                low = c;
            xorsum ^= c;
            sum += c;
        }
        fprintf(out, "Case #%d: ", t+1);
        if(xorsum)
            fprintf(out, "NO\n");
        else
            fprintf(out, "%d\n", sum-low);
    }
    return 0;
}
