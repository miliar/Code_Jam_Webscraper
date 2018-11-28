#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
int n;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,tci,tc,res,n,k,x,y,bt,ot,bp,op,movetime;
    vector<pair<char,int> > data;
    pair<char,int> temp;
    char t;
    cin >> tc;
    for (tci = 1;tci <= tc;++tci)
    {
        cin >> n;
        data.clear();
        res = bt = ot = 0;
        bp = op = 1;
        for (i = 0;i < n;++i)
        {
            cin >> temp.first;
            cin >> temp.second;
            data.push_back(temp);
        }
        for (i = 0;i < n;++i)
        {
            if (data[i].first == 'O')
            {
                movetime = abs(data[i].second - op);
                movetime -= bt;
                bt = 0;
                if (movetime < 0) movetime = 0;
                ++movetime;
                res += movetime;
                ot += movetime;
                op = data[i].second;
            }
            else
            {
                movetime = abs(data[i].second - bp);
                movetime -= ot;
                ot = 0;
                if (movetime < 0) movetime = 0;
                ++movetime;
                res += movetime;
                bt += movetime;
                bp = data[i].second;
            }
        }
        cout << "Case #" << tci << ": " << res << endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
