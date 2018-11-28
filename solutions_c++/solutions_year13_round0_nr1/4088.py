#include<iostream>
#include<fstream>

using namespace std;
fstream f1,f2;
int main()
{   char c;
    int x=0,o=0,t=0,d=0,i,j,flag=0,cas,u=0;
    char a[4][4];
    f1.open("large.in",ios::in);
    f2.open("outo.out",ios::out);
    f1>>cas;
    while(f1)
{

f1.get(c);
if(c=='\n')
break;
            }

    while(f1)
    {
        x=0;
        o=0;
        t=0;
        d=0;
        i=0;
        j=0;
        flag=0;

        for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        f1>>a[i][j];

    }
    for(i=0;i<4;i++)
    {x=0;
    o=0;
    t=0;
        for(j=0;j<4;j++)
        {
            if(a[i][j]=='X')

                x++;
                else if(a[i][j]=='O')
                o++;
                else if(a[i][j]=='T')
                t++;
                else if(a[i][j]=='.')
                d++;

        }
        if((x+t)==4)
        flag=1;
        else if ((o+t)==4)
        flag=2;



    }
    x=0;
    o=0;
    t=0;

    for(j=0;j<4;j++)
    {
        x=0;
    o=0;
    t=0;
       for(i=0;i<4;i++)
       {
         if(a[i][j]=='X')

                x++;
                else if(a[i][j]=='O')
                o++;
                else if(a[i][j]=='T')
                t++;
                else if(a[i][j]=='.')
                d++;

        }
        if((x+t)==4)
        flag=1;
        else if ((o+t)==4)
        flag=2;
       }
       x=0;
       t=0;
       o=0;
        for(i=0;i<4;i++)
        {
            if(a[i][i]=='X')

                x++;
                else if(a[i][i]=='O')
                o++;
                else if(a[i][i]=='T')
                t++;
                else if(a[i][i]=='.')
                d++;

        }
        if((x+t)==4)
        flag=1;
        else if ((o+t)==4)
        flag=2;
        x=0;
        o=0;
        t=0;
        for(i=0,j=3;i<4,j>=0;i++,j--)
        {
            if(a[i][j]=='X')

                x++;
                else if(a[i][j]=='O')
                o++;
                else if(a[i][j]=='T')
                t++;
                else if(a[i][j]=='.')
                d++;

        }
        if((x+t)==4)
        flag=1;
        else if ((o+t)==4)
        flag=2;
         if(u<cas)
    {


 f2<<"Case #"<<u+1;
 f2<<": ";
 if(flag==1)
f2<<"X won";
else if(flag==2)
f2<<"O won";
else if(flag==0)
{
    if(d==0)
    f2<<"Draw";
    else
    f2<<"Game has not completed";
}

 f2<<"\n";
 u++;
    }
}
f1.close();
f2.close();
return 0;
    }
