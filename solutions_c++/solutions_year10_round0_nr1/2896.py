#include<stdio.h>
#include<math.h>
main()
{
	long N=0,K=0,count;
	int j,T;
	char temp_ch;
	char *str;
	
	
	FILE *pFile,*pFile1;

	pFile=fopen("C:\\Documents and Settings\\kaku\\Desktop\\A-large.in","r");
	fscanf(pFile,"%d",&T);
	
	temp_ch=fgetc(pFile);

	for(j=1;j<=T;j++)
	{
		
		fscanf(pFile,"%ld",&N);
		temp_ch=fgetc(pFile);

		
		fscanf(pFile,"%ld",&K);
		temp_ch=fgetc(pFile);
		count=pow(2,N);
		
		count=(K+1)%count;
		if(count==0)
		str="ON";
		else
		str="OFF";
		pFile1=fopen("C:\\Documents and Settings\\kaku\\Desktop\\output.txt","a");
		fprintf(pFile1,"Case #%d: %s\n",j,str);
		fclose(pFile1);
		
	}
	fclose(pFile);

}

