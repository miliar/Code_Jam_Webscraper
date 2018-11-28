#include <fstream>

using namespace std;

struct lepes
{
    short int m;
    char s;
};

ofstream out;

lepes *t;

short int leptetmasik(char s, short int regi, short int honnan, lepes t[], int meret )
{
    short int i=honnan;
    while(t[i].s != s&&i<meret) i++;
    if(t[i].m>regi) return 1;
    else if(t[i].m<regi) return -1;
    else return 0;
}

int inline lepesgen(lepes t[], int meret)
{
    short int b, o, n;
    b = 1;
    o = 1;
    n = 0;
    bool bb,bo, nyom;

    int kor = 0;
    while(n<meret)
    {
        bb=false;
        bo=false;
        nyom = false;
        if((t[n].s=='B')&& (t[n].m==b))
        {
            bb=true;
            n++;
            nyom = true;
            if(n==meret) {
                kor++;
                break;
            }
        }
        if((t[n].s=='O')&& (t[n].m==o)&& !nyom)
        {
            bo=true;
            n++;
            if(n==meret) {
                kor++;
                break;
            }
        }

        if((t[n].s=='B')&& !bb)
        {
            if(t[n].m>b)
            {
                b++;
                bb = true;
            } else if(t[n].m<b)
            {
                b--;
                bb = true;
            }
        }
        if((t[n].s=='O')&& !bo)
        {
            if(t[n].m>o)
            {
                o++;
                bo = true;
            } else if(t[n].m<o)
            {
                o--;
                bo = true;
            }
        }
        if(!bo) o+=leptetmasik('O',o,n,t, meret);
        if(!bb) b+=leptetmasik('B',b,n,t, meret);
        kor++;
    }
    return kor;
}

int main()
{
    ifstream in;
    in.open("in.txt");
    int ddd;
    in >> ddd;
    out.open("out.out");
    for(int i= 0;i<ddd;i++)
    {
        int dd;
        in >> dd;
        t = new lepes[dd];
        for(int j=0;j<dd;j++)
        {
            lepes l;
            in >> l.s;
            in >> l.m;
            t[j] = l;
        }
        out << "Case #" << i+1 << ": " << lepesgen(t,dd) << endl;
        delete[] t;
    }
    in.close();
    out.close();
    return 0;
}
