#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
using namespace std;
int main()
{
    
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,f,N=1,n;
    char c;
    cin>>t;
    while(t--)
    {
              vector<int>O,B;
              vector<pair<char,int> >seq;
              int o=0,b=0,po=1,pb=1;
       cin>>f;
       while(f--)
       {
           cin>>c>>n;
           seq.push_back(make_pair(c,n));
           if(c=='O')
                     O.push_back(n);
           else
                     B.push_back(n);
       }  
           int i,j=0;     
           for(i=1;;++i)
           {
                   if(j>=seq.size()||(o>=O.size()&&b>=B.size())) break;
                   if(seq[j].first=='O')
                   {
                                        if(po<seq[j].second)
                                        po++;
                                        else if(po>seq[j].second)
                                        po--;
                                        else
                                        {
                                            o++;j++;
                                        }
                                        if(b<B.size()){
                                        if(B[b]>pb)pb++;
                                        else if(B[b]<pb)pb--;}
                   }
                   else
                   {
                                        if(pb<seq[j].second)
                                        pb++;
                                        else if(pb>seq[j].second)
                                        pb--;
                                        else
                                        {
                                            b++;j++;
                                        }
                                        if(o<O.size()){
                                        if(O[o]>po)po++;
                                        else if(O[o]<po)po--;}
                   }
           }
       cout<<"Case #"<<N++<<": "<<i-1<<endl;
    }
}  
                     
                     
                     
