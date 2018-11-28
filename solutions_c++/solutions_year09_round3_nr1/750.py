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
    cin >> T;
    for(int te=1;te<=T;te++)
    {
        string L;
        map<char,int> M;
        cin >> L;
        int w=1;
        unsigned long long res=0;
        for(int i=0;i<L.size();i++)
            if(M[L[i]]==0) M[L[i]] = w++;
        if(w>2) w--;
        
        for(int i=0;i<L.size();i++)
        {
            res*=w;
            if(M[L[i]]==1) res+=1; else if (M[L[i]]!=2) res+=(M[L[i]]-1);
        }
        cout << "Case #"<<te<<": "<< res << endl;
    }


    return 0;
}
