#include <cstdlib>
#include <cstdio>
#include <cstring>

int main(int argc, char* argv[])
{
    if(argc < 3)
        return 1;
    FILE* in = fopen(argv[1], "r");
    FILE* out = fopen(argv[2], "w");

    char stack[101];
    char combos[80][3];
    char oppose[60][2];
    int at;
    int T,C,D,N;
    fscanf(in, "%d", &T);
    for(int t=0; t<T; t++){
        memset(stack, 0, 101);
        memset(combos, 0, 80*3);
        memset(oppose, 0, 60*2);
        at = 0;

        fscanf(in,"%d", &C);
        for(int c = 0; c < C*2; c+=2){
            fscanf(in, " %c%c%c", &combos[c][0], &combos[c][1], &combos[c][2]);
            combos[c+1][0] = combos[c][1];
            combos[c+1][1] = combos[c][0];
            combos[c+1][2] = combos[c][2];
        }

        fscanf(in,"%d", &D);
        for(int d = 0; d < D*2; d+=2){
            fscanf(in, " %c%c", &oppose[d][0], &oppose[d][1]);
            oppose[d+1][0] = oppose[d][1];
            oppose[d+1][1] = oppose[d][0];
        }

        fscanf(in,"%d ", &N);
        for(int n = 0; n < N; n++){
            fscanf(in, "%c", &stack[at++]);
            if(at == 1)
                continue;//Can't do anything with only one element
            bool notBase = false;
            for(int c = 0; c < C*2; c++){
                if(stack[at-2] == combos[c][0] && stack[at-1] == combos[c][1]){
                    stack[at - 2] = combos[c][2];
                    --at;
                    notBase = true;
                    break;
                }
            }
            if(notBase)
                continue;
            for(int d = 0; d < D*2; d++){
                for(int acc = 0; acc < at; acc++){
                    if(stack[acc] == oppose[d][0] && stack[at - 1] == oppose[d][1]){
                        at = 0;
                        d = D*2;//to break out
                        break;
                    }
                }
            }
        }

        fprintf(out, "Case #%d: [", t+1);
        for(int acc = 0; acc < at; acc++){
            fprintf(out, "%c", stack[acc]);
            if(acc!=at-1)
                fprintf(out, ", ");
        }
        fprintf(out, "]\n");
    }
    return 0;
}
