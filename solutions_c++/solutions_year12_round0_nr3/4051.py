#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int T,A,B,n;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("outputC.out","w",stdout);
    cin >> T;
    int num=0;
    while (T)
    {
        T--;num++;
        cout << "Case #" << num << ": ";
        
        cin >> A >> B;
        int tmp=A,k;
        n=0;
        while (tmp)
        {
            n++;
            tmp/=10;
        }
        int mul=1,count=0;
        for (int i=1;i<n;i++) mul*=10;
        
    //    cout << A << ' ' << B << ' '<< n << ' ' << mul << endl;
        
        for (int i=A;i<=B;i++)
        {
            tmp=i;
            for (int j=0;j<n;j++)
            {
                k=tmp%10;
                tmp=tmp/10+k*mul;
                if (tmp>i && tmp<=B) 
                {
      //              cout << i << ' ' << tmp << endl;
                    count++;
                }
            }
        }
        
        cout << count << endl;
    }
}
            
                
    
