#include<iostream>
using namespace std;
char word[5000][20];
int L,pat[15];
void readin()
{ 
   char c;
   for(int i=0;i<L;++i)
     {
     scanf(" %c",&c);
      if(c!='(')
        pat[i]=(1<<(c-'a'));
      else
        { pat[i]=0;  
        while((c=getchar())!=')')
            if(c>='a'&&c<='z')
              pat[i]|=(1<<(c-'a'));
                             
        }
     }     
     
}
bool ok(char *s)
{
    for(int i=0;i<L;++i)
      if((pat[i]&(1<<(s[i]-'a')))==0)
         return false;
         return true; 
}
int main()
{
    int CASE=0,N,M,i,cnt;
      freopen("A.in","r",stdin);
      freopen("A.out","w",stdout);
    scanf("%d%d%d",&L,&N,&M);
    for(i=0;i<N;++i)
      scanf("%s",word[i]);
    while(M--)
    {  printf("Case #%d: ",++CASE);
       readin();
       
       for(cnt=i=0;i<N;++i)
        if(ok(word[i]))
          ++cnt;
        printf("%d\n",cnt);
    }
}
