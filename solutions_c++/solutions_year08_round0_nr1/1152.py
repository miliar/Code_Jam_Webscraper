#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

int n,s,q,re=0;
map<string,int> m;
vector <int> qu;


int main()
{
    FILE *f=fopen("A-large.in","r");
    fstream fout("A-large.out",ofstream::out);
    fscanf(f,"%d\n",&n);
    string te;
    for (int j=1;j<=n;j++)
    {
        re=0;
        m.clear();
        fscanf(f,"%d\n",&s);
        char c[250];
        for (int i=0;i<s;i++)
        {
            fgets(c,200,f);
            te=c;
            te=te.substr(0,te.length()-1);
            m[te]=i;
        }
        fscanf(f,"%d\n",&q);
        qu.resize(0);
        for (int i=0;i<q;i++)
        {
            fgets(c,200,f);
            te=c;
            if (j!=n || i!=q-1) te=te.substr(0,te.length()-1);
            qu.push_back(m[te]);
        }
        bool w[s];
        for (int i=0;i<s;i++) w[i]=0;
        int cp=0,cc=0;
        while (cp<q)
        {
              while (cc<s && cp<q)
              {
                    if (w[qu[cp]]==0)
                    {
                       cc++;
                       w[qu[cp]]=1;
                    }
                    cp++;
              }
              if (cc>=s) 
              {
                re++;
                for (int i=0;i<s;i++) w[i]=0;
                w[qu[cp-1]]=1;
                cc=1;
              }
        }
        fout << "Case #" << j << ": " << re << "\n";  
    }
    fclose(f);
    fout.close();
    return 0;
}
