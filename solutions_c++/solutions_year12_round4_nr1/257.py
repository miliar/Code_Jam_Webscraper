#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
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
        vector<int> d(N),l(N);
        for (int i=0;i<N;i++)
            cin>>d[i]>>l[i];
        int D;
        cin>>D;
        int get=0;
        vector<int> jump(N,0);
        jump[0]=d[0]*2;
        for (int i=1;i<N;i++)
        {
            for (int j=0;j<i;j++)
            {
                if (jump[j]>=d[i])
                {
                   jump[i]>?=min(d[i]-d[j],l[i])+d[i];
                }
            }
        }
        cout<<"Case #"<<t<<": "<<(*max_element(jump.begin(),jump.end())>=D?"YES":"NO")<<endl;
    }
    return 0;
}
