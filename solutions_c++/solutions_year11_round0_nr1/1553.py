#include <cstdio>

char side[200][2];
int button[200];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int ti = 1; ti <= tc; ti++)
    {
        int bpos = 1, opos = 1;
        int t = 0;
        int step = 0;
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%s%d", side[i], &button[i]);
        }
        for(t=0;step < n;t++)
        {
            int nxt;
            if(side[step][0] == 'B' && button[step] == bpos)
            {
                nxt = step;
                while(nxt < n && side[nxt][0] != 'O')nxt++;
                if(nxt < n){ if(opos < button[nxt])opos++; else if(opos > button[nxt])opos--; }
                step++;
            }
            else if(side[step][0] == 'O' && button[step] == opos)
            {
                nxt = step;
                while(nxt < n && side[nxt][0] != 'B')nxt++;
                if(nxt < n){ if(bpos < button[nxt])bpos++; else if(bpos > button[nxt])bpos--; }
                step++;
            }
            else
            {
                nxt = step;
                while(nxt < n && side[nxt][0] != 'O')nxt++;
                if(nxt < n){ if(opos < button[nxt])opos++; else if(opos > button[nxt])opos--; }

                nxt = step;
                while(nxt < n && side[nxt][0] != 'B')nxt++;
                if(nxt < n){ if(bpos < button[nxt])bpos++; else if(bpos > button[nxt])bpos--; }
            }

        }
        printf("Case #%d: %d\n", ti, t);
    }
}
