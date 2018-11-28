#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
char robot[101];
int button[101];
int O[101],B[101];
bool fgO[101], fgB[101];
int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    int t, n, x = 1;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        int a = 0, b = 0;
        for (int i = 0; i <= n; i++)
        {
            O[i] = B[i] = 1;
        }
        memset(fgO, 0, sizeof(fgO));
        memset(fgB, 0, sizeof(fgB));
        for (int i = 1; i <= n; i++)
        {
            cin>>robot[i]>>button[i];
            if (robot[i] == 'B')
            {
                B[b++] = button[i];
            }
            if (robot[i] == 'O')
            {
                O[a++] = button[i];
            }

        }
        int time = 0;
        int tmO = 0, nowO = 1;
        int tmB = 0, nowB = 1;
        int tmtime = 0;
        fgO[1] = 1;
        fgB[1] = 1;
        for (int i = 1; i <= n; i++)
        {
            if (robot[i] == 'O')
            {

                if (button[i] - nowO >= 0)
                {
                    tmtime = button[i] - nowO + 1;
                    if (B[tmB] - nowB > 0)
                    {
                        if (B[tmB] - nowB <= tmtime)
                        {
                            nowB = B[tmB];
                            //printf("nowB1 == %d\n", nowB);
                            //if (fgB[nowB]&& tmB + 1 < b)
                            {
                                //tmB++;
                                //fgB[nowB] = 0;
                            }

                        }
                        else
                        {
                            nowB += tmtime;
                            //printf("nowB2 == %d\n", nowB);
                        }
                    }
                    if (B[tmB] - nowB < 0)
                    {
                        if (nowB - B[tmB] <= tmtime)
                        {
                            nowB = B[tmB];
                            //printf("nowB3 == %d\n", nowB);
                            //if (fgB[nowB] && tmB + 1 < b)
                            {
                                //fgB[nowB] = 0;
                                //tmB++;
                            }

                        }
                        else
                        {
                            nowB -= tmtime;
                            //printf("nowB4 == %d\n", nowB);
                        }

                    }
                }
                else
                {
                    tmtime = nowO - button[i] + 1;
                    if (B[tmB] - nowB > 0)
                    {
                        if (B[tmB] - nowB <= tmtime)
                        {
                            nowB = B[tmB];
                            //printf("nowB5 == %d\n", nowB);
                            //if (fgB[nowB] && tmB + 1 < b)
                            {
                                //tmB++;
                                //fgB[nowB] = 0;
                            }

                        }
                        else
                        {
                            nowB += tmtime;
                            //printf("nowB6 == %d\n", nowB);
                        }
                    }
                    if (B[tmB] - nowB < 0)
                    {
                        if (nowB - B[tmB] <= tmtime)
                        {
                            nowB = B[tmB];
                            //printf("nowB7 == %d\n", nowB);
                           // if (fgB[nowB] && tmB + 1 < b)
                            {
                                //tmB++;
                                //fgB[nowB] = 0;
                            }

                        }
                        else
                        {
                            nowB -= tmtime;
                            //printf("nowB8 == %d\n", nowB);
                        }

                    }

                }
                time += tmtime;
                //printf("time == %d\n", time);
                nowO = button[i];
                //if(!fgO[nowO])
                {
                    if(tmO + 1 < a)
                        tmO++;
                    //printf("nowO 0 == %d\n", nowO);
                    //fgO[nowO] = 1;
                }
            }
            if (robot[i] == 'B')
            {
                if (button[i] - nowB >= 0)
                {
                    tmtime = button[i] - nowB + 1;
                    if (O[tmO] - nowO > 0)
                    {
                        if (O[tmO] - nowO <= tmtime)
                        {
                            nowO = O[tmO];
                           // printf("nowO1 == %d\n", nowO);
                            //if (fgO[nowO]&& tmO + 1 < a)
                            {
                                //tmO++;
                                //fgO[nowO] = 0;
                            }

                        }
                        else
                        {
                            nowO += tmtime;
                            //printf("nowO2 == %d\n", nowO);
                        }
                    }
                    if (O[tmO] - nowO < 0)
                    {
                        if (nowO - O[tmO] <= tmtime)
                        {
                            nowO = O[tmO];
                            //printf("nowO3 == %d\n", nowO);
                            //if (fgO[nowO]&& tmO + 1 < a)
                            {
                                //fgO[nowO] = 0;
                                //tmO++;
                            }

                        }
                        else
                        {
                            nowO -= tmtime;
                            //printf("nowO4 == %d\n", nowO);
                        }

                    }
                }
                else
                {
                    tmtime = nowB - button[i] + 1;
                    if (O[tmO] - nowO > 0)
                    {
                        if (O[tmO] - nowO <= tmtime)
                        {
                            nowO = O[tmB];
                            //printf("nowO5 == %d\n", nowO);
                            //if (fgO[nowO]&& tmO + 1 < a)
                            {
                                //tmO++;
                                //fgO[nowO] = 0;
                            }

                        }
                        else
                        {
                            nowO += tmtime;
                            //printf("nowO6 == %d\n", nowO);
                        }
                    }
                    if (O[tmO] - nowO < 0)
                    {
                        if (nowO - O[tmO] <= tmtime)
                        {
                            nowO = O[tmO];
                            //printf("nowO7 == %d\n", nowO);
                            //if (fgO[nowO]&& tmO + 1 < a)
                            {
                                //tmO++;
                                //fgO[nowO] = 0;
                            }

                        }
                        else
                        {
                            nowO -= tmtime;
                            //printf("nowO8 == %d\n", nowO);
                        }

                    }
                }
                time += tmtime;
                //printf("time == %d\n", time);
                nowB = button[i];
                //if(!fgB[nowB])
                {
                    if(tmB + 1 < b)
                    tmB++;
                    //printf("nowB 0== %d\n", nowB);
                    //fgB[nowB] = 1;
                }

            }
        }
        printf("Case #%d: %d\n",x++ , time);
    }
}
