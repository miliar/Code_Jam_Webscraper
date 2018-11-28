#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>
#include "euler.h"

using namespace std;

#define FOR(i,a,b) for (int i(a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

struct info
{
    double B;
    double E;
    double W;
};

int compare(info A, info B)
{
    return A.B<B.B;
}

int compare2(info A, info B)
{
    return A.W<B.W;
}


int main()
{
    int T;
    vector<info> I;
    cin>>T;
    REP(i,T)
    {
        double X,S,R,t,N,min=100000000;
        I.clear();
        cin>>X>>S>>R>>t>>N;
        REP(j,N)
        {
            info n;
            cin>>n.B>>n.E>>n.W;
            I.pb(n);
        }
        sort(I.begin(),I.end(),compare);
        REP(j,N)
        {
            double len=X;
            double cut=0;
            vector<info> seq;
            FOR(l,j,N)
            {
                if (I[l].B>=cut)
                {
                    seq.pb(I[l]);
                    cut=I[l].E;
                    len-=I[l].E-I[l].B;
                }
            }
            sort(seq.begin(),seq.end(),compare2);
            double tme=0,maxr=t,maxd=0;
            maxd=maxr*R;
            if (maxd>len)
            {
                tme+=((double)len)/R;
                maxr-=tme;
            }
            else
            {
                maxr=0;
                tme+=t;
                tme+=(len-maxd)/S;
            }
            REP(l,seq.size())
            {
                double tm=0;
                if (maxr>0)
                {
                    maxd=(seq[l].W+R)*maxr;
                    if (maxd>seq[l].E-seq[l].B)
                    {
                        tme+=(seq[l].E-seq[l].B)/(seq[l].W+R);
                        maxr-=(seq[l].E-seq[l].B)/(seq[l].W+R);
                    }
                    else
                    {
                        tme+=maxr;
                        tme+=(seq[l].E-seq[l].B-maxd)/(seq[l].W+S);
                        maxr=0;
                    }
                }
                else
                {
                    tme+=(seq[l].E-seq[l].B)/(seq[l].W+S);
                }
            }
            if (tme<min)
            {
                min=tme;
            }
        }
        printf("Case #%d: %.9lf\n",i+1,min);
    }
}
