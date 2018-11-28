#include <stdio.h>

unsigned int crc16(char *buf){
	int j;
	unsigned int temp, flag;
	temp = 0xFFFF;
	while(*buf!=0){
		temp = temp ^ *buf++;
		for (j = 1; j <= 8; j++){
			flag = temp & 0x0001;
			temp = temp >> 1;
			if (flag) temp = temp ^ 0xA001;
		}
	}
    return temp;
}

void getline(FILE * f,char * str)
{
	char c,*s=str;
	c=fgetc(f);
	while(((c==10)||(c==13))&&(!feof(f)))c=fgetc(f);
	while((c!=10)&&(c!=13)&&(!feof(f)))
	{
		*(s++)=c;
		c=fgetc(f);
	}
	*s=0;
}

int main()
{
	FILE *in,*out;
	in=fopen("input.txt","r");
	out=fopen("output.txt","w");
	
	int N,n;
	fscanf(in,"%i",&N);
	for(n=0;n<N;n++)
	{
		unsigned int engines[1000][2]={{0},{0}};
		int S,t;
		fscanf(in,"%i",&S);
		for(t=0;t<S;t++)
		{
			char str[101]={0};
			getline(in,str);
			engines[t][0]=crc16(str);
		}
		int Q,switches=0;
		fscanf(in,"%i",&Q);
		for(t=0;t<Q;t++)
		{
			char str[101]={0};
			getline(in,str);
			int j;
			unsigned int crc=crc16(str);
			for(j=0;j<S;j++)
			{
				if(engines[j][0]==crc)
				{
					if(engines[j][1]==0)
					{
						engines[j][1]=1;
						int i,sw=0;
						for(i=0;i<S;i++)
						{
							if(engines[i][1]!=0)sw++;
						}
						if(sw==S)
						{
							switches++;
							for(i=0;i<S;i++)engines[i][1]=0;
						}
						engines[j][1]=1;
					}
					break;
				}
			}
		}
		fprintf(out,"Case #%i: %i\n",n+1,switches);
	}
	fclose(in);
	fclose(out);
	return 0;
}