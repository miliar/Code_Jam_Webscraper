#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
using namespace std;
struct {
    int button;
    int order;
}O[102],B[102];
int main()
{
    int t,i,count;
    char cmd[3];
    scanf("%d",&t);
    for(count=1;count<=t;count++)
    {
        int time=0,tem_o=0,tem_b=0;
        for(i=1;i<102;i++)
        {
            O[i].order=999;
            O[i].button=999;
            B[i].order=999;
            O[i].button=999;
        }
        int n;
        cin>>n;
        for(i=1;i<=n;i++)
        {
            scanf("%s",cmd);
            if(cmd[0]=='O')
            {
                scanf("%d",&O[++tem_o].button);
                O[tem_o].order=i;
            }
            else if(cmd[0]=='B')
            {
                scanf("%d",&B[++tem_b].button);
                B[tem_b].order=i;
            }
        }





        int b_order=1,o_order=1,b_position=1,o_position=1;
        while(999!=B[b_order].order||999!=O[o_order].order)
        {




                int del1=O[o_order].button-o_position;
                int del2=B[b_order].button-b_position;

            //O--------------------------------------------------------
            if(O[o_order].order<B[b_order].order)
            {
                    if(abs(del1)+1>=abs(del2))
                    {
                        time+=abs(del1)+1;
                        o_position=O[o_order].button;
                        b_position=B[b_order].button;
                    }
                    else
                    {
                        time+=abs(del1)+1;
                        if(del2>0)
                        b_position+=abs(del1)+1;
                        else
                        b_position-=(abs(del1)+1);
                        o_position=O[o_order].button;
                        //cout<<time<<endl<<b_position<<endl;
                    }
                o_order++;
            }


                del1=O[o_order].button-o_position;
                del2=B[b_order].button-b_position;
            //B------------------------------------------------
            if(O[o_order].order>B[b_order].order)
            {
                //cout<<del2<<endl<<B[b_order].button<<endl<<b_position<<endl;
                if(abs(del1)<=abs(del2)+1)
                {
                    time+=abs(del2)+1;
                    o_position=O[o_order].button;
                    b_position=B[b_order].button;
                }
                else
                {
                    if(del1>0)
                    o_position+=(abs(del2)+1);
                    else
                    o_position-=(abs(del2)+1);
                    time+=abs(del2)+1;
                    b_position=B[b_order].button;
                }
                b_order++;
            }

        }
            printf("Case #%d: %d\n",count,time);
    }
}

