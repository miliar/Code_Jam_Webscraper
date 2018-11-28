#include <iostream>
#include <vector>

using namespace std;

vector <string> W;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int L, D, N;
    cin>>L>>D>>N;
    
    W = vector <string> (D);
    
    for(int i=0; i<D; i++)
        cin>>W[i];
    
    for(int nCaso=1; nCaso<=N; nCaso++)
    {
        string s;
        cin>>s;
        
        int mask[L];
        memset(mask, 0, sizeof(mask));
        
        int k = 0, p = 0;
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]=='(') k++;
            else if(s[i]==')')
            {
                k--;
                p++;
            }
            else
            {
                mask[p] |= (1<<(s[i]-'a'));
                if(k==0) p++;
            }
        }
        
        int cnt = 0;
        for(int i=0; i<D; i++)
        {
            bool ok = 1;
            for(int j=0; j<L; j++)
            {
                if((mask[j]&(1<<(W[i][j]-'a'))) == 0)
                {
                    ok = 0;
                    break;
                }
            }
            if(ok) cnt++;
        }
        
        cout<<"Case #"<<nCaso<<": "<<cnt<<endl;
    }
    return 0;
}
