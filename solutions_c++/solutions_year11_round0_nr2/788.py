#include<stdio.h>
#include<stdlib.h>
#include<deque>
#include<iostream>
#include<string>
#include<map>
using namespace std;
struct NODE
{
    char a;
    char b;
    NODE() {}
    NODE(char _a , char _b)
    {
        a = _a;
        b = _b;
    }
};
bool operator<(const NODE &a ,const NODE &b)
{
    if(a.a < b.a) return 1;
    if(a.a > b.a) return 0;
    if(a.b < b.b) return 1;
    if(a.b > b.b) return 0;
    return 0;
}
map<NODE , char> mp1;
map<NODE , char> mp2;
string cmd;
char st[10000];
int stn;
char get(char a,char b ,bool delq)
{
    if(delq)
    {
        if(mp2[NODE(a,b)] > 0) return '#';
        if(mp2[NODE(b,a)] > 0) return '#';
    }
    else
    {
        if(mp1[NODE(a,b)] > 0) return mp1[NODE(a,b)];
        if(mp1[NODE(b,a)] > 0) return mp1[NODE(b,a)];
    }
    return 0;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Magica_b.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int ii = 0;
    while(T--)
    {
        mp1.clear();
        mp2.clear();
        stn = 0;
        ii++;
        int ca , cb;
        scanf("%d",&ca);
        for(int i = 0 ; i < ca ; i++)
        {
            string ts ;
            cin >>ts;
            mp1[NODE(ts[0] , ts[1])] = ts[2];
        }
        scanf("%d",&cb);
        for(int i = 0 ; i < cb ; i++)
        {
            string ts ;
            cin >>ts;
            mp2[NODE(ts[0] , ts[1])] = '#';
        }
        int sn;
        cin >> sn >> cmd;


        for(int i = 0; i < sn; i++)
        {
            char a = cmd[i];
            if(stn == 0)
            {
                st[0] = a;
                stn++;
            }
            else
            {
                char b;

                //trans
                b = st[stn-1];
                char c = get(a,b,0);
                if(!(c == 0 || c == '#'))
                {
                    st[stn-1] = c;
                    continue;
                }
                //del
                bool flag= false;
                for(int j = stn-1 ; j >=0; j--)
                {
                    b = st[j];
                    char c = get(a,b,1);
                    if(c == 0) continue;
                    if(c != '#')continue;
                    flag = true;
                    stn = 0;
                    break;
                }
                if(!flag)
                {
                    st[stn++] = a;
                };

            }
        }
        printf("Case #%d: ",ii);
        putchar('[');
        if(stn>0)
        {
            printf("%c",st[0]);
            for(int i = 1; i < stn; i++)
                printf(", %c",st[i]);
        }
        puts("]");
    }
    return 0;
}
