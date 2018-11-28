//x:1 o:2 t:3 .:5
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int map[5][5];
//int judge[5][4];
int main()
{
    int n,i,j,flag_h,flag_l,flag_d,flag,a,x,t,dh,dl,dd1,dd2,tmp,z;
    char graph[5];
  freopen("A-small-attempt3.in", "r", stdin);
   freopen("out.txt", "w", stdout);
    scanf("%d",&n);z = n;
    while(n--)
    {
        memset(map,0,sizeof(map));flag_h = flag_l=flag_d =0;x=t=0;
       // memset(judge,0,sizeof(judge));
        for(i=0;i<4;i++)
        {
            scanf("%s",graph);
            for(j=0;j<4;j++)
            {
                if(graph[j]=='X')
                    map[i][j] = 1;
                if(graph[j]=='O')
                    map[i][j] = 2;
                if(graph[j]=='T')
                    map[i][j] = 3;
                if(graph[j]=='.')
                    map[i][j] = 5;
            }
        }
        for(i=0;i<4;i++)
        {
            tmp = map[i][0]*map[i][1];flag_h=0;
            for(j=1,dh = 1;j<4;j++)
            {
                if(map[i][j]*map[i][j-1]==5||map[i][j]*map[i][j-1]==10||map[i][j]*map[i][j-1]==25||map[i][j]*map[i][j-1]==15){dh = 0;break;}
                else{if(map[i][j]*map[i][j-1]==2||tmp*(map[i][j]*map[i][j-1])==18){flag_h=1;break;}
                else
                {

                    if(map[i][j]!=3)
                    {
                        a = map[i][j];
                    }
                    if(map[i][j-1]!=3)
                    {
                        a = map[i][j-1];
                    }
                }
                }
                tmp = map[i][j]*map[i][j-1];
                }
            if(dh==1)
            {
                if(flag_h==0)
                {
                    if(1==a)x = 1;
                    else t = 1;
                }
            }
        }
       // printf("x:%d t:%d dh:%d flag_h:%d\n",x,t,dh,flag_h);
 //if(flag_h==0)

        for(i=0;i<4;i++)
        {
            tmp = map[0][i]*map[1][i];flag_l = 0;
            for(j=1,dl = 1;j<4;j++)
            {
                if(map[j][i]*map[j-1][i]==5||map[j][i]*map[j-1][i]==10||map[j][i]*map[j-1][i]==25||map[j][i]*map[j-1][i]==15){dl = 0;break;}

                else
                {
                    if(map[j][i]*map[j-1][i]==2||tmp*(map[j][i]*map[j-1][i])==18){flag_l=1;break;}//judge[i][1] = judge[i][2]=0;

                    else
                    {
                        if(map[j][i]!=3)
                        {
                        a = map[j][i];//judge[i][a] =1;
                        }
                        if(map[j-1][i]!=3)
                        {
                        a = map[j-1][i];//judge[i][a] =1;
                        }
                    }
                }
                tmp = map[j][i]*map[j-1][i];
            }
            if(dl==1)
            {
            if(flag_l==0)
            {
                if(1==a)x = 1;
                else t = 1;
            }
            }
        }
        //printf("x:%d t:%d dl:%d flag_l:%d\n",x,t,flag_l);
        tmp = map[1][1]*map[0][0]; dd1 = 1;
        for(i=1;i<4;i++)
        {

            if(map[i][i]*map[i-1][i-1]==5||map[i][i]*map[i-1][i-1]==10||map[i][i]*map[i-1][i-1]==25||map[i][i]*map[i-1][i-1]==15){dd1 = 0;break;}
            else{if(map[i][i]*map[i-1][i-1]==2||map[i][i]*map[i-1][i-1]==18){flag_d=1;break;}
             else
             {
                    if(map[i][i]!=3)
                    {
                        a = map[i][i];//judge[i][a] =1;
                    }
                    if(map[i-1][i-1]!=3)
                    {
                        a = map[i-1][i-1];//judge[i][a] =1;
                    }
             }
            }
             tmp = map[i][i]*map[i-1][i-1];
        }
        if(dd1==1)
        {if(flag_d==0)
        {
            if(1==a)x = 1;
            else t = 1;
        }
        }
        dd2 = 1;
        //printf("x:%d t:%d\n",x,t);flag_d = 0;
        tmp = map[1][2]*map[0][3];
        for(i=1;i<4;i++)
        {

            if(map[i][3-i]*map[i-1][4-i]==5||map[i][3-i]*map[i-1][4-i]==10||map[i][3-i]*map[i-1][4-i]==25||map[i][3-i]*map[i-1][4-i]==15){dd2 = 0;break;}
            else{if(map[i][3-i]*map[i-1][4-i]==2||map[i][3-i]*map[i-1][4-i]==18){flag_d=1;break;}
             else
             {
                    if(map[i][3-i]!=3)
                    {
                        a =map[i][3-i];//judge[i][a] =1;
                    }
                    if(map[i-1][4-i]!=3)
                    {
                        a = map[i-1][4-i];//judge[i][a] =1;
                    }
             }
            }
             tmp = map[i][3-i]*map[i-1][4-i];
        }
        if(dd2==1)
        {
        if(flag_d==0)
        {
            if(1==a)x = 1;
            else t = 1;
        }
        }
        //printf("x:%d t:%d\n",x,t);
        if(x*t==1){printf("Case #%d: Draw\n",z-n);}
        else
        {
            if(x == 0 && t == 1)
            {printf("Case #%d: O won\n",z-n);}
            if(x ==1  && t == 0)
            {printf("Case #%d: X won\n",z-n);}
            if(x == 0&& t== 0&& dh*dl*dd1*dd2==0)
            {printf("Case #%d: Game has not completed\n",z-n);}
            if(x == 0&& t==0 &&dh*dl*dd1*dd2!=0)
            {printf("Case #%d: Draw\n",z-n);}
        }
    }
    return 0;
}
