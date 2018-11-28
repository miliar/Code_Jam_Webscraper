#include<iostream>
#include<algorithm>
using namespace std;
struct bb
{
       int index;
       int stop;
} Bmove[100];
struct oo
{
       int index;
       int stop;
} Omove[100];
int main()
{
    freopen("out.txt","w",stdout);
    freopen("A-large.in","r",stdin);
    int t,N;
    char r,temp;
    int m;
    int bl, ol;
    int i,j,k;
    int finish;
    int tt;
    int cb,co,bn,on,bi,oi;
    bool notfinish,bpush,opush;
    cin>>t;
    for (k = 1; k<=t; k++)
    {
        for (i = 0; i<100; i++)
        {
            Bmove[i].index = 1000000;
            Bmove[i].stop =  1000000;
            Omove[i].index = 1000000;
            Omove[i].stop =  1000000;
        }
          bl = 0;
          ol = 0;
          scanf("%d ",&N);
          for (i = 0; i<N; i++)
          {
             scanf("%c %d%c", &r, &m, &temp);
             if (r == 'B') 
             {
                Bmove[bl].index = i;
                Bmove[bl].stop = m;
                bl++;
             }
             else
             {
                Omove[ol].index = i;
                Omove[ol].stop = m; 
                ol++;
             }
          }
          tt = 0;
          cb = 1;
          co = 1;
          i = 0;
          j = 0;
          bn = Bmove[i].stop;
          on = Omove[j].stop;
          bi = Bmove[i].index;
          oi = Omove[j].index;
          finish = 0;
          bpush = false;
          opush = false;
          notfinish = false;
          if (finish < N)
             notfinish = true;
          while (notfinish)
          {
                tt++;
                if (cb == bn)
                {
                    if (bi < oi)
                    {
                       finish++;
                       bpush = true;
                       if (finish == N)
                          notfinish = false;
                    }
                }
                else
                {
                    if (cb > bn)
                       cb--;
                    else cb++;
                }
                if (co == on)
                {
                    if (oi < bi)
                    {
                           finish++;
                           opush = true;
                           if (finish == N)
                              notfinish = false;
                    }
                }
                else
                {
                    if (co > on)
                       co--;
                    else co++;
                }
                if (bpush)
                {
                    i++;
                    bn = Bmove[i].stop;
                    bi = Bmove[i].index;
                    bpush = false;
                }
                if (opush)
                {
                    j++;
                    on = Omove[j].stop;
                    oi = Omove[j].index;
                    opush = false;
                }
          }
          cout<<"Case #"<<k<<": "<<tt<<endl;
    }
    return 0;
}
