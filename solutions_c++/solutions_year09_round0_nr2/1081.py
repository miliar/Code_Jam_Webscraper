#include<iostream>
using namespace std;
#include<conio.h>

int in[100][100],M[100][100],MAX=1000000000;
int ctr,r,c;

int north,south,east,west;

void find(int i, int j)
{
     if (i>0 && in[i-1][j]<in[i][j])
       north=in[i-1][j];
    else
        north=MAX;
    if (i<r-1 && in[i+1][j]<in[i][j])
       south=in[i+1][j];
    else
        south=MAX;
    if (j>0 && in[i][j-1]<in[i][j])
       west=in[i][j-1];
    else
        west=MAX;
    if (j<c-1 && in[i][j+1]<in[i][j])
       east=in[i][j+1];
    else
        east=MAX;
}

int check(int i,int j)
{
     find(i,j);
     if (north==MAX && south==MAX && east==MAX && west==MAX)
        return -1;
     if (north<=west && north<=south && north<=east)
     {
        if (M[i-1][j]!=-1)
           return M[i-1][j];   
        else
            return check(i-1,j);
     }
     else if (west<=north && west<=south && west<=east)
     {
          if (M[i][j-1]!=-1)
             return M[i][j-1];
          else
              return check(i,j-1);
     }
     else if (east<=north && east<=south && east<=west)
     {
              if (M[i][j+1]!=-1)
                 return M[i][j+1];
              else
                  return check(i,j+1);
      }
      else if (south<=north && south<=west && south<=east)
      {
              if (M[i+1][j]!=-1)
                 return M[i+1][j];
              else
                  return check(i+1,j);
      }
}

void fill(int i, int j)
{
     find(i,j);
        
    //printf("%d %d %d %d %d %d\n",i,j,north,south,west,east);
    //getch();
    if (north==MAX && south==MAX && east==MAX && west==MAX)
       return ;    
       
    if (north<=west && north<=south && north<=east)
    {
       if (M[i-1][j]==-1)
       {
          M[i-1][j]=M[i][j];   
          fill(i-1,j);
       }
    }
    else if (west<=north && west<=south && west<=east)
    {
       if (M[i][j-1]==-1)
       {
          M[i][j-1]=M[i][j];   
          fill(i,j-1);
       }
    }
    else if (east<=north && east<=south && east<=west)
    {
       if (M[i][j+1]==-1)
       {
          M[i][j+1]=M[i][j];   
          fill(i,j+1);
       }
    }
    else if (south<=north && south<=west && south<=east)
    {
       if (M[i+1][j]==-1)
       {
          M[i+1][j]=M[i][j];   
          fill(i+1,j);
       }
    }
    return;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output10.txt","w",stdout);
    int t,i,j,F,k,x,F1;
    scanf("%d",&t);
    for (k=1;k<=t;k++)
    {
          scanf("%d%d",&r,&c);
          for (i=0;i<r;i++)
              for (j=0;j<c;j++)
              {
                  scanf("%d",&in[i][j]);
                  M[i][j]=-1;
              }
          ctr=0;
          F=1;
          while(F==1)
          {
              F=0;
              for (i=0;i<r;i++)
              {
                  for (j=0;j<c;j++)
                  {
                      //printf("M %d %d %d\n",i,j,M[i][j]);
                      if (M[i][j]==-1)
                      {
                          F=1;
                          x=check(i,j);
                          //printf("%d %d %d\n",i,j,x);
                          if (x==-1)
                          {
                             ctr++;
                             M[i][j]=ctr;
                          }
                          else
                              M[i][j]=x;
                          fill(i,j);
                      }
                  }
              }
          }
          printf("Case #%d:\n",k);
          for (i=0;i<r;i++)
          {
              for (j=0;j<c;j++)
              {
                  printf("%s%c",j==0?"":" ",M[i][j]+96);
              }
              printf("\n");
          }
    }
    //getch();
}
