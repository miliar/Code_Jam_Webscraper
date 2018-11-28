
#include<iostream>
#include<cstdio>
using namespace std;


int N;
inline int dif (int p1, int p2)
{
    int p = p1 - p2;
    if (p < 0) p = -p;
    ++p;
    return p;
}
inline int make(int a, int b)
{
    if (b >= (a-1)) return 1;
	return a-b;
}
int cal()
{
    int i,p;
    int pO, pB;
    int intervalO, intervalB;
    char color[5];
    scanf ("%d", &N);
    int t = 0, interval;
    pO = pB = 1;
    intervalO = intervalB = 0;
    for (i = 0; i <N; i++)
    {
        scanf ("%s %d", color, &p);
        if (color[0] == 'O')
        {
            interval = dif(pO, p);
            interval = make(interval, intervalO);
            t += interval;
            pO = p;
			intervalO= 0;
            intervalB += interval; 
        }
        else
        {
            interval = dif(pB, p);
            interval = make(interval, intervalB);
            t += interval;
            pB = p;
			intervalB= 0;
            intervalO += interval; 
			
        }
    }
    return t;
}






int main()
{
   int T,i,t;
  // freopen("A-large.in", "r", stdin);
  // freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (i = 1; i<= T; i++)
    {
        t = cal();
        printf ("Case #%d: %d\n", i, t);
    }
    return 0;
}
