#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool verify(vector<int> v)
{
    int n = v.size()+1;
    v.push_back(n);
    vector<int> s;
    for(int i=0;i<n;i++)
    {
        while(!s.empty() && s.back()==i)
            s.pop_back();
        if(v[i]<=i)
            return false;
        if(!s.empty() && s.back()<v[i])
            return false;
        s.push_back(v[i]);
    }
    return true;
}

void tst()
{
    int n;
    cin >> n;
    vector<int> next(n-1);
    for(int i=0;i<n-1;i++)
    {
        cin >> next[i];
        next[i]--;
    }
    if(!verify(next))
    {
        cout << " Impossible";
        return;
    }
    vector<int> dep(n,0);
    vector<int> pos(n,0);
    for(int i=n-2;i>=0;i--)
    {
        int j = next[i];
        dep[i] = dep[j]+1;
        pos[i] = pos[j]+(j-i)*dep[j]+1;
    }
    int mm = 0;
    for(int i=0;i<n;i++)
        mm = max(mm,pos[i]);
    for(int i=0;i<n;i++)
        pos[i] = mm-pos[i];
    for(int i=0;i<n;i++)
        cout << ' ' << pos[i];
}

int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        cout << "Case #"<< i <<":";
        tst();
        cout << endl;
    }
}
