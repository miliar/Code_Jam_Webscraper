#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
using namespace std;
typedef long long int lli;

int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int T;
    cin>>T;
    for (int t=1;t<=T;t++)
    {
        int N;
        cin>>N;
        vector<int> L(N),P(N);
        for (int i=0;i<N;i++) cin>>L[i];
        for (int i=0;i<N;i++) cin>>P[i];
        vector<pair<pair<int,int>,int> > d(N);
        for (int i=0;i<N;i++)
        {
            d[i].first=make_pair(-P[i],-L[i]);
            d[i].second=i;
        }
        sort(d.begin(),d.end());
        cout<<"Case #"<<t<<":";
        for (int i=0;i<N;i++) cout<<" "<<d[i].second;
        cout<<endl;
    }
}

