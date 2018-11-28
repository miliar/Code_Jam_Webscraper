#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<set>
using namespace std;

void main ()
{
	FILE *fp,*fp0;
	int casenum;
	int waitt,na,nb,nac,nbc;
	int nash,nasm,nagh,nagm;
	int nbsh,nbsm,nbgh,nbgm;


	if((fp=fopen("B-large.in","r"))==NULL)
	{
		printf("file open error!!\n");
		exit(EXIT_FAILURE);


	}
	if((fp0=fopen("B-large.out","w"))==NULL)
	{
		printf("file open error!!\n");
		exit(EXIT_FAILURE);

	}
	fscanf(fp,"%d",&casenum);
	for (int i=0;i<casenum;i)
	{
		multiset<int> nas,nag,nbs,nbg;
		fscanf(fp,"%d",&waitt);
		fscanf(fp,"%d %d",&na,&nb);
		nac=0;
		nbc=0;
		if(na==0||nb==0)
		{
			i++;
			fprintf(fp0,"Case #%d: %d %d\n",i,na,nb);
		}
		else
		{

			for(int a=0;a<na;a++)
			{
				fscanf(fp,"%d:%d %d:%d",&nash,&nasm,&nagh,&nagm);
				nas.insert((nash*100+nasm));
				if(60<=(nagm+=waitt))
				{
					nagh++;
					nagm-=60;
				}
				nag.insert((nagh*100+nagm));

			}
			for(int a=0;a<nb;a++)
			{
				fscanf(fp,"%d:%d %d:%d",&nbsh,&nbsm,&nbgh,&nbgm);
				nbs.insert((nbsh*100+nbsm));
				if(60<=(nbgm+=waitt))
				{
					nbgh++;
					nbgm-=60;
				}
				nbg.insert((nbgh*100+nbgm));
			}
			multiset<int>::iterator nasit = nas.begin();
			multiset<int>::iterator nagit = nag.begin();
			multiset<int>::iterator nbsit = nbs.begin();
			multiset<int>::iterator nbgit = nbg.begin();

			while(nasit!=nas.end())
			{
				//printf("NAS%d",*nasit);

				if(nbgit!=nbg.end())
				{
					if(*nasit>=*nbgit)
					{
						//printf("NBG%d",*nbgit);
						++nbgit;
						nac++;
					}
					
				}
				++nasit;
				//printf("\n");
				
			}
			while(nbsit!=nbs.end())
			{
				//printf("NBS%d",*nbsit);

				if(nagit!=nag.end())
				{
					if(*nbsit>=*nagit)
					{
						//printf("NAG%d",*nagit);
						++nagit;
						nbc++;

					}
				}
				++nbsit;
				//printf("\n");
				
			}
			/*
			
			while(nbgit!=nbg.end())
			{
				if(nasit!=nas.end())
				{
					if(*nasit<*nbgit)
					{
						nac++;
						++nasit;
					}
					else
					{
						++nasit;
						++nbgit;
					}
				}
				else break;
			}
			while(nagit!=nag.end())
			{
				if(nbsit!=nbs.end())
				{
					if(*nbsit<*nagit)
					{
						nbc++;
						++nbsit;
					}
					else
					{
						++nbsit;
						++nagit;
					}
				}
				else break;
			}*/

			//printf("%d",nbc);
			i++;
			fprintf(fp0,"Case #%d: %d %d\n",i,na-nac,nb-nbc);
		}
		nas.clear();
		nag.clear();
		nbs.clear();
		nbg.clear();


	}

	fclose(fp);
	fclose(fp0);
}
