#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

char ctonum[256][5];
int ctodig[256];
int main()
{
    ifstream in("B-large.in");
    ofstream out("ans.out");
    int t;
    in >> t;
    for(int i=0; i<t; i++){
        int n, s, p;

        cout << "Case #" << i+1 << endl;
        out << "Case #" << i+1 << ": ";
        in >> n >> s >> p;
        int d[n];
        for(int j=0; j<n; j++)
            in >> d[j];

        int puedenser=0;
        int ans=0;
        for(int j=0; j<n; j++){
            if(d[j]%3==0 && d[j]/3 >=p)
                ans++;
            else if(ceil(d[j]/3.)>=p)
                ans++;
            else if(d[j]!=0 && round(d[j]/3.)+1 >=p)
                puedenser++;
        }
        int puedenson=min(s, puedenser);
        /*for(int j=0; j<n; j++){

        }*/
        out << ans+puedenson << endl;
    }
    return 0;
}
