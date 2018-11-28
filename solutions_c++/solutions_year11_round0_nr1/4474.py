#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
using namespace std;
int button[101];
int passkey[101][2];
int posb1=1;
int poso2=1;
int tim=0;
int passkeycnt=0;
FILE *fp;
char w;
void init()
{
    for(int i=0;i<101;i++)
    {
        button[i]=0;
        passkey[i][0]=0;
        passkey[i][1]=0;
        //pos2[i[=0;
        //pos1[i]=0;
    }
    poso2=1;
    posb1=1;
    tim=0;
    passkeycnt=0;
}
void getkey()
{int index;
char rob;
char str[20];
fscanf(fp,"%s",str);
passkeycnt=atoi(str);


    //cin>>passkeycnt;
    for(int i=0;i<passkeycnt;i++)
    {
        fscanf(fp,"%s",str);
        rob=str[0];
        fscanf(fp,"%s",str);
        index=atoi(str);
        //cin>>rob;
    //cin>>index;
    //cout<<index<<endl;
    if(rob=='O')
    passkey[i][0]=2;
    else
    passkey[i][0]=1;

    passkey[i][1]=index;


    }
}
int search(int color,int lpk)
{int i=lpk;
    while(i<passkeycnt)
    {
        if(passkey[i++][0]==color)
        return (i-1);
    }

    return -1;
}
void moveo2(int lpk)
{int cmp=search(2,lpk);
//cout<<"sad\n"<<passkey[cmp][1]<<"ADSA"<<endl;
if(cmp!=-1)
{if(poso2>passkey[cmp][1])
poso2--;
else if(poso2<passkey[cmp][1])
poso2++;
}
}
void moveb1(int lpk)
{int cmp=search(1,lpk);
if(cmp!=-1)
{if(posb1>passkey[cmp][1])
posb1--;
else if(posb1<passkey[cmp][1])
posb1++;
}
}



void algo()
{int tempo2=0;
int tempb1=0;
int locpasskeycnt=0;
int k=0;
    while(locpasskeycnt<passkeycnt)
    {

        if(passkey[locpasskeycnt][0]==1&&passkey[locpasskeycnt][1]==posb1)
       {//cout<<"entering 1";
           tim++;

        moveo2(locpasskeycnt);
            locpasskeycnt++;
           continue;
       }
         if(passkey[locpasskeycnt][0]==2&&passkey[locpasskeycnt][1]==poso2)
        {//cout<<"entrting 2";
            tim++;
        moveb1(locpasskeycnt);
            locpasskeycnt++;
            continue;

       }

    tim++;
       moveo2(locpasskeycnt);
       moveb1(locpasskeycnt);


    }
}

int main()
{ fp=fopen("//home//karan//Downloads//input.txt","r");

freopen("//home//karan//Desktop//output.txt","w",stdout);
    int n=0;
    int t63=0;
//    int t221=0'
    char str[30];
    fscanf(fp,"%s",str);
    n=atoi(str);
    //w=getc(fp);

  //  cin>>n;
    int k;
    for( k=1;k<=n;k++)
    {
    init();

    getkey();
    algo();

    cout<<"Case #"<<k<<": "<<tim<<endl;
    }
    return 0;
}












