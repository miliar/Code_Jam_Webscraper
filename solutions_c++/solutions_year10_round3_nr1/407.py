#include <iostream>
#include <utility>
#include <algorithm>

#define MAX 1010

using namespace std;
typedef pair<int,int> wire;

wire Tab[MAX]={};

bool intersects(const wire& A, const wire& B)
{    
    return ((B.first<A.first && B.second>A.second) || (B.first>A.first && B.second<A.second));
}

int main()
{
    ios_base::sync_with_stdio(0);
    
    int T;
    cin>>T;
    for (int c=1; c<=T; ++c)
    {
        int N,licznik=0;
        cin>>N;
        for (int i=1; i<=N; ++i)
        {
            cin>>Tab[i].first>>Tab[i].second;
            for (int j=1; j<i; ++j) if (intersects(Tab[i],Tab[j])) ++licznik;
        }
        cout<<"Case #"<<c<<": "<<licznik<<endl;
    }
    return 0;
}
