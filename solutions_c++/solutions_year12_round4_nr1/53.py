#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string tst()
{
    int n;
    cin >> n;
    vector<int> l(n),d(n);
    for(int i=0;i<n;i++)
        cin >> d[i] >> l[i];
    int L;
    cin >> L;
    n++;
    d.push_back(L);
    l.push_back(0);
    vector<int> bhold(n,-1);
    bhold[0] = d[0];
    int j=1;
    for(int i=0;i<n;i++)
    {
        if(bhold[i]<0)
            return "NO";
        while(j<n && d[j]<=bhold[i]+d[i])
        {
            bhold[j] = min(l[j], d[j]-d[i]);
            j++;
        }
    }
    if(bhold[n-1]>=0)
        return "YES";
    else
        return "NO";
}

int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        cout << "Case #"<< i <<": " << tst() << endl;
    }
}
