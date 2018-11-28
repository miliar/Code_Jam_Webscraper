#include<iostream>
using namespace std;
int n;
int main()
{
    int x,k;
    cin >> n;
    for(int i =1; i <= n;i++)
    {
        cin >>x>>k;
        int t = 1 <<(x);
        cout << "Case #"<<i<<": ";
        if(k ==0){
            cout << "OFF" << endl;
            continue;
        }
        
        if(k % t == t-1)
            cout << "ON";
        else
            cout << "OFF";
        cout << endl;
    }
}
