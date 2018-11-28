#include <iostream>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

const int MAXN = 26;
char mat[MAXN][MAXN], opmat[MAXN][MAXN];

int main()
{
    freopen("out.txt", "w", stdout); 
    int T, C;
    cin>>T;
    
    for(int t = 1; T--; ++t)
    {
        memset(mat, 0, sizeof(mat));
        memset(opmat, 0, sizeof(opmat));
        string invoke, temps;
        vector <char> ans;
        
        cin>>C;
        for(int i = 0; i < C; i++)
        {
            cin>>temps;
            mat[temps[0]-'A'][temps[1]-'A'] = mat[temps[1]-'A'][temps[0]-'A'] = temps[2];
        }
        
        cin>>C;
        for(int i = 0; i < C; i++)
        {
            cin>>temps;
            opmat[temps[0]-'A'][temps[1]-'A'] = opmat[temps[1]-'A'][temps[0]-'A'] = 1;
        }
        
        cin>>C;
        cin>>invoke;
        for(int i = 0; i < C; i++)
        {
            ans.push_back(invoke[i]);
            while(ans.size()>=2 && mat[ans.back()-'A'][ans[ans.size()-2]-'A'])
            {
                char tar = mat[ans.back()-'A'][ans[ans.size()-2]-'A'];
                ans.pop_back();
                ans.pop_back();
                ans.push_back(tar);
            }
            
            bool cflag = false;
            char topc = ans.back();
            for(int j = 0; j < ans.size(); j++)
                if(opmat[ans[j]-'A'][topc-'A'])
                {
                    ans.clear();
                    break;
                }
        }
        
        printf("Case #%d: [", t);
        for(int i = 0; i < ans.size(); i++)
        {
            if(i) printf(", ");
            printf("%c", ans[i]);
        }
        
        printf("]\n");
    }
    
    return 0;
}
