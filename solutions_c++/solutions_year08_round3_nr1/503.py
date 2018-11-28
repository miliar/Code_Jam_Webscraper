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


int main()
{
   // clrscr();
    fstream fin("A-large(2).in");
    long long i,j,q,w,n,p,k,l,t,x;
    vector <int> freq, tt;
    vector <vector <int> > ar;
    fin>>n;
    for(i=0;i<n;i++)
    {
                    fin>>p>>k>>l;
                    freq.resize(0);
                    tt.resize(0);
                    ar.resize(0);
                    for(j=0;j<l;j++)
                    {
                                    fin>>t;
                                    freq.push_back(t);
                    }
                    sort(&freq[0],&freq[freq.size()]);
                    if(l>p*k)
                             goto nope;
                    t=0;
                    w=0;
                    x=0;
                    for(j=0;j<p;j++)
                                    tt.push_back(-1);
                    for(j=0;j<k;j++)
                                    ar.push_back(tt);
                    x=0; 
                    for(j=freq.size()-1;j>=0;j--)
                    {
                            ar[w][t]=freq[j];
                            x+=freq[j]*(t+1);
                            w++;
                            if(w==ar.size())
                            {
                                            w=0;
                                            t++;
                            }
                            //cout<<x<<" "<<freq[j]*(t+1)<<" "<<freq[j]<<" "<<w<<" "<<t<<endl;
                            
                    }
                    t=0; /*
                    for(j=0;j<ar.size();j++)
                    {
                                               for(p=0;p<ar[0].size();p++)
                                                                          cout<<ar[j][p]<<" ";
                                               cout<<endl;
                    } */
                    goto yeah;
                    nope:
                    cout<<"Case #"<<i+1<<": "<<"Impossible"<<endl;     
                    continue;
                    yeah:  
                    cout<<"Case #"<<i+1<<": "<<x<<endl;          
    }
    getch();
    return 1;  
}
