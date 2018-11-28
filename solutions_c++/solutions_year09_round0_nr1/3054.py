#include<cstdio>
#include<cstring>
#include<cstdlib>
int D,L,N;
char data[5000][16],input[5000];
int valid(int idx)
{
 int l,i,ok,j;
 l = strlen(input);
 for(i=0,j=0;j<l;++i,++j)
  {
   if(input[j]=='(')
    {
     ++j;
     ok=0;
     while(j<l && input[j]!=')')
      if(input[j++]==data[idx][i])
        ok=1;
     if(!ok)
      return 0;
    }
   else if(data[idx][i]!=input[j])
      return 0;
  }
 return 1; 
}
int main()
{
 freopen("inp1.txt", "rt", stdin);
 freopen("out.txt", "wt", stdout);
 int i,j,res,cases;
 scanf("%d%d%d",&L,&D,&N);
 getchar();
 for(i=0;i<D;++i)gets(data[i]);
 for(cases=1,res=0;cases<=N;++cases,res=0)
  {
   gets(input);
   for(j=0;j<D;++j)if(valid(j))res++;
   printf("Case #%d: %d\n",cases,res);  
  }
 system("pause");
}


