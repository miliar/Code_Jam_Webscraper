#include<iostream>
using namespace std;

__int64 a[31]={0,1,3 ,7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071 ,262143, 
524287 ,1048575, 2097151 ,4194303, 8388607 ,16777215, 33554431 ,67108863, 134217727, 268435455, 536870911, 1073741823};
int main()
{
    __int64 N,K,temp;
    int T;
    FILE *fp,*fp1;
    fp=fopen("11.TXT","r");
    fp1=fopen("ans.txt","w");
    while(fscanf(fp,"%d",&T)!=EOF)
    {
		for(int i=1;i<=T;i++)
		{
			fscanf(fp,"%d%d",&N,&K);
			 temp=a[N];
			fprintf(fp1,"Case #%d: ",i);
			if(K%(a[N]+1)==a[N])
			fprintf(fp1,"ON\n");
			else
			fprintf(fp1,"OFF\n");
		}
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}
