#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>

using namespace std;

int ni=0,nc=0;

int compute(vector<int> value,vector<int> gates, int pos)
{
    int sum=0;
    if(pos<ni)
    {
    sum=(compute(value,gates,((pos+1)*2)-1)+compute(value,gates,((pos+1)*2)));
    if(gates[pos]==1)
        value[pos]=sum/2;
    else if(sum>0)
        value[pos]=1;
    else
        value[pos]=0;
    }
    //printf("%d %d sum=%d gate=%d\n",pos,value[pos],sum,gates[pos]);
    return value[pos];
}

int dochange(int j,vector<int> value,vector<int> gates,vector<int> change,int v)
{
    int res=0;
    if(j>0)
    {
        for(int i=0;i<ni;i++)
        {
            if(change[i]==1)
            {
                gates[i]=1-gates[i];
                change[i]=0;
                res=dochange(j-1,value,gates,change,v);
                gates[i]=1-gates[i];
            }
            if(res==1)
                return 1;
        }

    }
    else
    {
        if(v==compute(value,gates,0))
            return 1;
        else
            return 0;
    }
}

int main()
{

  FILE *f = fopen("A-small.in","r");
  int n;

  if(f==NULL)
    printf("no file");
  fscanf(f,"%d",&n);
  
  for(int i=0;i<n;i++)
  {
   int m, v;
   vector<int> gates,change;
   //printf("%d ###\n",i+1);

   fscanf(f,"%d %d",&m,&v );
   //printf("m=%d v=%d\n",m,v);
   vector<int> value;
   for(int j=0;j<(m-1)/2;j++)
   {
    int g,c;
    fscanf(f,"%d %d",&g,&c);
    //printf("g=%d c=%d\n",g,c);
    gates.push_back(g);
    change.push_back(c);
    if (c==1)
        nc++;
    value.push_back(0);
   }
   ni=(m-1)/2;
   for(int j=0;j<(m+1)/2;j++)
   {
    int val;
    fscanf(f,"%d",&val);
    value.push_back(val);
   }
   int root,ans=-1;
   root=compute(value,gates,0);
   //printf("root=%d v=%d\n",root,v);
   if(root==v)
    ans=0;
   else
   {
   for(int j=1;j<nc;j++)
   {
     //printf("%d\n",j);
     if(dochange(j,value,gates,change,v)==1)
     {
        ans=j;
        break;
     }
   }
   }

   FILE *fout=fopen("A-small.out","a");
   if(ans==-1)
    fprintf(fout,"Case #%d: IMPOSSIBLE\n",(i+1));
   else
    fprintf(fout,"Case #%d: %d\n",(i+1),ans);
   fclose(fout);
   //printf("\n\n");
  }

  fclose(f);
  //cin.get();
}
