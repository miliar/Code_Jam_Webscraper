#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <list>
#include <vector>
#include <deque>
#include <functional>

#define pii 2*acos(0)
#define max 100

using namespace std;

int main()
{
    //vector<double> v;
    deque<double> ilist,ilist2;
    //deque<double> ideq;
    int a,b,c,d,e,i,j,k,l,m,n,tcount,fcount,f,t,ans[100],count,x,y;
    //char ch[max];
    //string str[max];
   // cout<<setprecision(10)<<pii;
    ifstream infile("C-small-attempt1.in");
    infile>>t;
    for (i=0;i<t;i++)
    { fcount=0;
      count=0;
      infile>>a>>b;
      x=a;
      y=b;
      //cout<<a<<" "<<b<<endl;
      for (n=a;n<b;n++)
      {
          for (m=n+1;m<=b;m++)

          {   //cout<<n<<" "<<m<<"|";
              count=0;
              e=0;
              x=n;
              y=m;
              for (j=10;;)
      {
          ilist.push_front(x%j);
          ilist2.push_front(y%j);
          count++;
          //cout<<ilist.front()<<"v"<<ilist2.front()<<"|";
          x/=j;
          y/=j;
          //j*=10;
          if (x==0||y==0)break;
      }
      //if (n==12&&m==21)
      //cout<<"<<33";
              for (c=count-1;c>0;c--)
              {   tcount=0;
                  d=ilist[count-1];
                  ilist.pop_back();
                  ilist.push_front(d);
                  for (e=0;e<count;e++)
                  {
                      if (ilist[e]==ilist2[e])
                      tcount++;
                  //    cout<<ilist[e]<<ilist2[e]<<" ";
                  }
                  if (tcount==count)
                  {fcount++;
                  //cout<<n<<" "<<m<<endl;
                  //for (e=0;e<count;e++)
                  //cout<<ilist[e]<<" "<<ilist2[e]<<endl;
                  break;}
              }
          }
      }
      ans[i]=fcount;
    }
    infile.close();
    ofstream outfile("o2.out");
    for (i=0;i<t;i++)
    {
      outfile<<"Case #"<<i+1<<": "<<ans[i];
       if (i!=t-1)
       {
           outfile<<endl;
       }
    }
    return 0;
}
