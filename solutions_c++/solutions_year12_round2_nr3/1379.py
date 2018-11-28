#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int T,N,S[1000];
FILE *in = fopen ("C.in","r");
FILE *out = fopen ("C.out","w");
bool us[50]={false};
vector <vector<int> > v;
bool f;

void sol(int ind,int sum)
{
     int i;
     //cout << ind << " " << sum << endl;
     if (ind==N)
     {
         if (v[sum].size()!=0&&!f)
         {
             f=1;
             for (i=0;i<v[sum].size()-1;i++)
                 fprintf (out,"%d ",v[sum][i]);
             fprintf (out,"%d\n",v[sum][i]);
             int l=-1;
             for (i=0;i<N;i++)
                 if (us[i])
                 {
                    if (l==-1)
                    {
                       l=S[i];
                       continue;
                    }
                    fprintf (out,"%d ",l);
                    l=S[i];
                 }
             fprintf (out,"%d\n",l);
             return;
         }
         for(i=0;i<N;i++)
            if (us[i])
               v[sum].push_back(S[i]);
         return;
     }
     sol(ind+1,sum);
     if (f)
        return;
     us[ind]=1;
     sol(ind+1,sum+S[ind]);
     us[ind]=0;
     return;
}

int main()
{

    fscanf (in,"%d",&T);

    for (int c=1;c<=T;c++)
    {
        fscanf (in,"%d",&N);
        for (int i=0;i<N;i++)
            fscanf (in,"%d",&S[i]);
        v.clear();
        v.resize(2000010);
        f=0;
        fprintf (out,"Case #%d:\n",c);
        sol (0,0);
        if (!f)
           fprintf (out,"Impossible\n");
    }

    return 0;
}
