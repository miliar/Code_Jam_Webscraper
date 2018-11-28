# include <iostream>
# include <string>
# include <stack>
# include <vector>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,cas,c,d,n;
    string str;
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        vector<char> stk;
        char pair[256][256]={0};
        bool ops[256][256]={0};

        cin>>c;
        for(int i=0;i<c;i++)
        {
            cin>>str;
            pair[str[0]][str[1]] = str[2];
            pair[str[1]][str[0]] = str[2];
        }

        cin>>d;
        for(int i=0;i<d;i++)
        {
            cin>>str;
            ops[str[0]][str[1]] = 1;
            ops[str[1]][str[0]] = 1;
        }

        cin>>n;
        cin>>str;
        for(int i=0;i<str.size();i++)
        {
            stk.push_back(str[i]);

            if(stk.size() > 1 )
            {
                char last = stk[stk.size()-1];
                char last2 = stk[stk.size()-2];
                char p = pair [last][last2];
                if( p )
                {
                    stk.pop_back();
                    stk.pop_back();
                    stk.push_back(p);
                }
            }

            for(int j=0;j<stk.size();j++)
            {
                if( ops[stk[j]][stk.back()] )
                {
                    stk.clear();
                    break;
                }
            }
        }
        printf("Case #%d: ",cas);
        printf("[");
        for(int i=0;i<stk.size();i++)
        {
            if( i < stk.size()-1)
            {
                printf("%c, ",stk[i]);
            }
            else printf("%c",stk[i]);
        }
        printf("]\n");
    }
    return 0;
}
