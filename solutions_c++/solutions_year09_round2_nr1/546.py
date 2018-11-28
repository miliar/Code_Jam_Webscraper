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

struct drvo
{
double w;
drvo *le,*de;//deca
bool list;
char feat[10];
};


int l;
char ch;//ovim citamo
int cc;//
int num;//trenutni broj zivotinja

void c_f(drvo *d)//cita f
{
fscanf(f,"%lf",&d->w);
//printf("\n%lf",d->w);
//PROCITA VREDNOST
fscanf(f,"%c",&ch);

if(ch==')') { d->list = true; return; }

while(ch==' '||ch=='\n')  { fscanf(f,"%c",&ch); }

if(ch==')') { d->list = true; return; }

d->list = false;

//printf("  %d  ",d->list);

int br = 0;

d->feat[br] = ch;
ch = fgetc(f);
while(ch!=' '&&ch!='\n') { br++; d->feat[br] = ch; ch = fgetc(f); }
//for(int gh = br+1; gh < 10; gh++) d->feat[gh] = '1';
//ucitan feature
d->le = new drvo(); d->de = new drvo();
while(ch!='(') { ch = fgetc(f); }
c_f(d->le);
ch = ' ';
while(ch!='(') { ch = fgetc(f); }
c_f(d->de);
ch = ' ';
while(ch!=')') ch = fgetc(f);//ide dok procita svoj ')'
}


struct animal
{
char ime[10];//nebitno
int br;//broj svojstava
char feat[101][10];
};

bool isok(char cc)
{
if(cc>='a'&&cc<='z')  return 1;
return 0;
}

void c_z(animal &a)
{
for(int i = 0; i < 10; i++) a.ime[i] = '1';
fscanf(f,"%s",&a.ime);
fscanf(f,"%d ",&a.br);
for(int i = 1; i <= 100; i++) for(int j = 0; j < 10; j++) a.feat[i][j] = '1';
for(int i = 1; i < a.br; i++) fscanf(f,"%s ",&a.feat[i]);
if(a.br!=0) fscanf(f,"%s",&a.feat[a.br]);
fscanf(f,"\n");//DAKLE MORA NEWLINE NA KRAJ!!!
}

void odredi(drvo *d, animal ana, double &v)
{
v*=d->w;
if(d->list) return;
bool prvi = false;
for(int i = 1; i <= ana.br; i++) if(strcmp(ana.feat[i], d->feat)==0) { prvi = 1; break; }
if(prvi) { odredi(d->le,ana, v); }
else odredi(d->de,ana,v);
}

int main()
{
f = fopen("A-small.in","r");
g = fopen("izlaz.txt","w");
int c;
fscanf(f,"%d\n",&c);
drvo *d = NULL;
animal z[101];
for(int i = 1; i <= c; i++)
{

fprintf(g,"Case #%d: \n",i);

d = new drvo();
fscanf(f,"%d\n",&l);

while((ch=fgetc(f))!='(') {}

c_f(d);//ovde ne ucita


fscanf(f,"%d\n",&num);
for(int an = 1; an <= num; an++)
{
c_z(z[an]);
for(int i1 = 1; i1 <= z[an].br; i1++) printf("%s ",z[an].feat[i1]); printf("\n");
double prob = 1;
odredi(d,z[an],prob);
fprintf(g,"%.10lf\n",prob);
}

}

}
