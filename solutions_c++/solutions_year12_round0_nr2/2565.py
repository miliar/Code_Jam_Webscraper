#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>

using namespace std;

class triplet
{
  public:
  int a,b,c,sum,high;
  bool sup;
};

ifstream in("input.in");
ofstream out("output.out");
int n, s, p;
string tmp;
triplet tr[200];


void eset2()
{
    string temp;
    string a;


    int scr[100];
    bool supr[100];
    bool psb[100];
    bool psp[100];
    bool xspr[100];
    stringstream str;
    int d,e, pst;
    getline(in, tmp);
    str << tmp;
    str >> n;
    str >> s;
    str >> p;
    for (int i=1; i<=n;i++)
    {
        supr[i]=false;
        psb[i]=false;
        psp[i]=false;
    }
    if (p!=0)
    {
    for (int i=1; i<=n; i++)
    {
        str >> scr[i];
        supr[i]=false;
        psb[i]=false;
        psp[i]=false;
        xspr[i]=true;
        for (int j=1; j<=179; j++)
        {
            if (tr[j].sum==scr[i])
            {
                if (tr[j].high>=p)
                {
                    psb[i]=true;
                    if (tr[j].sum==28)
                    {
                        cout << "sün";
                    }
                    if (!tr[j].sup) {xspr[i]=false;}
                }
                if (tr[j].sup)
                {
                    if (psp[i]==false)
                    {
                        supr[i]=true;
                    }
                }
                else
                {
                    if (supr[i])
                    {
                        psp[i]=true;
                        supr[i]=false;
                    }
                }
            }
        }
    }

    int possible=0;
    int suprising=0;
    int psuprising=0;
    int it;
    for (int i=1; i<=n; i++)
    {
        if (psb[i] && xspr[i])
        {
            possible++;
        }
        if (supr[i])
        {
            suprising++;
        }
    }
    if (possible>s)
    {
        while (possible>s)
        {
            possible--;
            suprising--;
        }
    }
    for (int i=1; i<=n; i++)
    {
        if (psb[i] && !xspr[i]) {possible++;}
    }
    /*if (suprising<s)
    {
        while (suprising<s)
        {
            possible--;
            suprising++;
        }
    }*/
        out << possible;
        if (possible==-1)
        {
            cout << "sün";
        }
    }
    else
    {
        out << n;
    }

}

int main()
{
    int t;
    int o;
    in >> t;
    getline(in,tmp);
    ifstream trip("tr.in");
    stringstream strm;
    string tm;
    for (int i=1; i<=179;i++)
    {
        trip >> tr[i].a;
        trip >> tr[i].b;
        trip >> tr[i].c;
        trip >> tr[i].sup;
        tr[i].sum=tr[i].a+tr[i].b+tr[i].c;
        tr[i].high=max(max(tr[i].a,tr[i].b),tr[i].c);
        cout << tr[i].sum;
        cout << endl;
    }
    for (int c=1; c<=t; c++)
    {
        out << "Case #" << c << ": ";
        eset2();
        out << endl;
    }
}
