//---------------------------------------------------------------------------

#pragma hdrstop
#include <stdio.h>
#include <tchar.h>
//---------------------------------------------------------------------------
char mc[100],c;
int n[100],r[100];
int goi,gbi;
int N;
#pragma argsused
void chg(char c)
{
int in;
for (in = 0; in < N; in++)
{
if (mc[in]==c && r[in]==0)
{
if (c=='O')
{
goi=in;
return;
} else
{
gbi=in;
return;
}
}
}
if (c=='O')
{
goi=-1;
} else
{
gbi=-1;
}
return;
}

//---------------------------------------------------------------------------
int _tmain(int argc, _TCHAR* argv[])
{
FILE *fin;
FILE *fout;
int T,i,j,k;
int co,cb,tm;
bool op,bp;

fin=fopen("A-large.in","rt");
fout=fopen("b.txt","wt");
fscanf(fin,"%d",&T);
for (i = 0; i < T; i++)
{
co=1;
cb=1;
fscanf(fin,"%d",&N);
for (j = 0; j < N; j++)
{
fscanf(fin,"%c",&c);
fscanf(fin,"%c",&mc[j]);
fscanf(fin,"%d",&n[j]);
r[j]=0;
}
chg('O');
chg('B');
for (tm = 1; tm < 11000; tm++)
{
op=true;
bp=true;


//оранж вперед
if (n[goi]>co)
{
co++;
op=false;
}
//оранж назад
if (n[goi]<co)
{
co--;
op=false;
}
//голубой вперед
if (n[gbi]>cb)
{
cb++;
bp=false;
}
//голубой назад
if (n[gbi]<cb)
{
cb--;
bp=false;
}

//нажать оранжевый
if (n[goi]==co && (r[goi-1]==1 || goi==0) && op==true && goi!=-1)
{
bp=false;
r[goi]=1;
if (goi==N-1)
{
break;
}
chg('O');
}

//нажать голубой
if (n[gbi]==cb && (r[gbi-1]==1 || gbi==0) && bp==true && gbi!=-1)
{
r[gbi]=1;
if (gbi==N-1)
{
break;
}
chg('B');
}


}
fprintf(fout,"%s","Case #");
fprintf(fout,"%d: ",i+1);
fprintf(fout,"%d\n",tm);

}

fclose(fin);






fclose(fout);
}
//---------------------------------------------------------------------------
