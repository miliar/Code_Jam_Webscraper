#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
using namespace std;
struct NODE
    {
        int pos;
        int pri;
        NODE(){}
        NODE(int _po ,int _pr)
            {
                pos = _po;
                pri = _pr;
            }
    };
vector<NODE> q[2];
char ts[10];
int main()
    {
        freopen("A-large.in","r",stdin);
        freopen("Bot_b.txt","w",stdout);
        int T;
        scanf("%d",&T);
        int ii = 0;
        while(T--)
            {
                q[0].clear();
                q[1].clear();
                ii++;
                int n;
                scanf("%d",&n);
                for(int i = 0 ; i < n ; i++)
                    {
                        int p;
                        scanf("%s%d",ts,&p);
                        if(ts[0] == 'O')
                            q[0].push_back(NODE(p , i));
                        if(ts[0] == 'B')
                            q[1].push_back(NODE(p , i));
                    }
                int x1  = 0 , x2 = 0;
                int p1 = 1 , p2 = 1;
                int ans =0;
                while(x1 < q[0].size() || x2 < q[1].size())
                    {
                        if(x1 == q[0].size())
                            {
                                ans += abs(q[1][x2].pos - p2)+1;
                                p2 = q[1][x2].pos;
                                x2++;
                                continue;
                            }
                        if(x2 == q[1].size())
                            {
                                ans += abs(q[0][x1].pos - p1)+1;
                                p1 = q[0][x1].pos;
                                x1++;
                                continue;
                            }
                        int d1 = abs(q[0][x1].pos - p1);
                        int d2 = abs(q[1][x2].pos - p2);
                        if(d1 == d2&& q[0][x1].pri < q[1][x2].pri)
                            {
                                ans +=abs(q[0][x1].pos - p1)+1;
                                p1 = q[0][x1].pos;
                                p2 = q[1][x2].pos;
                                x1++;
                                continue;
                            }
                        if(d1 == d2&& q[0][x1].pri > q[1][x2].pri)
                            {
                                ans +=abs(q[1][x2].pos - p2)+1;
                                p1 = q[0][x1].pos;
                                p2 = q[1][x2].pos;
                                x2++;
                                continue;
                            }
                        if(d1 < d2 && q[0][x1].pri < q[1][x2].pri)
                            {
                                ans += abs(q[0][x1].pos - p1)+1;
                                p1 = q[0][x1].pos;
                                p2 = q[1][x2].pos - (d2-d1-1);
                                x1++;
                                continue;
                            }
                        if(d1 < d2 && q[0][x1].pri > q[1][x2].pri)
                            {
                                ans += abs(q[1][x2].pos - p2)+1;
                                p2 = q[1][x2].pos;
                                p1 = q[0][x1].pos;
                                x2++;
                            }
                        if(d1 > d2 && q[0][x1].pri > q[1][x2].pri)
                            {
                                ans += abs(q[1][x2].pos - p2)+1;
                                p1 = q[0][x1].pos - (d1- d2-1);
                                p2 = q[1][x2].pos;
                                x2++;
                                continue;
                            }
                        if(d1 > d2 && q[0][x1].pri < q[1][x2].pri)
                            {
                                ans += abs(q[0][x1].pos - p1)+1;
                                p1 = q[0][x1].pos;
                                p2 = q[1][x2].pos;
                                x1++;
                            }
                    }
                printf("Case #%d: %d\n",ii,ans);
            }
        return 0;
    }
