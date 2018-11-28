#include<iostream>
using namespace std;

int a[20],b[20];

int main()
{
    freopen("2.in","rt",stdin);
    freopen("2.out","wt",stdout);    
    int n,k,t;
    cin >> t;
    for(int numt = 0; numt < t; numt++)
    {
           cout <<"Case #" << numt + 1<< ": ";
           cin >> k >> n;
           n %= (1<<k);        
           if ( n == ((1<<k) - 1) ) cout <<"ON";
           else cout <<"OFF";
           cout << endl;
    }
   /*
    int n,k;
    cin >> n >> k;
    for(int i = 0; i < k; i++)
    {
            char ch;
            for(int j = 0; j < n; j++) 
            {
                    b[j] = 1 - a[j];
                    if ( a[j] == 0 ) break;
            }
            for(int j = 0; j < n; j++) a[j] = b[j];
            for(int j = 0; j < n; j++) cout << a[j];            
            cout << endl;
    }    
    system("PAUSE");
    */
    return 0;
}
