#include<iostream>
#include <vector>
#include <algorithm>
#include<fstream>
using namespace std;
int no_of_dig(int n)
{
    int c=0;
    if (n==0)return 1;
    while(n)
    {
        c++;
        n/=10;
    }
    return c;
}
int check(int a,int b)
{
     int f=a;
     vector<int> myvector;
     vector<int> myvector1;
     int d=no_of_dig(a);
     int c=0,i,j;
     for(i=0;i<d;i++)
     {
         myvector1.push_back(a%10);
         a/=10;
      //  cout<<myvector1[i]<<" "<<a<<" ";

     }
     reverse(myvector1.begin(),myvector1.end());
     int temp[10]={0};
     int k=0,l;
     for(i=1;i<d;i++)
     {
          myvector=myvector1;
          rotate(myvector.begin(),myvector.begin()+i,myvector.end());
          if(myvector[0]==0) continue;

          for(j=0;j<d;j++)
          {
              temp[k]=temp[k]*10;
              temp[k]=(myvector[j])+temp[k];

          }
          if(temp[k]<=b&&temp[k]>f)
          {
              int usable=1;
              for(l=0;l<k;l++)
              {
                  if(temp[k]==temp[l])
                  {
                    usable=0;
                    break;
                  }
              }
              if(usable)
              c++;
          }

          k++;
          //cout<<temp<<" "<<f<<" "<<b<<" "<<c<<endl;
        }
     return c;
}

main()
{
    int i,a,b,t,j=0;
    ifstream in;
    ofstream out;
    in.open("in_c.txt");
    out.open("out_c.txt");
    in>>t;
    while(t--)
    {
        j++;
        int count=0;
        in>>a>>b;
        for(i=a;i<=b;i++)
        {
            count+=check(i,b);
           // cout<<"count="<<count<<endl;
        }
        out<<"Case #"<<j<<": "<<count<<endl;
    }
    in.close();
    out.close();
}
