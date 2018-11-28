#include<cstdio>
using namespace std;

#define  REP(z,n) for(int (z)=0;(z)<(n);++(z))

int main()
{
 int l,d,n;
 char ** w, temp;
 int ** a; // contains received words.
 int * c;
 scanf("%d%d%d", &l, &d, &n);
 scanf("%c", &temp);
 w=new char*[d];
 a=new int*[n];
 c=new int[n];
 REP(i,d) w[i]=new char[l];
 REP(i,n) a[i]=new int[l];
 REP(i,n) c[i]=0;
 REP(i,n) REP(j,l) a[i][j]=0;
 REP(i,d)
 {
  REP(j,l) scanf("%c", &w[i][j]);
  scanf("%c", &temp);
 }
 REP(i,n)
 {
  REP(j,l)
  {
   scanf("%c", &temp);
   if(temp=='(')
   {
    while(1)
    {
     scanf("%c", &temp);
     if(temp==')') break;
     a[i][j]|=(1<<(temp-'a'));
    }
   }
   else a[i][j]|=(1<<(temp-'a'));
  }
  scanf("%c", &temp);
 }
 REP(i,d) REP(j,n) REP(k,l)
 {
  if((1<<(w[i][k]-'a'))&a[j][k]) c[j]++; // letter matches.
  else { c[j]-=k; break; } 
 }
 REP(i,n)
  printf("Case #%d: %d\n", i+1, c[i]/l);
}
