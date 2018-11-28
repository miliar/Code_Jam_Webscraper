#include <cstdio>
#include <vector>
#include <utility>
using namespace std;

vector<int> v[2];
vector<int> com;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //
    int Tests;
    scanf("%d",&Tests);
    for(int Test=1;Test<=Tests;Test++)
    {
        printf("Case #%d: ", Test);
        int n;
        scanf("%d",&n);
        v[0].clear();
        v[1].clear();
        com.clear();
        for(int i=0;i<n;i++)
        {
            char s[2];
            int num;
            scanf("%s %d",s,&num);
            int c=s[0]=='O' ? 0 : 1;
            com.push_back(c);
            v[c].push_back(num);
        }
        //
        int p[2];
        p[0]=p[1]=0;
        int pcom=0;
        int x[2];
        x[0]=x[1]=1;
        //
        int res=0;
        while(pcom<com.size())
        {
            bool was[2];
            was[0]=was[1]=false;
            for(int i=0;i<2;i++)
                if(p[i]<v[i].size() && x[i]!=v[i][p[i]])
                {
                    was[i]=true;
                    if(x[i]<v[i][p[i]])
                        x[i]++;
                    else
                        x[i]--;
                }
            if(!was[com[pcom]] && x[com[pcom]]==v[com[pcom]][p[com[pcom]]])
            {
                p[com[pcom]]++;
                pcom++;
            }
            res++;
        }
        //
        printf("%d\n",res);
    }
    //
    return 0;
}
