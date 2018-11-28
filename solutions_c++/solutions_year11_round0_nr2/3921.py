#include <stdio.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;

char jeden,druhy;
char arr[100];
char b[100],nb[50];
char opp[100];
int up,lo,l,c,n,d;

void cekni()
{

char zly=arr[l-1];
bool bug=false;

for (int i=0;i<l-1;i++)
    {
    for (int j=0;j<d;j++)
        {
        if (zly==opp[j*2])
           if (arr[i]==opp[j*2+1])
              bug=true;
              
        if (zly==opp[j*2+1])
           if (arr[i]==opp[j*2])
              bug=true;
            
        if (bug) j=d;
        }
        
    if (bug) i=l;
    }

if (bug) l=0;
}

int zmiesaj(int l)
{
if (l>1)
   {
           if (arr[l-1]>arr[l-2])
              {
              jeden=arr[l-2];
              druhy=arr[l-1];
              }
           else
              {
              druhy=arr[l-2];
              jeden=arr[l-1];
              }
              
           lo=0;
           up=c;
           int med;
           
           while (lo<=up)
                 {
                 med=(lo+up)/2;
                 if (b[med*2]==jeden)
                    lo=up+1;
                 else if (b[med*2]>jeden)
                      up=med-1;
                 else lo=med+1;
                 }
           
           if (jeden==b[med*2])
           if (druhy==b[med*2+1])
              {
              l--;
              arr[l-1]=nb[med];
              zmiesaj(l);
              }
   }
return(l);
}

int main()
{
int t;
FILE *in = fopen("B.in","r");
FILE *out = fopen("B-small.out","w");
fscanf(in,"%d",&t);

//scanf("%d",&t);
char h;
for (int ca=0;ca<t;ca++)
    {
    fscanf(in,"%d",&c);
    //scanf("%d",&c);
    
    for (int i=0;i<c;i++)
        {
        fscanf(in,"%c",&h);
        fscanf(in,"%c%c%c",&b[2*i],&b[2*i+1],&nb[i]);
        }
    
    fscanf(in,"%d",&d);
    for (int i=0;i<d;i++)
        {
        fscanf(in,"%c",&h);
        fscanf(in,"%c%c",&opp[2*i],&opp[2*i+1]);
        }

    char inv[n];
    fscanf(in,"%d",&n);
    fscanf(in,"%c",&h);
    for (int i=0;i<n;i++)
        {
        fscanf(in,"%c",&inv[i]);
        }
   
    for (int i=0;i<c;i++)
        {
        if (b[2*i]>b[2*i+1])
           swap(b[2*i],b[2*i+1]);
        }
    
    for (int i=0;i<c-1;i++)
    for (int j=i+1;j<c;j++)
        {
        if (b[2*i]>b[2*j])
           {
           swap(b[2*i],b[2*j]);
           swap(b[2*i+1],b[2*j+1]);
           swap(nb[i],nb[j]);
           }
        }
        
    for (int i=0;i<d;i++)
        {
        if (opp[2*i]>opp[2*i+1])
           swap(opp[2*i],opp[2*i+1]);
        }
    
    for (int i=0;i<d-1;i++)
    for (int j=i+1;j<d;j++)
        {
        if (opp[2*i]>opp[2*j])
           {
           swap(opp[2*i],opp[2*j]);
           swap(opp[2*i+1],opp[2*j+1]);
           }
        }   
        
    l=0;
   
    
    
    
    for (int i=0;i<n;i++)
        {
        arr[l]=inv[i];
        l++;
        if (l>1)
           {
           l=zmiesaj(l);
           cekni();
           }
        }
   
   
   

    fprintf(out,"Case #%d: [",ca+1);
    if (l==0){}
    else if (l==1) {
                   fprintf(out,"%c",arr[l-1]);
                   }
    else 
         {
         for (int i=0;i<l-1;i++)
             fprintf(out,"%c, ",arr[i]);
             fprintf(out,"%c",arr[l-1]);
         }
    fprintf(out,"]\n");
   }
        
return 0;
}
