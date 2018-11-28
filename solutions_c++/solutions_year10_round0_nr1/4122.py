#include <cstdlib>
#include <iostream>

using namespace std;

int power(int a, int b)
{
     int c=a;
     for (int n=b; n>1; n--) c*=a;
     return c;
}

int main(int argc, char *argv[])
{
    int n;
    cin >> n;
    
    int num[n], click[n];
    
    for(int i=0;i<n;i++)
    {
        cin >> num[i] >> click[i];      
    }
    
    for(int i=0;i<n;i++)
    {
            int a = power(2,num[i])-1;
            int b = click[i]%(power(2,num[i]));
            //cout << a << " " << b;
            if(a==b)
                cout << "Case #" << i+1 << ": " << "ON" << endl;
            else
                cout << "Case #" << i+1 << ": " << "OFF" << endl;           
    }
}
