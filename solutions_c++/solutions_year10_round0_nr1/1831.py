#include<iostream>
#include<stdio.h>
using namespace std;

int main ()
{
    int t; cin >> t;
    int n, k; 
    for (int i = 1; i <= t; i++)
    {
        cin >> n >> k;
        cout << "Case #" << i << ": "; 
        if (k%(1<<n) == (1<<n)-1) cout << "ON"; else cout << "OFF";
        cout << endl; 
    }
}