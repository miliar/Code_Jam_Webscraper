#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
int t,c,d,n,j,z;
char p,q,r;
char comb[100][100]; bool op[100][100];
vector<char> state;
int main()
{
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&t);
 for (int i=1;i<=t;++i)
 {
  printf("Case #%d: ",i);
  for (j=0;j<100;++j)
   for (z=0;z<100;++z)
   { comb[j][z]='0'; op[j][z]=false; }
  state.clear();
  scanf("%d ",&c);
  for (j=0;j<c;++j)
  {
   scanf("%c%c%c ",&p,&q,&r);
   comb[p][q]=comb[q][p]=r;
  }
  scanf("%d ",&d);
  for (j=0;j<d;++j)
  {
   scanf("%c%c ",&p,&q);
   op[p][q]=op[q][p]=true;
  }
  scanf("%d ",&n);
  for (j=0;j<n;++j)
  {
   scanf("%c",&p);
   if (state.empty())
   {
    state.push_back(p);
    continue;
   }
   if (comb[p][state[state.size()-1]]!='0') 
    { state[state.size()-1]=comb[p][state[state.size()-1]]; continue; }
   state.push_back(p);
   for (z=0;z<state.size()-1;++z)
    if (op[state[z]][p]) { state.clear(); break; }
  }
  getchar();
  printf("[");
  for (j=0;j<state.size();++j)
  {
   printf("%c",state[j]);
   if (j<state.size()-1) printf(", ");
  }
  printf("]\n");
 }
}