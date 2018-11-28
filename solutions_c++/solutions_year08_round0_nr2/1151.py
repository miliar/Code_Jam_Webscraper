#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

int n,t,na,nb,t1;
vector <string> a,b;

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> n;
    for (int j=1;j<=n;j++)
    {
        int ast=0,bst=0;
        fin >> t >> na >> nb;
        a.resize(0);
        b.resize(0);
        string te;
        for (int i=0;i<na;i++)
        {
            fin >> te;
            t1=60*((te[0]-'0')*10+te[1]-'0')+(te[3]-'0')*10+te[4]-'0';
            te.resize(4);
            te[3]=t1%10+'0'; t1/=10; 
            te[2]=t1%10+'0'; t1/=10;
            te[1]=t1%10+'0'; t1/=10;
            te[0]=t1+'0';
            a.push_back(te);
            fin >> te;
            t1=60*((te[0]-'0')*10+te[1]-'0')+(te[3]-'0')*10+te[4]-'0';
            te.resize(4);
            te[3]=t1%10+'0'; t1/=10; 
            te[2]=t1%10+'0'; t1/=10;
            te[1]=t1%10+'0'; t1/=10;
            te[0]=t1+'0';
            a[a.size()-1]+=" "+te;
        }
        for (int i=0;i<nb;i++)
        {
            fin >> te;
            t1=60*((te[0]-'0')*10+te[1]-'0')+(te[3]-'0')*10+te[4]-'0';
            te.resize(4);
            te[3]=t1%10+'0'; t1/=10; 
            te[2]=t1%10+'0'; t1/=10;
            te[1]=t1%10+'0'; t1/=10;
            te[0]=t1+'0';
            b.push_back(te);
            fin >> te;
            t1=60*((te[0]-'0')*10+te[1]-'0')+(te[3]-'0')*10+te[4]-'0';
            te.resize(4);
            te[3]=t1%10+'0'; t1/=10; 
            te[2]=t1%10+'0'; t1/=10;
            te[1]=t1%10+'0'; t1/=10;
            te[0]=t1+'0';
            b[b.size()-1]+=" "+te;
        }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        int ac=0,bc=0;
        vector <string> aq(0),bq(0);
        while (a.size()>0 || b.size()>0)
        {
              if (b.size()<=0 || (a.size()>0 && a[0]<b[0]))
                 {
                     for (int i=0;i<aq.size();i++)
                     {
                         if (aq[i]<=a[0].substr(0,4))
                         {
                             ac++;
                             aq.erase(aq.begin()+i);
                             i--;
                         }
                     }
                     ac--;
                     if (ac<0) { ast++; ac++; }
                     te=a[0].substr(5,4);
                     t1=(te[0]-'0')*1000+(te[1]-'0')*100+(te[2]-'0')*10+te[3]-'0'+t;
                     te[3]=t1%10+'0'; t1/=10; 
                     te[2]=t1%10+'0'; t1/=10;
                     te[1]=t1%10+'0'; t1/=10;
                     te[0]=t1+'0';
                     bq.push_back(te);
                     a.erase(a.begin());
                 }
              else
                 {
                     for (int i=0;i<bq.size();i++)
                     {
                         if (bq[i]<=b[0].substr(0,4))
                         {
                             bc++;
                             bq.erase(bq.begin()+i);
                             i--;
                         }
                     }
                     bc--;
                     if (bc<0) { bst++; bc++; }
                     te=b[0].substr(5,4);
                     t1=(te[0]-'0')*1000+(te[1]-'0')*100+(te[2]-'0')*10+te[3]-'0'+t;
                     te[3]=t1%10+'0'; t1/=10; 
                     te[2]=t1%10+'0'; t1/=10;
                     te[1]=t1%10+'0'; t1/=10;
                     te[0]=t1+'0';
                     aq.push_back(te);
                     b.erase(b.begin());                     
                 }
        }
        fout << "Case #" << j << ": " << ast << " " << bst << "\n";
    }
    fin.close();
    fout.close();
    return 0;
}
