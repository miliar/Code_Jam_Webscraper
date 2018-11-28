#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <fstream>
using namespace std;
const int MAXN=1001;
int N;
int c[MAXN];

int main()
{
    int T;
    ifstream in;
    ofstream out;
    out.open("C-large.out",ios::trunc);
    in.open("C-large.in");
    in>>T;
    int casenum=0;
    while(T--)
    {
        casenum++;
        in>>N;
        int orsum=0;
        for(int i=0;i<N;i++)
        {
            in>>c[i];
            orsum^=c[i];
        }
        if(orsum!=0)
        {
            //printf("Case #%d: NO\n",casenum);
            out<<"Case #"<<casenum<<": NO"<<endl;
            continue;
        }
        sort(c,c+N);
        int res=0;
        for(int i=1;i<N;i++)
        {
            res+=c[i];
        }
        //printf("Case #%d: %d",casenum,res);
        out<<"Case #"<<casenum<<": "<<res<<endl;
    }
    out.close();
    in.close();
}
