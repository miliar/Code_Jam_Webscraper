#include <stdio.h>
double p;
int N,ii,L,len,i,j,rc,A,n,leng;
char s[500000],ss[500000],sti[500000];
int coor[100000],dax[100000];
char fea[10000][50];
bool aris()
{
int i,j,nn;
bool ind;
for(i=0;i<n;i++)
   {
   nn=0;
   while(fea[i][++nn]);
   if(nn!=leng)continue;
   for(ind=0,j=0;j<leng;j++)
      if(fea[i][j]!=sti[j])
         {
         ind=1;
         break;
         }
   if(!ind) return 1;
   }
return 0;
}
double rek(int co)
{
while(s[co]!='(')co++;
while(s[co]<'0'||s[co]>'9')co++;
double num=0.,k;
int i;
for(i=co;s[i]>='0'&&s[i]<='9';i++)
   num=num*10.+(double)(s[i]-'0');
co=i;
if(s[co]=='.')
   {
   k=0.1;
   co++;
   while(s[co]>='0'&&s[co]<='9')
      {
      num=num+k*((double)(s[co]-'0'));
      k/=10.;
      co++;
      }
   }
while(s[co]==' ')co++;
if(s[co]==')') return num;
leng=0;
while(s[co]>='a'&&s[co]<='z')
   sti[leng++]=s[co++];
while(s[co]!='(')co++;
if(aris())
   return rek(co)*num;
else
   {
   co=dax[co]+1;
   while(s[co]!='(')co++;
   return rek(co)*num;
   }
}
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
scanf("%d\n",&N);
for(ii=1;ii<=N;ii++)
   {
   printf("Case #%d:\n",ii);
   scanf("%d\n",&L);
   len=0;
   for(i=0;i<L;i++)
      {
      s[len++]=' ';
      gets(s+len);
      if(s[len])while(s[++len]);
      }
   rc=0;
   for(i=0;i<len;i++)
      if(s[i]=='(')
         coor[rc++]=i;
      else
         if(s[i]==')')
            dax[coor[--rc]]=i;
   scanf("%d",&A);
   if(A||ii!=N)
      scanf("\n");
   for(i=0;i<A;i++)
      {
      scanf("%s ",ss);
      scanf("%d",&n);
      if(!n)
         scanf("\n");
      else
         {
         for(j=0;j<n;j++)
            scanf("%s",fea[j]);
         scanf("\n");
         }
      p=rek(0);
      printf("%.9lf\n",p);
      }
   }
return 0;
}
