#include <stdio.h>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;

struct order
{
    int p;
    int seqnum;
};
queue<order> Oseq, Bseq;
int T, t = 1;
int n;

int main()
{
         freopen("in.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
   for(scanf("%d", &T); T; --T)
    {

        char str[2];
        int pos;

        scanf("%d", &n);
        for(int i = 0; i < n; ++i)
        {
            order o;
            scanf("%s%d", str, &pos);

            o.p = pos;
            o.seqnum = i + 1;
            if(str[0] == 'O')
                Oseq.push(o);
            else
                Bseq.push(o);
        }

        int ans = 0;
        int opos = 1, bpos = 1;

        while(1)
        {
            if(Oseq.empty() && Bseq.empty())
                break;
            ++ans;

            if(Oseq.empty())
            {
                int bnext = Bseq.front().p;
                if(bpos < bnext)
                    ++bpos;
                else if(bpos > bnext)
                    --bpos;
                else
                    Bseq.pop();
            }else if(Bseq.empty())
            {
                int onext = Oseq.front().p;
                if(opos < onext)
                    ++opos;
                else if(opos > onext)
                    --opos;
                else
                    Oseq.pop();
            }else
            {
                int bnext = Bseq.front().p;
                int onext = Oseq.front().p;
                bool opop = false, bpop = false;
                if(bpos < bnext)
                    ++bpos;
                else if(bpos > bnext)
                    --bpos;
                else 
                {
                    bpop = true;
                }
                if(opos < onext)
                    ++opos;
                else if(opos > onext)
                    --opos;
                else
                {
                    opop = true;
                }
                if(opop && bpop)
                {
                    if(Oseq.front().seqnum < Bseq.front().seqnum)
                        Oseq.pop();
                    else
                        Bseq.pop();
                }else if(opop && Oseq.front().seqnum < Bseq.front().seqnum)
                    Oseq.pop();
                else if(bpop && Bseq.front().seqnum < Oseq.front().seqnum)
                    Bseq.pop();
            }
        }
        
        printf("Case #%d: %d\n", t++, ans);
    }
}