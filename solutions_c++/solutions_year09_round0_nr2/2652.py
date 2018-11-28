#include<iostream>

using namespace std;

void proceed (int a[][100],char l[][100][3],int h,int w,int cur,int H,int W);
char best(int a[][100],char l[][100][3],int h,int w,int H,int W)
{
int go[4]={0,0,0,0};
char goi='u';
if(h!=0)
go[0]=a[h][w]-a[h-1][w];
if(w!=0)
go[1]=a[h][w]-a[h][w-1];
if(w!=W-1)
go[2]=a[h][w]-a[h][w+1];
if(h!=H-1)
go[3]=a[h][w]-a[h+1][w];
if(go[1]>go[0])
{
go[0]=go[1];
goi='l';
}
if(go[2]>go[0])
{
go[0]=go[2];
goi='r';
}
if(go[3]>go[0])
{
go[0]=go[3];
goi='d';
}
if(go[0]>0)
return goi;
else return 'n';
}



void upflow(int a[][100],char l[][100][3],int h,int w,int cur,int H,int W)
{
l[h][w][2]='y';
if(h!=0)
{
if(l[h-1][w][1]=='n'&&best(a,l,h-1,w,H,W)=='d')
{
l[h-1][w][1]=cur;
l[h-1][w][1]='y';
proceed(a,l,h-1,w,cur,H,W);
}
}

if(w!=0)
{
if(l[h][w-1][1]=='n'&&best(a,l,h,w-1,H,W)=='r')
{
l[h][w-1][0]=cur;
l[h][w-1][1]='y';
proceed(a,l,h,w-1,cur,H,W);
}
}

if(w!=W-1)
{
if(l[h][w+1][1]=='n'&&best(a,l,h,w+1,H,W)=='l')
{
l[h][w+1][0]=cur;
l[h][w+1][1]='y';
proceed(a,l,h,w+1,cur,H,W);
}
}

if(h!=H-1)
{
if(l[h+1][w][1]=='n'&&best(a,l,h+1,w,H,W)=='u')
{
l[h+1][w][0]=cur;
l[h+1][w][1]='y';
l[h+1][w][0]=cur;
proceed(a,l,h+1,w,cur,H,W);
}
}

}

void downflow(int a[][100],char l[][100][3],int h,int w,int cur,int H,int W)
{
l[h][w][1]='y';
char goi=best(a,l,h,w,H,W);
if(goi!='n')
{
if(goi=='u')
{
l[h-1][w][0]=cur;
proceed(a,l,h-1,w,cur,H,W);
}
if(goi=='l')
{
l[h][w-1][0]=cur;
proceed(a,l,h,w-1,cur,H,W);
}
if(goi=='r')
{
l[h][w+1][0]=cur;
proceed(a,l,h,w+1,cur,H,W);
}
if(goi=='d')
{
l[h+1][w][0]=cur;
proceed(a,l,h+1,w,cur,H,W);
}
}
}




void proceed (int a[][100],char l[][100][3],int h,int w,int cur,int H,int W)
{
int i,j,flag=0;
if(l[h][w][1]=='n')
{
l[h][w][1]='y';
downflow(a,l,h,w,cur,H,W);
}
if(l[h][w][2]=='n')
{
l[h][w][2]='y';
upflow(a,l,h,w,cur,H,W);
}

}

void newlabel(int a[][100],char l[][100][3],int cur,int H,int W)
{
int i,j,flag=0;
for(i=0;i<H&&flag==0;i++)
for(j=0;j<W&flag==0;j++)
{
if(l[i][j][0]==96)
flag=1;
}
if(flag!=0)
{
l[i-1][j-1][0]=cur;
proceed(a,l,i-1,j-1,cur,H,W);
newlabel(a,l,cur+1,H,W);
}
}



int main()
{
int T,H,W,a[100][100],t,i,j;
char l[100][100][3];
cin>>T;
for(t=0;t<T;t++)
{
cout<<"Case #"<<t+1<<":"<<endl;
cin>>H>>W;
for(i=0;i<H;i++)
for(j=0;j<W;j++)
{
cin>>a[i][j];
l[i][j][0]=96;
l[i][j][1]='n';
l[i][j][2]='n';
}
newlabel(a,l,97,H,W);
for(i=0;i<H;i++)
{
for(j=0;j<W;j++)
cout<<l[i][j][0]<<" ";
cout<<endl;
}
}
return 0;
}
