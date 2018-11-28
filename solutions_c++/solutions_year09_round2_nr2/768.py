#include<algorithm>
#include<cstdio>
#include<iostream>
#include<map>
#include<stack>
#include<string>
#include<vector>
#include<queue>
using namespace std;
int main()
{
     int T;
     string N;
    cin >> T;
    for(int te=1;te<=T;te++)
    {
            vector<int> V;
            
            cin >> N;
            V.push_back(0);
            for(int i=0;i<N.size();i++)
                    V.push_back(N[i]-'0');
            next_permutation(V.begin(),V.end());
            cout << "Case #"<<te<<": ";
            if(V[0]) cout << V[0];
            for(int i=1;i<V.size();i++)
                    cout << V[i];
            cout<<endl;
    }
    return 0;
}
