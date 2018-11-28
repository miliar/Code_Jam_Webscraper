#include <stdio.h>
//#include <string.h>
int main(int argc,char **argv)
{
	if(argc<2)
	{
		return -1;
	}
	FILE * input=fopen(argv[1],"r");
	if(input==NULL)
	{
		return -1;
	}
	char c;
	int T;
	int N;
	int K=0;
	int *mas;
	int *pos;
	int temp;
	fscanf(input,"%d",&T);
	for(int t=0;t<T;t++)
	{
		fscanf(input,"%d",&N);
		mas = new int[N];
		pos = new int[N];
		for(int i=0;i<N;i++) mas[i]=0;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N+1;j++)
			{
				fscanf(input,"%c",&c);
				if(c=='1')
				{
					mas[i]=j;
				}
			}
		}
		for(int i=0;i<N;i++)
		{pos[i]=mas[i]-i-1;
	//	printf("%d pos%d=%d\n",t,i,pos[i]);
		}

////////////////////////
		K=0;
		for(int i=0;i<N;i++)
		{
			if(pos[i]>0)
			{
				for(int j=1;j<=pos[i];j++)
				{
					if(pos[i+j]>=0)
					{
	//				printf("Not good %d\n",i+j+1);
					for(int f=1;f+i<N;f++){	
					if(pos[i+f]<=-f)
					{
	//					printf("GOOD %d\n",i+f);
						for(int p=f;p>0;p--)
						{
							temp=mas[i+p-1];
							mas[i+p-1]=mas[i+p];
							mas[i+p]=temp;
							K++;
						}
						for(int p=0;p<N;p++) pos[p]=mas[p]-p-1;
					break;
					}}
					}
				}

			for(int j=1;j<=pos[i];j++){
				if(mas[i+j-1]>mas[i+j])
				K++;
				temp=mas[i+j];
				mas[i+j]=mas[i+j-1];
				mas[i+j-1]=temp;}
			for(int p=0;p<N;p++) pos[p]=mas[p]-p-1;
			}
		}
	/*	for(int i=0;i<N;i++)
		{
			printf("%d ",mas[i]);
		}
		printf("\n");
		printf("%d K=%d\n",t,K);
		for(int j=0;j<N;j++)
		{
			for(int i=0;i<N-1;i++)
			{
				if(mas[i]>i+1 && mas[i]>mas[i+1])
				{
					K++;
					temp=mas[i];
					mas[i]=mas[i+1];
					mas[i+1]=temp;
				printf("%d %d %d\n",t,mas[i],mas[i+1]);
				}
			}
		}*/
		delete[] mas;
		delete[] pos;
		printf("Case #%d: %d\n",(t+1),K);
	}
	return 0;
}
