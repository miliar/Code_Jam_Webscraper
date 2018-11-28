#include <string>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

int bc(int x)
{
    if(!x)
        return 0;
    return (x%2)+bc(x/2);
}

int tst()
{
    int n,m;
    scanf("%d%d\n",&n,&m);
    vector<int> masks(m);
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        {
            char c;
            scanf(" %c",&c);
            if(c=='x')
            {
                masks[j] |= (1<<i);
            }
        }

    vector<pair<int,int> > old;
    old.push_back(make_pair(0,0));
    for(int i=0;i<m;i++)
    {
        vector<pair<int,int> > nju;
        for(int mask=0;mask<(1<<n);mask++)
        {
            if(mask & masks[i])
                continue;
            int ans=0;
            for(int mm = 0;mm < old.size(); mm++)
            {
                if( ((old[mm].first | (old[mm].first/2) | (old[mm].first*2)) & mask) == 0)
                    ans >?= old[mm].second;
            }
            ans += bc(mask);
//            fprintf(stderr,"%d %d\n",mask,ans);
            nju.push_back(make_pair(mask,ans));
        }

        old = nju;
//        fprintf(stderr,"sep\n");
    }

//        fprintf(stderr,"sep\n");

    int ans=0;
    for(int i=0;i<old.size();i++)
        ans >?= old[i].second;
    return ans;
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        printf("Case #%d: %d\n",i+1,tst());
    }

}
