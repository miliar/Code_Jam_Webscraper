#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<map>

using namespace std;

int main()
{
    int t, count;
    cin >> t;
    count=0;
    int n;
    long long l, h;
    long long f[10000];
    while (count<t)
    {
        count++;
        cout << "Case #" << count << ": ";
        cin >> n >> l >> h;
        for (int i=0; i<n; i++)
        {
            cin >> f[i];
        }
        bool found=false;
        
        for (int i=l; i<=h; i++)
        {
            bool T=true;
            for (int j=0; j<n; j++)
                if (f[j]%i!=0 && i%f[j]!=0 ) 
                { T=false;break;}
            if (T)
            {
                found=true;
                cout << i <<endl; 
                break;
            }            
        }
        if (!found)
            cout << "NO" << endl;

    }

}
