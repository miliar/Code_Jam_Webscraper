#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
int main()
{
    long n,i,t,m,oc,bc,rPosO,rPosB,o,b,l;
    vector<long> op,om,bp,bm;
    char c;
    scanf("%ld",&n);
    for (l=0;l<n;l++)
    {
        t=0;
        op.clear();
        om.clear();
        bp.clear();
        bm.clear();
        scanf("%ld",&m);
        for (i=0;i<m;++i)
        {
            while ((scanf("%c",&c)) && (c!='O') && (c!='B'));
            if (c=='O')
            {
                scanf("%ld",&o);
                op.push_back(o);
                om.push_back(i);
            }
            else
            {
                scanf("%ld",&b);
                bp.push_back(b);
                bm.push_back(i);
            }
        }
        rPosO=1;
        rPosB=1;
        o=0;
        b=0;
        while ((o<op.size()) || (b<bp.size()))
        {
            oc=0;
            bc=0;
            if (((o<op.size()) && (rPosO==op[o])) && ((b==bm.size()) || (om[o]<bm[b])))
            {
                o++;
                oc=1;
            }
            else if (((b<bp.size()) && (rPosB==bp[b])) && ((o==om.size()) || (bm[b]<om[o])))
            {
                b++;
                bc=1;
            }
            if ((oc==0) && (rPosO!=op[o]))
            {
                rPosO+=(op[o]-rPosO)/(int)(round(abs((double)(op[o]-rPosO))));
            }
            if ((bc==0) && (rPosB!=bp[b]))
            {
                rPosB+=(bp[b]-rPosB)/(int)(round(abs((double)bp[b]-rPosB)));
            }
            t++;
        }
        cout<<"Case #"<<1+l<<": "<<t<<endl;
    }
}
