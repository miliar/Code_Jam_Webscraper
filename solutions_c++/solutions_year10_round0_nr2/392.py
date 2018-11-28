#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int n_temp[1000];
int gcd(int a,int b)
{
    while(b!=0)
    {
        a=a%b;
        swap(a,b);
        }
        return a;
}
int my_deal(vector<int>& vec_value,int n)
{
    sort(vec_value.begin(),vec_value.end());
    for(int i=0;i<n-1;i++)
    {
       n_temp[i]=vec_value[i+1]-vec_value[0];
       cout<<n_temp[i]<<endl;
    }
    n--;
    while(n>1)
    {
        for(int i=0;i<n;i+=2)
        {
            if(i+1>=n)
               n_temp[i/2]=n_temp[i];
            else
               n_temp[i/2]=gcd(n_temp[i],n_temp[i+1]);

        }
        n=(n+1)/2;
        }
        if(vec_value[0]%n_temp[0]==0)
        return 0;
        else
    return n_temp[0]-vec_value[0]%n_temp[0];

}
int main()
{
   // ifstream in("A-large.in");
    ifstream in("a.in");
    ofstream out("a.out");
    int c=0,n=0;
    in>>c;
    for(int i=1;i<=c;i++)
     {
         vector<int> vec_value;
         int temp=0;
         in>>n;
         for(int j=0;j<n;j++)
         {
            in>>temp;
            vec_value.push_back(temp);
         }
         temp=my_deal(vec_value,n);
         out<<"Case #"<<i<<": "<<temp<<endl;
      }

    return 0;
}
/*
bool my_snapper(int n,int k)
{
    int base=1;
    for(int i=0;i<n;i++)
       base*=2;
    if((k+1)%base==0)
       return true;
    else
       return false;

}
int main()
{
    ifstream in("A-large.in");
    //ifstream in("a.in");
    ofstream out("a.out");
    int t=0,n=0,k=0;
    in>>t;
    for(int i=1;i<=t;i++)
    {
        in>>n>>k;
        if(my_snapper(n,k))
           out<<"Case #"<<i<<": ON"<<endl;
        else
           out<<"Case #"<<i<<": OFF"<<endl;
    }

    return 0;
}
*/
