#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
using namespace std;
char grid[100][100];
char grid2[100][100];
char arr[100]="";
int di[]={-1,-1,1,1};
int dj[]={-1,1,-1,1};
int main()
{ int T;
  scanf("%d\n",&T);
  for(int t=0;t<T;t++)
  { int N,K;
    scanf("%d %d\n",&N,&K);
    for(int i=0;i<N;i++)
    { scanf("%s\n",arr);
      for(int j=0;j<N;j++)
      grid[i][j]=arr[j];
    }
    for(int i=0;i<N;i++)
    for(int j=0;j<N;j++)
    grid2[j][N-i-1]=grid[i][j];
    /*printf("\n");
    for(int i=0;i<N;i++)
    { for(int j=0;j<N;j++)
      printf("%c",grid2[i][j]);
      printf("\n");
    }*/
    for(int j=0;j<N;j++)
    { string str="";
      for(int i=0;i<N;i++)
      { if(grid2[i][j]!='.')
        str+=grid2[i][j];
        grid2[i][j]='.';
      }
      int len=str.size();
      //printf("%s\n",str.c_str());
      for(int i=len-1;i>=0;i--)
      grid2[N+i-len][j]=str[i];
    }
    /*printf("\n\n");
    for(int i=0;i<N;i++)
    { for(int j=0;j<N;j++)
      printf("%c",grid2[i][j]);
      printf("\n");
    }*/
    int wb=0,wr=0;
    for(int i=0;i<N;i++)
    { for(int j=0;j<N;)
      if(grid2[i][j]!='B')
      j++;
      else
      { int cnt=0;
        while(j<N&&grid2[i][j++]=='B')
        cnt++;
        wb=max(wb,cnt);
      }
    }
    for(int j=0;j<N;j++)
    { for(int i=0;i<N;)
      if(grid2[i][j]!='B')
      i++;
      else
      { int cnt=0;
        while(i<N&&grid2[i++][j]=='B')
        cnt++;
        wb=max(wb,cnt);
      }
    }
    for(int i=0;i<N;i++)
    for(int j=0;j<N;j++)
    if(grid2[i][j]=='B')
    { for(int k=0;k<4;k++)
      for(int ni=i,nj=j;ni>=0&&nj>=0&&ni<N&&nj<N;)
      if(grid2[ni][nj]!='B')
      { ni+=di[k];
        nj+=dj[k];
      }
      else
      { int cnt=0;
        while(ni>=0&&ni<N&&nj>=0&&nj<N&&grid2[ni][nj]=='B')
        { cnt++;
          ni+=di[k];
          nj+=dj[k];
        }
        wb=max(wb,cnt);
      }
    } 
    //For R
    for(int i=0;i<N;i++)
    { for(int j=0;j<N;)
      if(grid2[i][j]!='R')
      j++;
      else
      { int cnt=0;
        while(j<N&&grid2[i][j++]=='R')
        cnt++;
        wr=max(wr,cnt);
      }
    }
    for(int j=0;j<N;j++)
    { for(int i=0;i<N;)
      if(grid2[i][j]!='R')
      i++;
      else
      { int cnt=0;
        while(i<N&&grid2[i++][j]=='R')
        cnt++;
        wr=max(wr,cnt);
      }
    }
    for(int i=0;i<N;i++)
    for(int j=0;j<N;j++)
    if(grid2[i][j]=='R')
    { for(int k=0;k<4;k++)
      for(int ni=i,nj=j;ni>=0&&nj>=0&&ni<N&&nj<N;)
      if(grid2[ni][nj]!='R')
      { ni+=di[k];
        nj+=dj[k];
      }
      else
      { int cnt=0;
        while(ni>=0&&ni<N&&nj>=0&&nj<N&&grid2[ni][nj]=='R')
        { cnt++;
          ni+=di[k];
          nj+=dj[k];
        }
        wr=max(wr,cnt);
      }
    }   
    if(wr>=K&&wb>=K)
    printf("Case #%d: Both\n",t+1);
    else if(wr>=K)
    printf("Case #%d: Red\n",t+1);
    else if(wb>=K)
    printf("Case #%d: Blue\n",t+1);
    else
    printf("Case #%d: Neither\n",t+1);
  }
}
