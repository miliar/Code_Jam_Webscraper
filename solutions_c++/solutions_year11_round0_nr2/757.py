#include <cstdio>
#include <deque>
#include <cstring>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);//*/
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;++t)
    {
        char combine[26][26]={};
        int opposed[26]={};
        int C,D,N;
        scanf("%d",&C);
        for (int i=0;i<C;++i)
        {
            char s[10];
            scanf("%s",s);
            combine[s[0]-'A'][s[1]-'A'] = s[2]-'A';
            combine[s[1]-'A'][s[0]-'A'] = s[2]-'A';
        }
        scanf("%d",&D);
        for (int i=0;i<D;++i)
        {
            char s[10];
            scanf("%s",s);
            opposed[s[0]-'A'] |= 1<<(s[1]-'A');
            opposed[s[1]-'A'] |= 1<<(s[0]-'A');
        }
        scanf("%d",&N);
        char s[1000];
        scanf("%s",s);
        deque<int> d;
        int used=0,iused[26]={};
        for (int i=0;i<N;++i)
        {
            int c = s[i]-'A';
            if (!d.empty() && combine[d.back()][c])
            {
                int old = d.back(), neww = combine[d.back()][c];
                if (!(--iused[old]))
                    used = used & (~(1<<old));
                iused[neww]++;
                used |= 1<<neww;
                d.back() = neww;
            }
            else if (opposed[c]&used)
            {
                d.clear();
                used=0;
                memset(iused,0,sizeof(iused));
            }
            else
            {
                used |= 1<<c;
                iused[c]++;
                d.push_back(c);
            }
        }
        printf("Case #%d: [",t);
        for (deque<int>::iterator i=d.begin();i!=d.end();++i)
            if (i==d.begin())
                printf("%c",*i+'A');
            else
                printf(", %c",*i+'A');
        printf("]\n");
    }
    fclose(stdin);
    fclose(stdout);//*/
    return 0;
}
