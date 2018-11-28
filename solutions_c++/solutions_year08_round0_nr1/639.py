#include <iostream>
#include <string>
#include <map>
#include <stdlib.h>

using namespace std;

int main()
{
    int N,S,Q;
    char tp[101];
    int cnt[101];
    int idx=0;
    int k;
    map<string,int> search;
    cin.getline(tp,101);
    N = atoi(tp);
    for(int i=1;i<=N;i++)
    {
        memset(cnt,0,sizeof(int)*101);
        search.clear();
        idx=0;
        cin.getline(tp,101);
        S = atoi(tp);
        for(int j=0;j<S;j++)
        {
            cin.getline(tp,101);
            search[tp] = j+1;
        }
        cin.getline(tp,101);
        Q = atoi(tp);
        for(int j=0;j<Q;j++)
        {
            cin.getline(tp,101);
            if(search.count(tp)>0)
            {
                k = search[tp];
                if(cnt[k]==idx)
                {
                    cnt[k]++;
                    cnt[0]++;
                    if(cnt[0]==S)
                    {
                        cnt[k]++;
                        cnt[0]=1;
                        idx++;
                    }
                }
            }
        }
        cout<<"Case #"<<i<<": "<<idx<<endl;
    }
    //system("PAUSE");
}