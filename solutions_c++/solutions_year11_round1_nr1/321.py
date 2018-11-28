#include <iostream>
using namespace std;
int tn,t;
long long n,pd,pg;

long long gcd(long long a,long long b)
{
    if (a<b)
       swap(a,b);
    if (b==0)
       return a;
    return gcd(b,a%b);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    cin >> tn;
    for (t=1;t<=tn;t++)
    {
        cin >> n >> pd >> pg;
        if (pg==100 && pd!=100)
        {
           cout << "Case #" << t << ": Broken" << endl;
           continue;
        }
        if (pg==0 && pd!=0)
        {
           cout << "Case #" << t << ": Broken" << endl;
           continue;
        }      
        
        long long a= 100/gcd(pd,100);
        if (a<=n)
        {
            cout << "Case #" << t << ": Possible" << endl;
        }
        else
        {
            cout << "Case #" << t << ": Broken" << endl;
        }
    }
}
