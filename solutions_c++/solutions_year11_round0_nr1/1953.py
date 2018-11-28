/*  Google Code Jam Qualification Round 2011
    Problem A. Bot Trust
    Varot Premtoon 7 May 2554 */

#include <cstdio>

int abs(int x)
{
    if(x<0) return -x;
    return x;
}

int sol(int cse)
{
    int n;
    int o[200][2];
    int b[200][2];
    int io,ib,no,nb;
    int po,pb;
    int i,j;
    char col[2];
    int bt;
    int t,diso,disb;
    scanf("%d",&n);
    no = nb = 0;
    for(i=0;i<n;i++) {
        scanf("%s %d",col,&bt);
        if(col[0]=='B') {
            b[nb][0] = bt;
            b[nb][1] = i;
            nb++;
        } else {
            o[no][0] = bt;
            o[no][1] = i;
            no++;
        }
    }
    po = pb = 1;
    t = 0;
    for(io=ib=0;io<no&&ib<nb;) {
        diso = abs(po-o[io][0]);
        disb = abs(pb-b[ib][0]);
        if(o[io][1]<b[ib][1]) {
            t += diso + 1;
            if(diso>=disb) {
                pb = b[ib][0];
                //ib++;
            } else {
                if(pb < b[ib][0]) pb += diso + 1;
                else pb -= diso + 1;
            }
            po = o[io][0];
            io++;
        } else {
            t += disb + 1;
            if(disb>=diso) {
                po = o[io][0];
                //io++;
            } else {
                if(po < o[io][0]) po += disb + 1;
                else po -= disb + 1;
            }
            pb = b[ib][0];
            ib++;
        }
    }
    for(;io<no;io++) {
        diso = abs(po-o[io][0]);
        t += diso + 1;
        po = o[io][0];
    }
    for(;ib<nb;ib++) {
        disb = abs(pb-b[ib][0]);
        t += disb + 1;
        pb = b[ib][0];
    }
    printf("Case #%d: %d\n",cse,t);
    return 0;
}




int main()
{
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++) sol(i);
    return 0;
}
