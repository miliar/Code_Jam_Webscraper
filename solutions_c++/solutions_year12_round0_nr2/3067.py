#include <stdio.h>
#define max(a,b) a>b?a:b

int main()
{
	int T,N,S,p,t,*out;
	FILE *f;
	f=fopen("B-large.in","rb");
	if(!f)
	{
		printf("fail to open file\n");
		return 0;
	}
	fscanf(f,"%d\n",&T);
	out=new int[T];

	int gt1,gt2;
	int ngt;
	for(int i=0;i<T;i++)
	{
		fscanf(f,"%d %d %d",&N,&S,&p);
		gt1=max(0,(p*3-4));
		gt2=max(0,(p*3-2));
		ngt=0;
		out[i]=0;

		for(int j=0;j<N;j++)
		{
			fscanf(f,"%d",&t);
			if(t>=2&&t>=gt1&&t<gt2)
				ngt++;
			else if(t>=gt2)
				out[i]++;
		}
		if(ngt>=S)
			out[i]+=S;
		else
			out[i]+=ngt;
	}
	fclose(f);

	f=fopen("out.txt","wb");
	for(int i=0;i<T;i++)
		fprintf(f,"Case #%d: %d\n",i+1,out[i]);
	fclose(f);
	delete[] out;
	return 0;
}