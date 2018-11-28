#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
 
int main()
{

FILE *fp1,*fp2;
int T,c,d,n;
char comb[40][3];
char opp[30][2];
vector<char> elements;
int i,j,l,k,g,x,index,h,o,flag;
char ch,sp,p;

fp1=fopen("B-large.in","r");
fp2=fopen("B-large.out","w");
fscanf(fp1,"%d",&T);

for (i=1;i<=T;i++)
{
fscanf(fp1,"%d",&c);

for (k=0;k<c;k++)
fscanf(fp1,"%s",comb[k]);

fscanf(fp1,"%d",&d);
for (j=0;j<d;j++)
fscanf(fp1,"%s",opp[j]);

fscanf(fp1,"%d",&n);
fscanf(fp1,"%c",&sp);
index=-1;
for (l=0;l<n;l++)
{
fscanf(fp1,"%c",&ch);
elements.push_back(ch);
index++;

if (index>0)
{
flag=0;
for (x=0;x<c;x++)
{
if ((elements[index]==comb[x][0] && elements[index-1]==comb[x][1]) || (elements[index]==comb[x][1] && elements[index-1]==comb[x][0]))
{
elements.pop_back();
elements.pop_back();
elements.push_back(comb[x][2]);
flag=1;
index=index-1;
break;
}
}
if (flag==0)
{
p=elements[index];
for (h=0;h<d;h++)
{
if (opp[h][0]==p)
{
for (o=index-1;o>=0;o--)
{
if (elements[o]==opp[h][1])
{elements.clear();
index=-1;
break;
}
}
}

if (opp[h][1]==p)
{
for (o=index-1;o>=0;o--)
{
if (elements[o]==opp[h][0])
{elements.clear();
index=-1;
break;
}
}
}
if (index==-1)
break;
}
} 
}
}
if (index==-1)
fprintf(fp2,"Case #%d: []\n",i);
else if (index==0)
fprintf(fp2,"Case #%d: [%c]\n",i,elements[0]);
else
{
fprintf(fp2,"Case #%d: [%c,",i,elements[0]);
for (g=1;g<=(index-1);g++)
fprintf(fp2," %c,",elements[g]);
fprintf(fp2," %c]\n",elements[g]);
}
elements.clear();
index=-1;flag=0;
}
fclose(fp1);
fclose(fp2);
return 0;
}





