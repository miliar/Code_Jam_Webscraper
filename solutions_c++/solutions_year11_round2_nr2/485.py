#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

int n;
double mindist;
vector <double> pos;

bool able(double r)
{
    double lef = -1000000001;
    for(int i = 0 ; i < pos.size() ; i++)
    {
        double L = pos[i] - r;
        double R = pos[i] + r;
        L = max(L , lef);
        if(L > R)
            return false;
        lef = L + mindist;
    }
    return true;
}

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    ios :: sync_with_stdio(false);
    int TestCase;
    cin >> TestCase;
    for(int CaseID = 1 ; CaseID <= TestCase ; CaseID ++)
    {
        pos.clear();
        int diffpos;
        cin >> diffpos >> mindist;
        for(int i = 1 ; i <= diffpos ; i++)
        {
            long long p , amount;
            cin >> p >> amount;
            for(int j = 1 ; j <= amount ; j++)
                pos.push_back((double)p);
        }
        sort(pos.begin() , pos.end());
        double L = -1 , R = 100000000 , M;
        while(R - L > 1e-7)
        {
            M = (L + R) * 0.5;
            if(able(M))
                R = M;
            else
                L = M;
        }
        cout << "Case #" << CaseID << ": " << R << endl ;
    }
    return 0;
}
