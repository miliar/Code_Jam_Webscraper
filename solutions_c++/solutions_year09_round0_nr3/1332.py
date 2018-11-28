#include<cstdio>
using namespace std;

#define M 10000
#define REP(z,n) for(int (z)=0;(z)<(n);++(z))

int main()
{
 int n, trash; scanf("%d%c", &n, &trash);
 char line[503];
 int count[503][3];
 int p,c;
 REP(q,n)
 {
  p=0;
  c=0;
  REP(a,503) REP(b,3) count[a][b]=0;
  while(1)
  {
   scanf("%c", &line[p]);
   p++;
   if(line[p-1]=='\n') break;
  }
  p--;
  for(int i=p-1;i>=0;--i)
  {
   if(line[i]=='m') count[i][0]=1;
   for(int j=i+1;j<p;++j)
   {
if(line[i]=='m') count[i][0]=1;
if(line[i]=='a') if(line[j]=='m') count[i][0]=(count[i][0]+count[j][0])%M;
if(line[i]=='j') if(line[j]=='a') count[i][0]=(count[i][0]+count[j][0])%M;
if(line[i]==' ') if(line[j]=='j') count[i][0]=(count[i][0]+count[j][0])%M;
if(line[i]=='e') if(line[j]==' ') count[i][0]=(count[i][0]+count[j][0])%M;
if(line[i]=='d') if(line[j]=='e') count[i][0]=(count[i][0]+count[j][0])%M;
if(line[i]=='o') if(line[j]=='d') count[i][0]=(count[i][0]+count[j][0])%M;
if(line[i]=='c') if(line[j]=='o') count[i][0]=(count[i][0]+count[j][0])%M;
if(line[i]==' ') if(line[j]=='c') count[i][1]=(count[i][1]+count[j][0])%M;
if(line[i]=='o') if(line[j]==' ') count[i][1]=(count[i][1]+count[j][1])%M;
if(line[i]=='t') if(line[j]=='o') count[i][0]=(count[i][0]+count[j][1])%M;
if(line[i]==' ') if(line[j]=='t') count[i][2]=(count[i][2]+count[j][0])%M;
if(line[i]=='e') if(line[j]==' ') count[i][1]=(count[i][1]+count[j][2])%M;
if(line[i]=='m') if(line[j]=='e') count[i][1]=(count[i][1]+count[j][1])%M;
if(line[i]=='o') if(line[j]=='m') count[i][2]=(count[i][2]+count[j][1])%M;
if(line[i]=='c') if(line[j]=='o') count[i][1]=(count[i][1]+count[j][2])%M;
if(line[i]=='l') if(line[j]=='c') count[i][0]=(count[i][0]+count[j][1])%M;
if(line[i]=='e') if(line[j]=='l') count[i][2]=(count[i][2]+count[j][0])%M;
if(line[i]=='w') if(line[j]=='e') count[i][0]=(count[i][0]+count[j][2])%M;
   }
  }
  for(int i=0;i<p;++i)
  {
   if(line[i]=='w') c=(c+count[i][0])%M;
// DEBUG   printf("(%c: %d %d %d) ", line[i], count[i][0], count[i][1], count[i][2]);
  }
  printf("Case #%d: %04d\n", q+1, c);
 }
}
