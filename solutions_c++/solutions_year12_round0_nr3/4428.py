#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int pw[4] = {1,10,100,1000};
bool check(int x, int y)
{
    int lx = ceil(log10((double)x));
    int ly = ceil(log10((double)y));
    if(lx != ly)
    {
        return false;
    }
    int i;
    for( i = 1; i < lx; i++)
    {
        int k = (x % pw[i])*pw[lx-i] + x / pw[i];
        if( k == y)
            return true;
    }
    return false;
    
}

int main()
{
    int i,j;
    vector<pair<int,int> > p;
    for(i = 1; i <= 1000; i++)
        for(j = i+1; j <= 1000; j++)
            if(check(i,j))
            {
                p.push_back(make_pair(i,j));
                
            }

    int u;
    cin >> u;

    for(j = 1; j <= u; j++)
    {
        int a,b;
        cin >> a >> b;
        
        int c = 0;
        for(i = 0; i < (int)p.size(); i++)
            if(p[i].first >= a && p[i].second <= b)
                c++;
        cout << "Case #" << j << ": " << c << "\n";
    }
    
    return 0;
}
