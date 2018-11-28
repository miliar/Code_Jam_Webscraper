#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
FILE *f,*g;
long long n;
bool isdigit(char ff)
{
 if(ff>='0'&&ff<='9') return 1;
 return 0;
}
int main()
{

f = fopen("A-small.in","r");
g = fopen("izlaz.txt","w");
int c;
fscanf(f,"%d\n",&c);
for(int i = 1; i <= c; i++)
{
vector <int> x;
x.resize(0);
char ch = fgetc(f);
while(isdigit(ch)) { x.push_back((int)((int)ch-(int)'0')); ch = fgetc(f);}
for(int gg = 0; gg < x.size(); gg++) swap(x[gg],x[x.size()-gg-1]);
//for(int xx = 0; xx < x.size(); xx++) fprintf(g,"%d",x[xx]); fprintf(g,"\n");
//while(n>0){ x.insert(x.begin(),n%10); n/=10;  }
if(!next_permutation(x.begin(),x.end()))
{
   // printf("tag");
/*int l = 0;
for(l = 0; l <= 9; l++)
{
    bool found = false;
for(int j = 0; j < x.size(); j++)
{
if(x[j]==l) { found = 1; break;}
}
if(!found) break;
}*/
x.push_back(0);
 //printf(" %d ",l);
sort(&x[0],&x[x.size()]);
//while(x[0]==0) { next_permutation(x.begin(),x.end()); }
for(int b = 0; b < x.size(); b++) if(x[b]!=0) { swap(x[b],x[0]); break; }
}
fprintf(g,"Case #%d: ",i);
for(int xx = 0; xx < x.size(); xx++) fprintf(g,"%d",x[xx]);
fprintf(g,"\n");
}
}

