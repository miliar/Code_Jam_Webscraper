#include <stdio.h>
#include <algorithm>

using namespace std;
const int NMAX = 1000000;
char buf[NMAX];

bool isdigit(char c)
{
    return c>='0' && c<='9';
}

int get_bot(char *&c)
{
    while (*c && (*c==' '||isdigit(*c)))
        ++c;
    if(*c=='O')
        return 0;
    if(*c=='B')
        return 1;
    return -1;
}
int get_pos(char *&c)
{
    while (*c && !isdigit(*c)) ++c;
    int num = 0;
    while (*c && isdigit(*c)) {
        num = 10*num + *c - '0';
        ++c;
    }
    return num;
}

int runtest(int it)
{
    int botpos[2] = {1,1};
    int alltime = 0;
    gets(buf);
    char *c = buf;
    int num_cmd = get_pos(c);
    int curtime  = 0;
    int prevtime = 0;
    int prevbot  = -2;
    for (int i=0; i<num_cmd; ++i) {
        int bot = get_bot(c);
        int pos = get_pos(c);
        int dist = std::abs(pos-botpos[bot]);   // dist to our next button
        botpos[bot] = pos;
        if (prevbot!=bot) {
            dist = std::max(dist-prevtime, 0);   // moving during other bot works
        }
        curtime = dist+1;                       // +1 to push
        if (prevbot!=bot) {
            prevtime = 0;
        }
        prevtime += curtime;
        alltime += curtime;
        prevbot = bot;
    }
    return alltime;
}

int main()
{
    freopen("in.txt",  "rt", stdin );
    freopen("out.txt", "wt", stdout);
    int numt = 0;
    scanf("%d\n",&numt);
    for(int it=0; it<numt; ++it) {
        int re = runtest(it);
        printf("Case #%d: %d\n", (1+it), (re));
    }
}


