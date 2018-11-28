#include <stdio.h>

FILE *fin, *fout;
int na, nb, n, spintime;
int counta, countb;
int data[2][110][2];
int matrix[410][410];

void input()
{
    int i, a, b, c ,d;
    char temp[120] = {0,};

    fscanf(fin, "%d", &spintime);
    fscanf(fin, "%d%d", &na, &nb);
    fscanf(fin, "%c", &temp[0]);

    for(i=1; i<=na; i++) {
        fgets(temp, 100, fin);
        sscanf(temp, "%d:%d %d:%d", &a, &b, &c, &d);

        data[0][i][0] = 60*a + b;
        data[0][i][1] = 60*c + d + spintime;
    }
    for(i=1; i<=nb; i++) {
        fgets(temp, 100, fin);
        sscanf(temp, "%d:%d %d:%d", &a, &b, &c, &d);

        data[1][i][0] = 60*a + b;
        data[1][i][1] = 60*c + d + spintime;
    }

    n = na + nb;
    counta = countb = 0;
}

#define QMAX 100000
int queue[QMAX];
int front, rear;
int check[410], trace[410];
void put(int k)
{
    ++rear;
    if(rear == QMAX)
        rear = 0;
    queue[rear] = k;
}
int get()
{
    int k = queue[front];
    ++front;
    if(front == QMAX)
        front = 0;
    return k;
}
int BFS()
{
    int i, v;

    for(i=0; i<=n+n+1; i++)
        check[i] = 0;

    front = 0;  rear = -1;

    put(0);
    check[0] = 1;
    trace[0] = -1;
    while(front <= rear) {
        v = get();

        if(v == n+n+1)
            return 1;

        for(i=1; i<=n+n+1; i++) {
            if(matrix[v][i] == 1 && check[i] == 0) {
                put(i);
                check[i] = 1;
                trace[i] = v;
            }
        }
    }

    return 0;
}

void argu()
{
    int t = n+n+1, min = 99999999;
    while(trace[t] != -1) {
        if(min > matrix[trace[t]][t])
            min = matrix[trace[t]][t];
        t = trace[t];
    }

    t = n+n+1;
    while(trace[t] != -1) {
        matrix[trace[t]][t] -= min;
        matrix[t][trace[t]] += min;
        t = trace[t];
    }
}

void proc()
{
    int i, j, vi, vj;

    for(i=0; i<=n+n+1; i++) {
        for(j=0; j<=n+n+1; j++)
            matrix[i][j] = 0;
    }

    for(i=1; i<=n; i++)
        matrix[0][i] = 1;
    for(i=n+1; i<=n+n; i++)
        matrix[i][n+n+1] = 1;

    for(i=1; i<=na; i++) {
        for(j=1; j<=nb; j++) {
            /* i -> j ? */
            if(data[0][i][1] <= data[1][j][0]) {
                vi = i;
                vj = na + j;

                matrix[vi][n+vj] = 1;
            }

            /* j -> i ? */
            if(data[1][j][1] <= data[0][i][0]) {
                vi = i;
                vj = na + j;

                matrix[vj][n+vi] = 1;
            }
        }
    }

    while(BFS())
        argu();

    for(i=n+1; i<=n+n; i++) {
        if(matrix[n+n+1][i] == 0) {
            if(i - n <= na)
                counta++;
            else
                countb++;
        }
    }
}

void output(int casei)
{
    fprintf(fout, "Case #%d: %d %d\n", casei, counta, countb);
}

int main()
{
    int casei, casen;

    fin = fopen("input.txt", "r");
    fout = fopen("output.txt", "w");

    fscanf(fin, "%d", &casen);

    for(casei=1; casei<=casen; casei++) {
        input();
        proc();
        output(casei);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
