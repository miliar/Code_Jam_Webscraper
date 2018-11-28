#include <iostream>
#include <sstream>
#include <string.h>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <fstream>
#include <stdio.h>

#define FOR(i,n) for(i=0;i<(int)n;i++)
#define FOREQ(i,n) for(i=0;i<=n;i++)
#define INF 1.0E+15

using namespace std;

FILE *fin;
FILE *fout;
int N,i,j;

char to[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k',
    'r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	fin = fopen("A-small-attempt1.in","r");
	fout = fopen("output.out","w");
    int T,t=0;
    fscanf(fin,"%d\n",&T);
    while(t<T)
    {
        fprintf(fout,"Case #%d: ",t+1);
        char C;
        fscanf(fin,"%c",&C);
        while(C != '\n')
        {
            if(C == ' ')
                fprintf(fout," ");
            else{
                fprintf(fout,"%c",to[C-'a']);
            }
            fscanf(fin,"%c",&C);
        }
        fprintf(fout,"\n");
        t++;
    }
}
