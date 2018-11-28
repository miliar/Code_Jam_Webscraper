#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct data
{
    int id;
    long long f;
}
temp;

bool cmp(data a, data b) { return a.f > b.f; }

long long check(vector <data> v, int k, int p)
{
    long long press = 0;
    long long level = 1;
    int space = k;
    
    for(int i=0; i<v.size(); i++)
    {
        if(space == 0) level ++, space = k;
        if(level > p) return -1;
        press += v[i].f * level;
        space --;
    }
    
    return press;
}

int main()
{
    freopen("A.in","r", stdin); freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int T=1; T<=t; T++)
    {
        int p, k, l;
        cin >> p >> k >> l;
        int letter[1000];
        vector <data> v;
        for(int i=0; i<l; i++)
        {
            cin >> temp.f;
            temp.id = i;
            v.push_back(temp);
        }
        sort(v.begin(), v.end(), cmp);
        printf("Case #%d: %I64d\n", T, check(v,k,p));
    }
}
