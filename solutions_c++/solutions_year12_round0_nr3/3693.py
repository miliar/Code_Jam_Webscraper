#include <cstring>
#include <iostream>
#include <map>
#include <cstdio>
#include <set>
#include <iterator>
#include <vector>
using namespace std;

int A,B;
vector<int> arr[2000001];

void init()
{
    for(int i=1; i <= 2000000; ++i)
    {
        int t=i;
        while(t)
        {
            arr[i].push_back(t%10);
            t/=10;
        }
    }
}

int po[10]={1,10,100,1000,10000,100000,1000000,10000000};

int getInt(int a)
{
    int l1 = arr[a].size();
    set<int> s;
    for(int i = l1-1; i >= 0; --i)
    {
        int ss=0;
        int t=0;
        for(int j=i; j>=0;--j) ss+=arr[a][j]*po[l1-1-t], t++;
        for(int j=l1-1; j>i; --j) ss+=arr[a][j]*po[l1-1-t], t++;
        if(ss>a&&ss<=B)
            s.insert(ss);
        //cout << ss <<endl;
    }
    return s.size();
}

int main()
{
    init();
    //freopen("C-large.in","r", stdin);
    //freopen("C-large.out","w", stdout);
    int t;
    cin >> t;
    int ca = 0;
    while(t--)
    {
        cin >> A >> B;
        int sum = 0;
        for(int i = A; i <= B; ++i)
        {
            sum += getInt(i);
        }
        printf("Case #%d: ", ++ca);
        cout << sum << endl;
    }
    return 0;
}

