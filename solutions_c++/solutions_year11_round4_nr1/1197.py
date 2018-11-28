#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <iomanip>

using namespace std;

int binsearch(long* tab, int n, long a) {
    int l = 0;
    int r = n - 1;
    while (l < r){
        int s = (l + r)/2;
        if (a < tab[s])
            r = s;
        else
            l = s + 1;
    }
    return l;
}
struct Pair{
    int x,y;
};

bool op(Pair A, Pair B){
    return A.x > B.x;
}



int main()
{
    int t;
    cin >> t;
    cout.precision(6);           // no decimal place
    cout.setf(ios::fixed);
    for(int j = 0; j < t; j++){

        long double time = 0;
        int x, s, r, t, n;
        scanf(" %d%d%d%d%d", &x, &s, &r, &t, &n);
        vector < Pair > pv;
        int walkaways = 0;
        for(int i = 0; i < n; i++){
            int a, b, v;
            scanf("%d%d%d", &a, &b, &v);
            Pair temp;
            temp.x = v;
            temp.y = b - a;
            pv.push_back(temp);
            walkaways += temp.y;
        }
        Pair ostat;
        ostat.x = 0;
        ostat.y = x - walkaways;
        pv.push_back(ostat);
       // cout << pv[n].y << endl;

        sort(pv.begin(), pv.end(), op);
        //for(int i = n; i >= 0; i--){
        //    cout <<"v = " << pv[i].x << " droga " << pv[i].y<<endl;
        //}
        cout << "Case #" << j + 1 <<": ";
        long double timeleft = t;
        for(int i = n; i >= 0; i--){
            Pair temp = pv[i];
            int vAkt = r + temp.x;
            long double actual = (long double)temp.y / (long double)vAkt;
            if ( actual <= timeleft){
                timeleft -= actual;
                time += actual;
            } else{
                long double diff = actual - timeleft;
                long double runned = timeleft * vAkt;
                time += timeleft;
                timeleft = 0;
                time += (long double)(temp.y - runned)/ (long double)(s + temp.x);
            }
        }

    cout << time << endl;
    }
    return 0;
}
