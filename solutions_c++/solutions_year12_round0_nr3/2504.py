#include <iostream>
#include <fstream>
#include <math.h>
#include <set>

using namespace std;

int digits(int n)
{
    if(n<10) return 1;
    return (digits(n/10)+1);
}

int tiz(int k)
{
    if(k==0) return 1;
    return 10*tiz(k-1);
}
int shift(int n,int k,int d)
{
    int x = n / tiz(k);
    int y = n % tiz(k);
    return (tiz(d-k)*y+x);
}

bool rec(int i,int j)
{
    int d=digits(i);
    for(int k=1;k<d;k++)
    {
        if(shift(i,k,d)==j) return true;
    }
    return false;
}
int main()
{
    ifstream be("jam.be");
    ofstream ki("jam.ki");
    int t;
    be>>t;
    //cout<<shift(99888,4,5);
    for(int testcase=1;testcase<=t;testcase++)
    {
        int a,b;
        be>>a>>b;
        int db=0;
        for(int i=a;i<=b;i++)
        {
            int d=digits(i);
            set<int> r;
            for(int k=1;k<d;k++)
            {
                int s=shift(i,k,d);
                if(a<=s && s<=b && i<s) r.insert(s);
            }
            db+=r.size();
            //ki<<i<<" "<<r.size()<<endl;
        }
        ki<<"Case #"<<testcase<<": "<<db<<endl;
    }
    be.close();
    ki.close();
    return 0;
}
