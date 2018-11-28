#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <iostream>
#define u 10000
using namespace std;
map <string, long> a;

int t,i,cur,n,l,k,j,L,r,r2;

double prob[u];
char ch;
string s,S[u];

int main()
{
 freopen("a.in","r",stdin);
 freopen("A.out","w",stdout);
 scanf("%d\n",&t);

 for (i=1; i<=t;i++)
 {
  a.clear();
  printf("Case #%d: \n",i);
  scanf("%d\n",&n);
  for (l=0; l<5*n; l++) prob[l]=-1;
  prob[0]=0;
  cur=0;
  for (l=0; l<n; l++)
   {
     scanf("%c",&ch); // cout<<ch<<endl;
     while (ch!='(' && ch!=')') scanf("%c",&ch);
     if (ch=='(')
     {
          cur*=2;
          if (prob[cur]!=-1) cur++;
          cin>>prob[cur];
          cin>>s; //cout<<s<<" "<<prob[cur]<<" "<<cur<<endl;
          L=s.size();
          if (s[L-1]!=')')  S[cur]=s; else
          for (k=0; k<L; k++)
           if (s[k]==')') cur/=2;

     } else
     {
      cur/=2;
      scanf("%c",&ch);
      while (ch!='\n')
      { if (ch==')') cur/=2; scanf("%c",&ch); }
     }

    //scanf("\n");
  }


  double  ans=1;
   scanf("%d",&r);
   for (l=0; l<r; l++)
    { cin>>s; ans=1; a.clear();
       scanf("%d",&r2);
       for (k=0; k<r2; k++)
        { cin>>s;  a[s]=1; }

       cur=1;
       while (prob[cur]!=-1)
       {
           ans*=prob[cur];
           if ( a[S[cur]]==1 )
           cur*=2; else cur=cur*2+1;
       }
      printf("%.7f\n",ans);
      scanf("\n");
     }

  }

 return 0;
}
