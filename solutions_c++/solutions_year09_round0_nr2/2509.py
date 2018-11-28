#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <math.h>
#include <bitset>
#include <string.h>
#include <stack>
#include <queue>
#include <memory.h>

#define MAXH 102
#define MAXW 102
#define SET(a,b) memset(a,b,sizeof(a));
#define input(a) scanf("%d",&a);
using namespace std;

int alt[MAXH][MAXW],drained[MAXH][MAXW],h,w,cells_covered=0,xx,yy,ind;
char final_matrix[MAXH][MAXW];
bool status[MAXH][MAXW];


//============= print_matrix =============
void print_matrix2()
{cout<<h<<" "<<w<<endl;
 for(int a=0;a<h;++a)
 {for(int b=0;b<w;++b)
 {
     printf("%d ",drained[a][b]);
 }
 printf("\n");
}
return ;
}
//print_matrix real =====================
void print_matrix()
{

int finalval[MAXH*MAXW];
SET(finalval,0);
int offset=-ind,temp;
char z='a';
 for(int a=0;a<h;++a)
 {for(int b=0;b<w;++b)
 {temp=drained[a][b]+offset;
     if(!finalval[temp])
    {finalval[temp]=z;z++;}
 printf("%c ",finalval[temp]);
 }printf("\n");
}
return ;
}
//============== get_max_coord =============
void get_max_coord()
{
    int maxalt=-1;
    for (int a=0;a<h;++a)
    {
        for (int b=0;b<w;++b)
        {
            if (alt[a][b]>maxalt && !status[a][b])
            {
                maxalt=alt[a][b];
                xx=a;
                yy=b;
            }
        }
    }
   // cout<<xx<<" "<<yy<<endl;
    return;
}

//============ isvalid ================
bool isvalid(int x,int y)
{if(x<0 || x>=h || y < 0 || y>=w)
{return false;}
return true;
}

//===========track_back ================
void track_back(int x,int y,int cost)
{int x1,x2,x3,x4,y1,y2,y3,y4;
    drained[x][y]=ind;

x1=x-1;y1=y;
x2=x;y2=y-1;
x3=x;y3=y+1;
x4=x+1;y4=y;

if(isvalid(x1,y1) && drained[x1][y1]==cost)
{drained[x1][y1]=ind;
track_back(x1,y1,cost);
}

if(isvalid(x2,y2) && drained[x2][y2]==cost)
{drained[x2][y2]=ind;
track_back(x2,y2,cost);
}

if(isvalid(x3,y3) && drained[x3][y3]==cost)
{drained[x3][y3]=ind;
track_back(x3,y3,cost);
}

if(isvalid(x4,y4) && drained[x4][y4]==cost)
{drained[x4][y4]=ind;
track_back(x4,y4,cost);
}

return;
}
//================ getvalidcell ==============
bool getvalidcell()
{bool check=0;
int x1,x2,x3,x4,y1,y2,y3,y4,d1,d2,d3,d4,maxd=0,newx,newy;

x1=xx-1;y1=yy;
x2=xx;y2=yy-1;
x3=xx;y3=yy+1;
x4=xx+1;y4=yy;

if(isvalid(x1,y1))
{d1=alt[xx][yy]-alt[x1][y1];
if(d1>maxd){maxd=d1;newx=x1;newy=y1;check=1;}
}


if(isvalid(x2,y2))
{d2=alt[xx][yy]-alt[x2][y2];
if(d2>maxd){maxd=d2;newx=x2;newy=y2;check=1;}
}


if(isvalid(x3,y3))
{d3=alt[xx][yy]-alt[x3][y3];
if(d3>maxd){maxd=d3;newx=x3;newy=y3;check=1;}
}


if(isvalid(x4,y4))
{d4=alt[xx][yy]-alt[x4][y4];
if(d4>maxd){maxd=d4;newx=x4;newy=y4;check=1;}
}

if(check)
 {
 status[xx][yy]=1;
 drained[xx][yy]=ind;
 if(status[newx][newy])
 {
 //print_matrix();
     track_back(newx,newy,drained[newx][newy]);
 //cout<<endl;
 //print_matrix();exit(0);

 return 0;
 }
   else
 {xx=newx;yy=newy;return 1;}
 }
 else
 {status[xx][yy]=1;drained[xx][yy]=ind;
 return 0;
 }
}

//================ fill ======================
void fill()
{
    while (getvalidcell())
    {
        cells_covered++;
    }
    return;
}

//========== main =======================
int main()
{
    freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
    int t,g=1;
    input(t);
    while (t--)
    {SET(drained,0);
     SET(status,0);
        input(h);
        input(w);

        for (int a=0;a<h;++a)
        {
            for (int b=0;b<w;++b)
            {
               input(alt[a][b]);
            }
        }

        ind=-1;
        cells_covered=0;
        while (cells_covered!=h*w)
        {cells_covered++;
            get_max_coord();
            fill();
            ind--;
               //  print_matrix();

        }
        //fillup_label();
      printf("Case #%d:\n",g);
        print_matrix();
        g++;
    }


    return 0;
}


