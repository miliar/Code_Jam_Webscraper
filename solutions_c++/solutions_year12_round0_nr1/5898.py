#include <stdio.h>
#define problem_n problemA

int problemA()
{
    FILE *in = fopen("coded.txt", "r"), *out = fopen("decoded.txt", "w");
    //////////////a///////////////////e//////////////h//////////////k//////////////n//////////////q//////////////t/////////v/////////
    char key[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    int T;
    fscanf(in, "%d", &T);
    fscanf(in, "\n");
    for(int t=0;t<T;t++)
    {
        fprintf(out, "Case #%d: ", t+1);
        while(!feof(in))
        {
            char c;
            fscanf(in, "%c", &c);
            if (c=='\n') break;
            if (c==' ') fprintf(out," ");
            else fprintf(out, "%c", key[c-97]);
        }
        fprintf(out, "\n");
    }
    return 0;

}

int problemB()
{
    FILE *in = fopen("sample.txt", "r"), *out = fopen("a", "w");
    //FILE *in = fopen("", "r"), *out = fopen("", "w");
    int T;
    fscanf(in, "%d", &T);
    for (int t=0; t<T; t++)
    {
        int N,S,P;
        fscanf(in, "%d %d %d", &N, &S, &P);
        int * total = new int[N];
        for (int n=0; n<N; n++)
        {
            fscanf(in, "%d", &total[n]);
            printf("%d\n", total[n]);
        }
    }
}

int problemC()
{
    FILE *in = fopen("sample.txt", "r"), *out = fopen("a", "w");

}


int main() { return problem_n(); }
