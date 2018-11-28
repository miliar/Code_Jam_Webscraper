#include<cstdio>
#include<algorithm>
using namespace std;
pair<int,int> edOut[100][100], PP;
int edges[102][102][5];
int hst[102][102];
char alp[100][100][100];
int main()
{ int t, i,j,H[100],W[100];
  int N;
  scanf("%d", &N);
 for(t=0;t<N;t++)
{
  pair<int,int> sinks[40];
  int sink=0;
  scanf("%d%d", &H[t], &W[t]);
  for(i=1;i<=H[t];i++)
 {
    hst[i][0]=10001;
    hst[i][W[t]+1]=10001;
 }
  for(i=1;i<=W[t];i++)
 {
    hst[H[t]+1][i]=10001;
    hst[0][i]=10001;
 }
  for(i=1;i<=H[t];i++)
 {
   for(j=1;j<=W[t];j++)
  {
    scanf("%d", &hst[i][j]);
    edges[i][j][1]=0;
    edges[i][j][2]=0;
   edges[i][j][3]=0;
   edges[i][j][4]=0; 
  }
 }
 
 for(i=1;i<=H[t];i++)
 {
   for(j=1;j<=W[t];j++)
 {
    if(hst[i+1][j]>=hst[i-1][j] && hst[i][j-1]>=hst[i-1][j] && hst[i][j+1]>=hst[i-1][j])
    {
       if(hst[i][j]>hst[i-1][j])
      {
        edges[i-1][j][4]=1;}
       else
       {
        PP.first=i;
        PP.second=j;
        sinks[sink++]=PP;
       }
    }
    else if(hst[i+1][j]>=hst[i][j-1] && hst[i][j+1]>=hst[i][j-1] && hst[i-1][j]>=hst[i][j-1])
   {
        if(hst[i][j]>hst[i][j-1])
      { 
        edges[i][j-1][3]=1;}
       else
       {
        PP.first=i;
        PP.second=j;
        sinks[sink++]=PP;
       }
    }
     else if(hst[i][j-1]>=hst[i][j+1] && hst[i+1][j]>=hst[i][j+1] && hst[i-1][j]>=hst[i][j+1])
    {
       if(hst[i][j]>hst[i][j+1])
      {
        edges[i][j+1][2]=1;
      }
      else
      {
        PP.first=i;
        PP.second=j;
        sinks[sink++]=PP;
      }
    }
    else 
    {
       if(hst[i][j]>hst[i+1][j])
      {
        edges[i+1][j][1]=1;
      }
      else
      {
        PP.first=i;
        PP.second=j;
        sinks[sink++]=PP;
      }
    }
  }

}




  for(i=1;i<=H[t];i++)
 {
   for(j=1;j<=W[t];j++)
  {
    alp[t][i][j]='#';
  }
 }
 char alpha='A';
 pair<int,int> Stack[10000];
 int size, cur;
 for(i=0;i<sink;i++)
 {
   Stack[0]=sinks[i];
   size=1;
   while(size!=0)
   {
     cur=size-1;
     if(alp[t][Stack[cur].first][Stack[cur].second]!='#')
     size--;
     else
     for(j=1;j<5;j++)
     {
        if(edges[Stack[cur].first][Stack[cur].second][1]==1)
        {
          Stack[size].first=Stack[cur].first-1;
          Stack[size++].second=Stack[cur].second;
        }
        if(edges[Stack[cur].first][Stack[cur].second][2]==1)
        {
          Stack[size].first=Stack[cur].first;
          Stack[size++].second=Stack[cur].second-1;
        }
        if(edges[Stack[cur].first][Stack[cur].second][3]==1)
        {
          Stack[size].first=Stack[cur].first;
          Stack[size++].second=Stack[cur].second+1;
        }
        if(edges[Stack[cur].first][Stack[cur].second][4]==1)
        {
          Stack[size].first=Stack[cur].first+1;
          Stack[size++].second=Stack[cur].second;
        }
        alp[t][Stack[cur].first][Stack[cur].second]=alpha;
    }
  }
  alpha++;
 }
  for(i=1;i<=H[t];i++)
 {
   for(j=1;j<=W[t];j++)
  {
    if(alp[t][i][j]=='#')
    alp[t][i][j]=alpha++;
  }
 }
 int o, f;
 char Uto='a',goo;
 for(o=0;o<(alpha-'A');o++)
 { f=0;
   for(i=1;i<=H[t];i++)
  { 
    for(j=1;j<=W[t];j++)
   {
     if(f==0 && alp[t][i][j]<='Z' && alp[t][i][j]>='A')
    {f=1;
     goo=alp[t][i][j];
    }
     if(f==1 && alp[t][i][j]==goo)
    {
     alp[t][i][j]=Uto;
    }
   }
  }
 Uto++;
  }
 }
for(t=0;t<N;t++)
{printf("Case #%d:\n", t+1);
 for(i=1;i<=H[t];i++)
 {
   for(j=1;j<=W[t];j++)
  {
    printf("%c ", alp[t][i][j]);
  }printf("\n");
 }
}
return 0;
}


 
