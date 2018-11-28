#include<iostream>
#include<fstream>
using namespace std;

int tt;

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("a.out");
    fin>>tt;
    for (int k=0;k<tt;k++)
    {
        int n,po=1,pb=1,to=0,tb=0;
        int t[200],p[200];
        fin>>n;
        for (int i=0;i<n;i++)
        {
            char c;
            fin>>c;
            if (c=='O') t[i]=1; else t[i]=2;
            fin>>p[i];
        }
        int r=0;
        while (r<n)
        {
              if (t[r]==1)
              {
                          to=to+abs(po-p[r])+1;
                          if (to<=tb) to=tb+1;
                          po=p[r];
              }
              if (t[r]==2)
              {
                          tb=tb+abs(pb-p[r])+1;
                          if (tb<=to) tb=to+1;
                          pb=p[r];
              }
              r++;
        }
        if (to>tb) fout<<"Case #"<<k+1<<": "<<to<<endl;
        else fout<<"Case #"<<k+1<<": "<<tb<<endl;
    }
}
