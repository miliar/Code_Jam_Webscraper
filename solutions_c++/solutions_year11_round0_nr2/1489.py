
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int kCase=1;kCase<=T;kCase++)
    {
        char combine[26][26] = {0};
        int C, D, N;
        scanf("%d",&C);
        for(int i=0;i<C;i++)
        {
            char c1,c2,c3;
            scanf(" %c%c%c", &c1,&c2,&c3);
            combine[c1-'A'][c2-'A'] = c3;
            combine[c2-'A'][c1-'A'] = c3;
        }

        char opposed[26][26] = {0};
        scanf("%d",&D);
        for(int i=0;i<D;i++)
        {
            char c1,c2;
            scanf(" %c%c",&c1,&c2);
            opposed[c1-'A'][c2-'A'] = 1;
            opposed[c2-'A'][c1-'A'] = 1;
        }

        vector<char> stk;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            char c1;
            scanf(" %c",&c1);
            
            // do combine
            while(!stk.empty() && combine[stk.back()-'A'][c1-'A'])
            {
                c1 = combine[stk.back()-'A'][c1-'A'];
                stk.pop_back();
            }

            // do opposed
            bool bOpposed = false;
            for(int i=0;i<stk.size();i++)
            {
                if(opposed[stk[i]-'A'][c1-'A'])
                {
                    bOpposed = true;
                    stk.clear();
                }
            }

            if(!bOpposed)
            {
                stk.push_back(c1);
            }
        }

        //Case #1: [E, A]
        printf("Case #%d: [", kCase);
        for(int i=0;i<stk.size();i++)
        {
            if(i==0)
            {
                printf("%c", stk[i]);
            }
            else
            {
                printf(", %c", stk[i]);   
            }
        }
        printf("]\n");
    }
}



namespace{
struct Test
{
    Test()
    {
        freopen("../Resource/B-large.in","r",stdin);
        freopen("../Resource/B-large.out","w",stdout);
    }

    ~Test()
    {
        //scanf("%*s");
    }
}g_Test;
}

