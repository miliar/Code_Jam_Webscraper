#include<stdio.h>
#include<stdlib.h>
int main(int argc, char* argv[])
{
	FILE* fp = fopen("A-large.in","rb");
	FILE* fp2 = fopen("outputLarge1.in","wb");
	if(fp && fp2)
	{
		char line[1024];
		unsigned n1,k1,T;
		fgets(line,1024,fp);
		T = atol(line);
		for( int i = 1; i <= T; i++)
		{
			if(fgets(line,1024,fp) )
			{
				sscanf(line,"%d\t%d",&n1,&k1);
				unsigned long long n = 0;
				unsigned long long k = 0;
				n = n1;
				k = k1;
				if((k & ((1<<n)-1)) == ((1<<n)-1))
				{
					fprintf(fp2,"Case #%d: ON\r\n",i);
				}
				else
				{
					fprintf(fp2,"Case #%d: OFF\r\n",i);
				}
			}
			else
				break;
		}
		fclose(fp);
		fclose(fp2);
	}
	return 1;
}