#include<stdio.h>

void main()
{
	FILE* file;
	FILE* fileout;
	fileout=fopen("A-small-attempt0out.txt","wb+");
	file=fopen("A-small-attempt0 (1).in","rb");
	int count=0;
	fscanf(file,"%d",&count);
	for(int i=0;i<count;i++)
	{
		int nA,nB;
		float* pData;
		float* pProb;
		fscanf(file,"%d %d",&nA,&nB);
		pData=new float[nA];
		pProb=new float[nA+2];
		
		for(int j=0;j<nA;j++)
		{
			fscanf(file,"%f",&pData[j]);
		}
		pProb[0]=1.0;
		pProb[nA+1]=1.0;
		for(int i=0;i<nA;i++)
			pProb[0]*=pData[i];
		for(int i=nA;i>=1;i--)
		{
			pProb[nA-i+1]=1.0;
			int j;
			for(j=0;j<i-1;j++)
				pProb[nA-i+1]*=pData[j];
			pProb[nA-i+1]*=(1.0-pData[j]);
		}
		float * result=new float[nA+2];
		float temp=0.0;
		for(int i=1;i<=nA;i++)
			temp+=pProb[i];
		result[0]=pProb[0]*(nB-nA+1)+temp*(nB-nA+1+nB+1);
		
		result[nA+1]=nB+2;
		for(int i=1;i<=nA;i++)
		{
			float temp1=0.0,temp2=0.0;
			for(int j=0;j<=i;j++)
				temp1+=pProb[j];
			for(int k=i+1;k<=nA;k++)
				temp2+=pProb[k];
			result[i]=temp1*(2*i+nB-nA+1)+temp2*(2*i+nB-nA+1+nB+1);
		}
		float min=result[0];
		for(int i=1;i<=nA+1;i++)
		{
			if((result[i]-min)<-0.00001)
				min=result[i];
		}
		//fprintf(fileout,"Case #%d: %f ",i+1,min);
		fprintf(fileout,"Case #%d: %f \r\n",i+1,min);
		delete result,pData,pProb;
	}
	fclose(file);
	fclose(fileout);
}