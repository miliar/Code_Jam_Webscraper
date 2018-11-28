//---------------------------------------------------------------------------

#include <clx.h>
#pragma hdrstop

//---------------------------------------------------------------------------
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define PB push_back
#define FOR(i,m) for(i=0;i<m;++i)
#define SFOR(i,s,m) for(i=s;i<m;++i)
#define SZ(a) (int)a.size()

#pragma argsused
int main(int argc, char* argv[])
{
    FILE *in, *out;
    int N,i;

    in = fopen("B-large.in","rt");
    out= fopen("B-large.out","wt");
    fscanf(in,"%d\n",&N);
    SFOR(i,1,N+1)
    {   int T,NAB,NBA;      //исходные
        fscanf(in,"%d\n",&T);
        fscanf(in,"%d %d\n",&NAB,&NBA);
        //самое интересное - сами поездки
        //в моменты отправлени€ количество убывает, в моменты прибыти€ + “ - прибывает
        VI froma(0),toa(0),fromb(0),tob(0);
        int j,h1,m1,h2,m2;
        FOR(j,NAB)
        {   fscanf(in, "%d %d %d %d\n",&h1,&m1,&h2,&m2);
            froma.PB(m1+60*h1);
            tob.PB(m2+60*h2+T);
        }
        FOR(j,NBA)
        {   fscanf(in, "%d %d %d %d\n",&h1,&m1,&h2,&m2);
            fromb.PB(m1+60*h1);
            toa.PB(m2+60*h2+T);
        }
        //сливаем в 1 массив и сортируем все моменты
        //второй компонент с -, чтобы прибытие было раньше отправлени€
        vector<pair<int,int> > a,b;
        FOR(j,SZ(froma))
            a.PB(make_pair(froma[j],1));
        FOR(j,SZ(toa))
            a.PB(make_pair(toa[j],-1));
        FOR(j,SZ(fromb))
            b.PB(make_pair(fromb[j],1));
        FOR(j,SZ(tob))
            b.PB(make_pair(tob[j],-1));
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        //собственно подсчет
        int nta=0,ntb=0;    //должны начать в ј и ¬
        int cura=0,curb=0;
        FOR(j,SZ(a))
        {   if (a[j].second==-1)
            {   //прибытие
                cura++;
            }
           else
            {   //отправление
                if (cura>0)
                    cura--;
              else  nta++;
            }
        }
        FOR(j,SZ(b))
        {   if (b[j].second==-1)
            {   //прибытие
                curb++;
            }
           else
            {   //отправление
                if (curb>0)
                    curb--;
              else  ntb++;
            }
        }
        fprintf(out,"Case #%d: %d %d\n",i,nta,ntb);
    }
    fclose(in);
    fclose(out);
    return 0;
}
//---------------------------------------------------------------------------
