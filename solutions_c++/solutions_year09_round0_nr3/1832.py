#include <stdio.h>
#include <vector>
#include <string.h>

using namespace std;

char line[503];
char GG[30] = "welcome to code jam";
const int GGL = 19;
int FL[GGL];

struct BIGINT
{
    int A[21];
};

BIGINT S[500][GGL];

void copy(BIGINT &a, BIGINT const& b)
{
    a.A[0] = b.A[0];
    for (int i=0; i<a.A[0]; i++) 
        a.A[i+1] = b.A[i+1];
    return;
}

void add(BIGINT & a, BIGINT const& b)
{
    int i;
    int sz=a.A[0];
    if (sz < b.A[0]) sz = b.A[0];
    int tmp = 0;
    for (i=1; i<=sz; i++) {
        if (i<=a.A[0]) tmp += a.A[i];
        if (i<=b.A[0]) tmp += b.A[i];
        a.A[i] = tmp % 10000;
        tmp /= 10000;
    }
    if (tmp != 0) {
        a.A[i] = tmp; 
        i++;
    }
    a.A[0] = i-1;
    
    return;
}

void set(BIGINT & a, int b)
{
    a.A[0] = 0;
    while( b > 0 ) {
        a.A[0] ++;
        a.A[ a.A[0] ] = b % 10000;
        b /= 10000;
    }
    return;
}

void print(BIGINT & a)
{
    int sz = a.A[0];
    if (sz == 0) printf("%04d\n", 0);
    else {
        while( sz > 0 ) {
            printf("%04d", a.A[sz]);
            sz--;
        }
        printf("\n");
    }
    return;
}

int process(int L)
{
    int i,j,k;
    for (i=0; i<L; ++i) {
        for(j=0; j<GGL; ++j) S[i][j].A[0] = 0; 
    }

    // pre compute FL
    for (j=0; j<GGL; ++j) {
        for (i=0; i<L; ++i) {
            if (line[i] == GG[j]) {
                FL[j] = i;
                break;
            }
        }
        if (i>=L) return 0;
    }

    for (j=0; j<GGL; ++j) {
        // for each state
        // printf(" ===============  state[%d] = %c ==============\n", j, GG[j]);
        for (i=FL[j]; i<L; ++i) {
            // for each char
            if (GG[j] == line[i]) {
                if (j==0) {
                    set(S[i][j], 1);
                    // printf(" == set S[%d][%d] = 1\n", i, j);
                }
                else {
                    // char laststate = GG[j-1];
                    // add k to i
                    for(k=FL[j-1]; k<i; ++k) {
                        if (GG[j-1] == line[k]) {
                            // printf(" == curr,state,char = %d,%d,%c\n",i,j,line[i]);
                            // printf(" == leftint = ");
                            // print(S[k][j-1]);
                            add(S[i][j], S[k][j-1]);
                        }
                    }
                }
            }
        }
    }
    BIGINT ans;
    set(ans, 0);
    for (i=0; i<L; ++i) {
        // printf("i, char = %d,%c\n", i, line[i]);
        // print(S[i][GGL-1]);
        add(ans, S[i][GGL-1]);
    }
    // print(ans);
    if (ans.A[0] == 0) return 0;
    return ans.A[1];

/*
    BIGINT tmp;
    set(tmp, 0);
    print(tmp);

    set(tmp, 9999);
    print(tmp);

    set(tmp, 10001);
    print(tmp);

    set(tmp, 300000001);
    print(tmp);

    BIGINT b;
    set(b, 100000000);

    for (i=0; i<1000000; i++) {
        add(tmp, b);
        if (i % 1000 == 0) 
            print(tmp);
    }
*/
    return 0;
}

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);

    int i,N,L;
    scanf("%d", &N);
    fgetc(stdin);

    for (i=0; i<N; i++) {
        fgets(line, 502,  stdin);
        L = strlen(line);
        while( line[L-1] == '\r' || line[L-1] == '\n') {
            line[L-1] = '\0';
            L--;
        }
        // printf("%s\n", line);
        printf("Case #%d: %04d\n", i+1, process(L) );
    }

    return 0;
}

