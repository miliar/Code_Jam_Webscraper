#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;

int main(int argc, char *argv[])
{	
	FILE *fin,*fout;
	int cases;
		
	// Fetch # of Input...
	fin = fopen(argv[1],"r");
	if(fin==NULL)
	{cout<<"Unable to open INPUT File.";}
	fout = fopen(argv[2],"w");
	if(fout==NULL)
	{cout<<"Unable to open OUTPUT File.";}

	fscanf(fin,"%d",&cases);
	cout<<"cases="<<cases<<endl;

	int SElst_len, Qlst_len;
	char SE[100][102];
	char Query[1000][102],temp;
	int fre[100];
	for(int i=1;i<=cases;i++)
	{
		// Step_1: Get the SE list length
		fscanf(fin,"%d",&SElst_len);
		temp=fgetc(fin); // reading new line char...

		// Step_2: Fetch all SE strings...
		for(int j=0;j<SElst_len;j++)
		{
			fgets(SE[j],102,fin);
			fre[j]=0;
		}
		
		// Step_3: Get the Query List length;
		fscanf(fin,"%d",&Qlst_len);
		temp=fgetc(fin); // reading new line char...

		// Step_4: Fetch all queries.
		for(int j=0;j<Qlst_len;j++)
		{
			fgets(Query[j],102,fin);
		}

		// Step_5: Find answer.
		int ans=0;
		int j,k,l;
		
		for(j=0;j<Qlst_len;)
		{
//			int match;
			int farthest;
		    
			int SEindex[100]={0};
			for(k=0;k<SElst_len;k++)	
			{
				if(strcmp(Query[j],SE[k])==0)
				{
					SEindex[k]++;//match=k;	
					break;
				}
			}
			for(j=j+1;j<Qlst_len;j++)
			{
				for(l=0;l<SElst_len;l++)	
				{	
					if(strcmp(Query[j],SE[l])==0)
					{
						SEindex[l]++;
						break;
					}
				}
			// Find if all indices are encountered..
				int flag=1;
				for(k=0;k<SElst_len;k++)	
				{	
					if(SEindex[k]==0)
					{	flag=0;	}	
				}
				if(flag==1)
				{cout<<"Farthest ind-"<<j<<endl; ans++; break;}
			}
		}		
					
		// Step_7: Write to File
		fprintf(fout,"Case #%d: %d\n",i,ans);
	}		

	fclose(fin);
	fclose(fout);
	return 0;	

}
