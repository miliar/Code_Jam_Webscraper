#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
vector <int> bit, tam;
int ntest;
char s[110];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.ou","w",stdout);
    
    scanf("%d\n",&ntest);
    for (int test=1; test<=ntest; test++)
    {
        scanf("%s\n",&s);
        bit.clear();
        tam.clear();
        for (int i=0; i<strlen(s); i++)
        {
            bit.push_back(s[i]-'0');
            tam.push_back(s[i]-'0');
        }
        printf("Case #%d: ",test);
        if (next_permutation(bit.begin(),bit.end()))
           for (int i=0; i<bit.size(); i++)
               printf("%d",bit[i]);
        else
        {
            sort(bit.begin(),bit.end());
            int id=-1;
            for (int i=0; i<bit.size(); i++) 
                if (bit[i]!=0)
                {
                   printf("%d0",bit[i]);
                   id=i;
                   break;
                }
            for (int i=0; i<bit.size(); i++)
                if (i!=id)
                   printf("%d",bit[i]);
        }
        printf("\n");
    }
    
    
    return 0;
}
