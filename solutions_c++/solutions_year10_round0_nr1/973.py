#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

bool my_snapper(int n,int k)
{
    int base=1;
    for(int i=0;i<n;i++)
       base*=2;
    if((k+1)%base==0)
       return true;
    else
       return false;

 /*   for(int i=0;i<n;i++)
    {

        if(k%2==0)
        return false;
        k/=2;
        }
        return true;
        */
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
