#include<string.h>
#include<math.h>
#include<iostream.h>
#include<conio.h>
#include<stdlib.h>
#include<stdio.h>

struct vonat
{
    int indul,erkez;
    int milyen,volt;
};

int n,t;
vonat str[500],v;
int h1,h2,m1,m2,na,nb,szam,i,j,k,kem,ka,kb,time,all;
char c;

void main()
{
	FILE *f,*g;
	f=fopen("be.txt","r");
	g=fopen("ki.txt","w");
	fscanf(f,"%d",&n);
    for (i=1;i<=n;i++)
	{
         fscanf(f,"%d",&t);
	     fscanf(f,"%d%d",&na,&nb);
		 for (j=1;j<=na;j++)
		 {
	         fscanf(f,"%d%c%d%d%c%d",&h1,&c,&m1,&h2,&c,&m2);
			 str[j].indul=h1*60+m1;
			 str[j].erkez=h2*60+m2+t;
			 str[j].milyen=1;
			 str[j].volt=0;
		 }
		 for (j=na+1;j<=na+nb;j++)
		 {
	         fscanf(f,"%d%c%d%d%c%d",&h1,&c,&m1,&h2,&c,&m2);
			 str[j].indul=h1*60+m1;
			 str[j].erkez=h2*60+m2+t;
			 str[j].milyen=2;
			 str[j].volt=0;
		 }
		 for(j=1;j<na+nb;j++)
			 for(k=j+1;k<=na+nb;k++)
				 if(str[j].indul>str[k].indul || (str[j].indul==str[k].indul && str[j].erkez>str[k].erkez))
				 {
				     v=str[j];
					 str[j]=str[k];
					 str[k]=v;
				 }
		 ka=0;
		 kb=0;
		 kem=0;
		 while(kem==0)
		 {
			 kem=1;
			 time=-1;
			 for(j=1;j<=na+nb;j++)
			 {
				if(str[j].volt==0 && time==-1)
				{
					kem=0;
					str[j].volt=1;
					if(str[j].milyen==1)
					{
						ka++;
						all=1;
					}
						else 
						{
							kb++;
							all=2;
						}
					time=str[j].erkez;
				}
				else if(str[j].volt==0 && str[j].milyen!=all && time<=str[j].indul)
				{
					time=str[j].erkez;
					str[j].volt=1;
					all=str[j].milyen;
				}
			 }
		 }
		 fprintf(g,"Case #%d: %d %d",i,ka,kb);
		 if(i!=n)
			 fprintf(g,"\n");
	}
	g=fopen("ki.txt","w");
	fclose(f);
	fclose(g);
}