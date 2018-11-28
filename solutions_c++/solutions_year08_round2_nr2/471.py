#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <sstream>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
#include <conio.h>
#include <fstream>


using namespace std;

int isprime(int x)
{
    int i;
    for(i=2;i<x/2+1;i++)
                        if(x%i==0)
                                  return 0;
    return 1;
}
int main()
{
   // clrscr();
    fstream fin("B-small-attempt0(2).in");
    int n,a,b,p,i,j,k,m,q,jj,kk,ff;
    vector <int> primes,grp1,grp2;
    vector <vector <int> > g1,g2;
    for(i=2;i<1010;i++)
                       if(isprime(i)==1)
                                        primes.push_back(i);
    fin>>n;
    for(i=0;i<n;i++)
    {
                    fin>>a>>b>>p;
                    for(j=0;j<primes.size();j++)
                                                if(primes[j]>b)
                                                               break;
                    q=j-1;
                    if(q==primes.size()-1)
                                        q--;
                    g1.resize(0);
                    g2.resize(0);
                    for(j=a;j<=b;j++)
                    {
                                     grp1.resize(0);
                                     grp2.resize(0);
                                     grp1.push_back(j);
                                     for(k=0;k<q;k++)
                                     {
                                                     if(primes[k]>j)
                                                                    break;
                                                     if(j%primes[k]==0)
                                                                       grp2.push_back(primes[k]);
                                     }
                                     g1.push_back(grp1);
                                     g2.push_back(grp2);
                    }
                    while(1)
                    {
                            m=1;
                            for(j=0;j<g1.size();j++)
                            {
                                                    if(g1[j].size()==0)
                                                                       continue;
                                                    for(k=0;k<g1.size();k++)
                                                    {
                                                                            if(j==k)
                                                                                    continue;
                                                                            ff=0;
                                                                            for(jj=0;jj<g2[j].size();jj++)
                                                                            {
                                                                            for(kk=0;kk<g2[k].size();kk++)
                                                                            {
                                                                            if(g2[j][jj]==g2[k][kk] && g2[j][jj]>=p)
                                                                            {
                                                                            ff=1;break;
                                                                            }
                                                                            }
                                                                            if(ff==1) break;
                                                                            }
                                                                            if(ff==1)
                                                                            {
                                                                                     m=0;
                                                                                     for(kk=0;kk<g2[k].size();kk++)
                                                                                     {
                                                                                     g2[j].push_back(g2[k][kk]);
                                                                                     }
                                                                                     for(kk=0;kk<g1[k].size();kk++)
                                                                                     {
                                                                                     g1[j].push_back(g1[k][kk]);
                                                                                     }
                                                                                     g2[k].resize(0);
                                                                                     g1[k].resize(0);
                                                                                     
                                                                            }
                                                    }   
                                                                         
                            }
                            if(m==1)
                                    break;
                    }
                    k=0;
                    for(j=0;j<g1.size();j++)
                                            if(g1[j].size()>0)
                                                              k++;
                    /* for(j=0;j<g1.size();j++)
                    {
                                            for(m=0;m<g1[j].size();m++)
                                                                       cout<<g1[j][m]<<" ";
                                            cout<<" :: ";
                                            for(m=0;m<g2[j].size();m++)
                                                                       cout<<g2[j][m]<<" ";
                                            cout<<endl;
                    } */
                    cout<<"Case #"<<i+1<<": "<<k<<endl;               
    }
    getch();
    return 1;  
}
