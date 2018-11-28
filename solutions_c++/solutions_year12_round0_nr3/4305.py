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
#include <stdlib.h>

#define FOR(i,n) for(i=0;i<(int)n;i++)
#define FOREQ(i,n) for(i=0;i<=n;i++)
#define INF 1.0E+15

using namespace std;

FILE *fin;
FILE *fout;

int main()
{
    fin = fopen("C-small-attempt1.in","r");
    //fin = fopen("1.in","r");
    fout = fopen("output.out","w");
    int T;
    fscanf(fin,"%d",&T);
    int t = 0;
    while(t<T)
    {
        int i,j;
        set<pair<int,int> > _set;
        fprintf(fout,"Case #%d: ",t+1);
        int A,B;
        fscanf(fin,"%d %d",&A,&B);
        for(i=A;i<=B;++i)
        {
            char buffer[30];
            memset(buffer,0,sizeof(buffer));
            sprintf(buffer,"%d%d",i,i);
            int length = strlen(buffer) / 2;
            for(j=1;j<length;++j)
            {
                char bf[15];
                memset(bf,0,sizeof(bf));
                strncpy(bf,buffer+j,length);
                printf("bf %s\n",bf);
                int n1 = atoi(bf);
                if(n1 > B || n1 < A || n1 == i)
                    continue;
                printf(":%d\n",n1);
                if(i < n1)
                    _set.insert(make_pair(i,n1));
                else
                    _set.insert(make_pair(n1,i));
            }
        }
        fprintf(fout,"%d\n",_set.size());
        t++;
    }
}
