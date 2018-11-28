#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int a,b,numDigits;
int power(int c,int b)
{
    int res = 1;
    for(int i=1;i<=b;i++)
    {
            res = res * c;
            }
    return(res);
}
int value(int a,int j)
{
    vector<int>temp;
    temp.clear();
    int x = 0;
    while(a != 0)
    {
            x = a % 10;
            temp.push_back(x);
            a = a / 10;  
            }
    reverse(temp.begin(),temp.end());
    int sum = 0;
    int c = numDigits-1;
    int k = j;
    for(int d = 0; d < numDigits;)
    {
            sum += power(10,c--) * temp[k];
            k = (k + 1) % numDigits;
            d++;
            }
    return sum;
}
int main()
{
    ofstream fout("out.in");
    ifstream fin("in.in");
    int t;
    fin>>t;
    int test = 1;
    while(test <= t)
    {
               fin>>a>>b;
               //fout<<a<<b<<"\n";
               int numRecycled = 0;
               for(int i=a;i<=b;i++)
               {
                       int x = i;
                       numDigits = 0;
                       while(x!=0)
                       {
                                  x = x / 10;
                                  numDigits++;
                                  }
                       for(int j=1;j<numDigits;j++)
                       {
                               int ans = value(i,j);
                               if(value(i,j) >= a && value(i,j) <= b)
                               {
                                             if(i < ans)
                                              {
                                               numRecycled++;
                                               //fout<<"i "<<i<<" ans "<<ans<<"\n";
                                               }
                                              }

                               }
                       }

               fout<<"Case #"<<test<<": "<<numRecycled<<"\n";
               test++;
               }
}
