#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<fstream>
 
using namespace std;
 
bool check(int a,int b)
{
    if(a==b)
        return true;
    list<int> la,lb;
    vector<int> tmp(10,0);
    int t1,t2;
    while(a>9 && b>9)
    {
        t1=a%10;
        a=a/10;
        t2=b%10;
        b=b/10;
        la.push_front(t1);
        lb.push_front(t2);
        tmp[t1]+=1;
        tmp[t2]-=1;
    }
    if(a>9)
        return false;
    if(b>9)
        return false;
    la.push_front(a);
    lb.push_front(b);
    tmp[a]+=1;
    tmp[b]-=1;
    for(int i=0;i<10;i++)
    {
        if(tmp[i]!=0)
            return false;
    }

    int len=lb.size();
    list<int>::iterator itr1=lb.begin();
    for(int i=0;i<len;i++)
    {
        lb.push_back(*itr1);
        itr1++;
    }
    itr1=lb.begin();
    len=lb.size();
    int l2=la.size();
    list<int>::iterator itr2=la.begin();
    for(int i=0;i<len;i++)
    {
        if((*itr1)==(*itr2) && (i+l2)<=len)
        {
            list<int>::iterator itr11;
            itr11=itr1;
            int j=0;
            for(j=0;j<l2;j++)
            {
                if((*itr11)!=(*itr2))
                    break;
                itr11++;
                itr2++;
            }
            if(j==l2)
                return true;
            itr2=la.begin();
        }
        itr1++;
    }
    return false;
}

int convert(list<int> &a)
{
    int ans=0;
    int len=a.size();
    list<int>::iterator itr=a.begin();
    for(int i=0;i<len;i++)
    {
        ans*=10;
        ans+=*itr;
        itr++;
    }
    return ans;
}
 int main()
 {
     ifstream file;
     ofstream out;
     file.open("c:\\b\\input.txt");
     out.open("c:\\b\\output.txt");
     int n;
     file>>n;
     //string tmp;
     //getline(file,tmp);
     int a,b; //change for long dataset
     for(int i=0;i<n;i++)
     {
         file>>a>>b;
         int ans=0;
         for(int ii=a;ii<b;ii++)
         {
             list<int> l;
             int t1=ii,t2;
             while(t1>9)
             {
                 t2=t1%10;
                 l.push_front(t2);
                 t1=t1/10;
             }
             l.push_front(t1);
             int len=l.size();
             list<int>::iterator itr;
             for(int j=0;j<len;j++)
             {
                 t1=convert(l);
                 if(t1<=b && t1>ii)
                     ans++;
                 itr=l.end();
                 itr--;
                 t1=(*itr);
                 l.pop_back();
                 l.push_front(t1);
             }



            /* for(int jj=b;jj>ii;jj--)
             {
                 if(check(ii,jj))
                     ans++;
             }*/
         }
         out<<"Case #"<<(i+1)<<": "<<ans<<endl;
     }
     return 0;
 }