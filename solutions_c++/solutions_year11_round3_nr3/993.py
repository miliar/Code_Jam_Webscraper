#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
const int N = 10000;
int a[N];
int n, l, h;
bool yes(int x)
{
    for(int i=0;i<n;i++)
    {
        if (x > a[i]) {
            if (x % a[i] != 0) 
                return false;
        }
        else if(a[i]%x!=0) return false;
    }
    return true;
}

int main(){
    int Tcase;
    cin>>Tcase;
    for(int t=1;t<=Tcase;t++)
    {
        cin >> n >> l >> h;
        for(int i=0;i<n;i++)
            cin>>a[i];
        printf("Case #%d: ", t);
        bool flag=true;
        for(int i=l;i<=h;i++)
        {
            if(yes(i))
            {
                flag=false;
                cout<<i<<endl;
                break;
            }
        }
        if(flag)
            cout<<"NO"<<endl;
    }
}

