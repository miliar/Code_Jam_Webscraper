#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>
using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
};

long long gcd(long long arr[], int n) {
    long long temp = arr[0];
    for (int i = 1; i < n; i++) {
        temp = gcd(temp, arr[i]);
    }
    return temp;
}

int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int m;
        long long arr[1400];
        cin >> m;
        for (int j = 0; j < m; j++) {
            cin >> arr[j];
        }
        sort(arr, arr+m);
        long long arr2[100000];
        int l = 0;
        for (int j = m-1; j >=0; j--) {
            for (int k = j-1; k >= 0; k--) {
                arr2[l++] = arr[j]-arr[k];
            }
        }
        long long T = gcd(arr2, l);
        long long ans = (ceil((double)arr[0] / T))*T - arr[0];
        cout << "Case #" << i+1 << ": " << ans << endl;
        //cout << "Divisor: " << divisor << endl;
        //cout << "Case #" << i+1 << ": " << (remainder-divisor) << endl;
        /*long long remainder = gcd(arr, m);
        for (int j = 0; j < m; j++) {
            arr[j] -= remainder;
        }
        long long divisor = gcd(arr, m);
        long long ans = divisor - remainder;
        cout << "Case #" << i+1 << ": " << ans << endl;*/
        /*int greatest = -1;
        int inc = 0;
        for (int k = 0; k < 100000000; k++) {
            long long common = gcd(arr, m);
            if (common > greatest) {
                greatest = common;
                inc = k;
            }
            for (int j = 0; j < m; j++)
                arr[j]++;
        }
        cout << "Case #" << i+1 << ": " << inc  << "  greatest: " << greatest << endl;*/
    }
}