#include<iostream>
#include<stdio.h>
using namespace std;
int orange[100][2];
int blue[100][2];
int main()
{
    freopen("D:\\b.txt", "w", stdout);
    int t, n, button;
    int posO, posB, curO=0, curB, pressed, ans;
    int cntO, cntB = 0, cnt = 0;
    char color;
    scanf("%d",&t);
    int i = 1;
    while(i <= t)
    {
        scanf("%d", &n);
        cntO = 0;
        cntB = 0;
        cnt = 0;
        for(int j=0; j<n; j++)
        {
            cin >> color >> button;
            if(color=='O')
            {
                orange[cntO][0] = button;
                orange[cntO++][1] = cnt++;
            }
            else if(color=='B')
            {
                blue[cntB][0] = button;
                blue[cntB++][1] = cnt++;
            }

        }
        posO=1;
        posB=1;
        curO=0;
        curB=0;
        pressed=0;
        ans=0;
        while(pressed!=cnt)
        {
            int aim;
            int times;
            if(curO<cntO && orange[curO][1]==pressed)
            {
                aim = orange[curO++][0];
                times=abs(aim-posO)+1;
                ans+=times;
                pressed++;
                posO = aim;
                for(int j=0; j<times; j++)
                {
                    if(posB<blue[curB][0])
                        posB++;
                    if(posB==blue[curB][0])
                        break;
                    if(posB>blue[curB][0])
                        posB--;
                }
            }
            if(curB<cntB &&blue[curB][1]==pressed)
            {
                aim = blue[curB++][0];
                times=abs(aim-posB)+1;
                ans+=times;
                posB = aim;
                pressed++;
                for(int j=0; j<times; j++)
                {
                    if(posO<orange[curO][0])
                        posO++;
                    if(posO==orange[curO][0])
                        break;
                    if(posO>orange[curO][0])
                        posO--;
                }
            }
        }
        cout<< "Case #"<< i << ": " << ans << endl;
        i ++;
    }
}

