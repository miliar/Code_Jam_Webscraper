#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

#define M 1001

bool crible[M];

int main()
{
    FILE * input = fopen("inputc.txt", "r");
    FILE * output = fopen("outputc", "w");
    int T;
    fscanf(input, "%d", &T);
    for(int i = 0; i < M; i++) crible[i] = true;
    for(int i = 2; i < M; i++)
    {
        if(crible[i])
        {
            for(int a = 2; a*i < M; a++)
                crible[a*i] = false;
        }
    }
    for(int cas = 1; cas <= T; cas++)
    {
        int n;
        fscanf(input, "%d", &n);
        int petit = 0; int grand = 0;
        for(int i = 2; i <= n; i++)
        {
            if(crible[i])
            {
                //printf("*");
                petit++;
                long long puiss = i;
                while( puiss <= n) { grand++; puiss *= i; }
            }
        }
        if(n > 1) grand++; //pour le "1"
        fprintf(output,"Case #%d: %d\n", cas, grand - petit);
    }
	return 0;
}
