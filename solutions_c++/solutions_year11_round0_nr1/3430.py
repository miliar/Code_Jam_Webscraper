#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large-result.out");
struct node
{
    int num;
    int flag;
};
node x[205],y[205];
int main()
{

    int t,n,b,c,d,tt=1;
    char a;
    fin>>t;
    while(t--)
    {
        fin>>n;
        c = d = 0;
        for(int i=0;i<n;i++)
        {
            fin>>a>>b;
            if(a=='O')
            {
                x[c].num=b;
                x[c++].flag=i;
            }
            else if(a=='B')
            {
                y[d].num=b;
                y[d++].flag=i;
            }
        }
        int anss = 0;
        int cc=0,dd=0;
        int nn=1,mm=1;
        for(int i=0;i<n;i++)
        {
            if(cc<c && x[cc].flag==i)
            {
                int tem = x[cc].num;
                int ans = abs(tem - nn) + 1;
                anss += ans;
                nn = tem;
                if(dd<d){
                if(abs(y[dd].num-mm)<=ans)
                {
                    mm=y[dd].num;
                }
                else
                {
                    //y[dd].num = mm - ans;
                    if(mm > y[dd].num)
                    {
                        mm -= ans;
                    }
                    else
                    {
                        mm += ans;
                    }
                }
                }
                cc++;
            }
            else if(dd<d && y[dd].flag==i)
            {
                int tem = y[dd].num;
                int ans = abs(tem - mm) + 1;
                anss += ans;
                mm = tem;
                if(cc<c){
                if(abs(x[cc].num-nn)<=ans)
                {
                    nn=x[cc].num;
                }
                else
                {
                    //y[dd].num = mm - ans;
                    if(nn > x[cc].num)
                    {
                        nn -= ans;
                    }
                    else
                    {
                        nn += ans;
                    }
                }
                }
                dd++;
            }
            //dd++;
        }
        fout <<"Case #"<<tt++<<": ";
        fout << anss << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
