#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define P 10000

int main(int argc, char **argv) {
    FILE* f = fopen(argv[1], "r");
    
    int N;
    fscanf(f, "%d", &N);

    char buf[600];

    fgetc(f);

    char* msg = "welcome to code jam";
    int msglen = strlen(msg);

    for(int i = 0; i< N; i++) {
        printf("Case #%d: ", i+1);
        fgets(buf, 555, f);
        int len = strlen(buf);
        //printf("%d\n", len);
        //printf("%s", buf);

        int ways[22];
        memset(ways, 0, sizeof(ways));
        ways[0] = 1;

        for (int j = 0; j < len-1; j++) {
            for (int k = 1; k <= msglen; k++) {
                if (buf[j] == msg[k-1]) {
                    ways[k] = (ways[k] + ways[k-1]) % P;
                }
            }
        }

        printf("%04d\n", ways[msglen]);
    }
    

    fclose(f);
    return 0;
}
