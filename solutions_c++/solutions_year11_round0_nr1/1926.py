#include "fstream.h"
#include "math.h"
#define int long
using namespace std;
struct sBt
{
 char r;
 int num;
} bts[100];
int main(int argc, char *argv[])
{
 ifstream inp("input.txt");
 ofstream oup("output.txt"); 
 int n;
 inp>>n;
 for (int q=1;q<=n;q++)
 {
  int k,o=-1,b=-1,op=1,bp=1,sec=0;
  bool t=false;
  inp>>k;
  for (int i=0;i<k;i++)
  {
   inp>>bts[i].r>>bts[i].num;
   if (bts[i].r=='B'&&b==-1)
    b=i;
   if (bts[i].r=='O'&&o==-1)
    o=i;
  }
  t=false;
  if (o==-1)
   t=true;
  else
  if (b==-1)
   t=false;
  else
  if (o>b)
   t=true;
  while (o!=-1||b!=-1)
  {
   if (!t)
   {
    int l=labs(bts[o].num-op);
    if (b!=-1)
    {
     if (labs(bts[b].num-bp)<=l+1)
      bp=bts[b].num;
     else
     {
      if (bts[b].num>bp)
       bp+=l+1;
      else
       bp-=l+1;
     }
    }
    op=bts[o].num;
    sec+=l+1;
    int i=o+1;
    while (i<k&&(bts[i].r!='O'))
     i++;
    if (i==k)
     o=-1;
    else
     o=i;
   }
   else
   {
    int l=labs(bts[b].num-bp);   
    if (o!=-1)
    {
     if (labs(bts[o].num-op)<=l+1)
      op=bts[o].num;
     else
     {
      if (bts[o].num>op)
       op+=l+1;
      else
       op-=l+1;
     }
    }
    bp=bts[b].num;
    sec+=l+1;
    int i=b+1;
    while (i<k&&(bts[i].r!='B'))
     i++;
    if (i==k)
     b=-1;
    else
     b=i;
   }
   t=false;
   if (o==-1)
    t=true;
   else
   if (b==-1)
    t=false;
   else
   if (o>b)
    t=true;
  }
  oup<<"Case #"<<q<<": "<<sec<<endl;
 }
 inp.close();
 oup.close();
 return 0;
}
