#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main()
{
    vector<int> S[5000];
    int L,D,N;
    string b;
    cin >> L >> D >> N;
    for(int i=0;i<D;i++)
    {
            cin >> b;
            S[i].resize(L,0);
            for(int j=0;j<L;j++)
                    S[i][j]|= 1<<(b[j]-'a');            
    }
    for(int i=0;i<N;i++)
    {
            cin >> b;
            vector<int> zap(L,0);
            int it=0;
            for(int j=0;j<L;j++,it++)            
                    if(b[it]!='(')
                                  zap[j]|= 1<<(b[it]-'a');
                                  else
                                  while(b[++it]!=')')
                                    zap[j]|= 1<<(b[it]-'a');
            int res=0;
            for(int k=0;k<D;k++)
            {
                    bool ok=true;
                    for(int j=0;j<L;j++)
                            if(((S[k][j])&(zap[j]))==0)
                                                 ok=false;
                    if(ok) res++;
            }
            cout << "Case #" <<i+1 <<": " << res << endl;
            
    }
    return 0;
}
