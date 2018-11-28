#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

int orange[100][2];
int blue[100][2];
int main()
{
   freopen("A-large.in", "r", stdin);
   freopen("output.out", "w", stdout);
    int t, n, button;
    char color;
    scanf("%d",&t);
    for(int i=1; i<=t; i++)
    {
        scanf("%d",&n);
        int ora_cnt = 0;
        int blu_cnt = 0;
        int cnt = 0;
        for(int j=0; j<n; j++)
        {
            cin>>color>>button;
            if(color=='O')
            {
                orange[ora_cnt][0] = button;
                orange[ora_cnt++][1] = cnt++;
            }
            if(color=='B')
            {
                blue[blu_cnt][0] = button;
                blue[blu_cnt++][1] = cnt++;
            }
        }
        int ora_pos=1;
        int blu_pos=1;
        int ora_cur=0;
        int blu_cur=0;
        int pressed=0;
        int ans=0;
        while(pressed!=cnt)
        {
            int aim;
            int times;
            if(ora_cur<ora_cnt && orange[ora_cur][1]==pressed)
            {
                aim = orange[ora_cur++][0];
                times=(int)fabs(aim-ora_pos)+1;
                ans+=times;
                pressed++;
                ora_pos = aim;
                for(int j=0; j<times; j++)
                {
                    if(blu_pos<blue[blu_cur][0])
                        blu_pos++;
                    if(blu_pos==blue[blu_cur][0])
                        break;
                    if(blu_pos>blue[blu_cur][0])
                        blu_pos--;
                }
            }
            if(blu_cur<blu_cnt &&blue[blu_cur][1]==pressed)
            {
                aim = blue[blu_cur++][0];
                times=(int)fabs(aim-blu_pos)+1;
                ans+=times;
                blu_pos = aim;
                pressed++;
                for(int j=0; j<times; j++)
                {
                    if(ora_pos<orange[ora_cur][0])
                        ora_pos++;
                    if(ora_pos==orange[ora_cur][0])
                        break;
                    if(ora_pos>orange[ora_cur][0])
                        ora_pos--;
                }
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
}
