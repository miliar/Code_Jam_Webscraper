#include<stdio.h>
#include<memory.h>
char dict[5001][16];
int l,d,n;
FILE *f, *g;
char tp[16][27];
bool check(int i1)//da li se dict[i1] moze napisati pomocu trenutnog sablona
{
for(int i = 1; i <= l; i++)//trazimo svaki char
{
bool fail = true;
for(int j = 1; j <= tp[i][0]; j++) if(tp[i][j]==dict[i1][i]) { fail = false; break;}
if(fail) return false;
}
return true;
}

void load_pattern()
{
memset(tp,0,sizeof(tp));
char chh;
for(int i = 1; i <= l; i++)
{
fscanf(f,"%c",&chh);
if(chh=='(')
{
chh = fgetc(f);
while(chh!=')')
{
tp[i][0]++; tp[i][tp[i][0]] = chh;
chh = fgetc(f);
}
}
else
{
tp[i][0] = 1; tp[i][1] = chh;
}
}
fgetc(f);
}


int main()
{
f = fopen("A-small.in","r");
g = fopen("ress.txt","w");
fscanf(f,"%d%d%d\n",&l,&d,&n);
for(int i = 1; i <= d; i ++)
{
for(int j = 1; j <= l; j++)
{
dict[i][j] = fgetc(f);
}
fgetc(f);
}

for(int i = 1; i <= n; i++)
{
load_pattern();
int res = 0;
for(int i = 1; i <= d; i++) if(check(i)) res++;
fprintf(g,"Case #%d: %d\n",i,res);
}

}
