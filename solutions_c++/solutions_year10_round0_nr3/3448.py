
#include<stdio.h>


//#define LMT 256

long long compt(int r,int n,int k,int*buf)
{
	long long sum=0;

	int *buf_bk=new int [n];
	for(int ii=0;ii<n;ii++)
		buf_bk[ii]=buf[ii];

	for(int ii=0;ii<r;ii++)
	{
		int ss=0;
		if(ii!=0)
		{
			for(int jj=0;jj<n;jj++)
				if(buf_bk[jj]!=buf[jj])
						{ss=1;break;}

			if(ss==0)
			{
				sum*=r/(ii);
				ii=r-(r%ii);
				if(ii>=r)break;
			}
			
		}

		int p=0,i=0;
		while(i<n)
		{
			if(p+buf_bk[i]>k)break;
			p+=buf_bk[i++];
		}
		sum+=p;
		if(i==n)continue;
		int *tmp=new  int[i];
		for(int jj=0;jj<i;jj++)
			tmp[jj]=buf_bk[jj];
		for(int jj=0;jj<i;jj++)
			for(int kk=i+jj;kk<n;kk+=i)
				buf_bk[kk-i]=buf_bk[kk];
		for(int jj=0;jj<i;jj++)
			buf_bk[jj+n-i]=tmp[jj];
		delete[]tmp;

	}

	delete[]buf_bk;
	return sum;
}

int main(int argc, char* argv[])
{
	int l,i,j;
	char ch,pch,cch;
	FILE*fr,*fw;
	char*strr,*strw;
	int N,K,R;
	strr= "C-small-attempt2.in";
	strw= "C-small-attempt2.out";

	fr=fopen(strr,"r");
	if(fr==NULL)
	{
		printf("fopen failed:%s\n",strr);
		return 1;
	}
	fw=fopen(strw,"w");
	if(fr==NULL)
	{
		printf("fopen failed:%s\n",strw);
		fclose(fr);
		return 2;
	}

	ch=fgetc(fr);
	l=0;
	while(ch>='0'&&ch<='9')
	{
		l*=10;
		l+=ch-'0';
		ch=fgetc(fr);
	}
	i=0;
	while(++i<=l)
	{
		pch=0;
		fprintf(fw,"Case #%d: ",i);

		fscanf(fr,"%d",&R);
		fscanf(fr,"%d",&K);
		fscanf(fr,"%d",&N);
		int*buf=new int[N];
		for(int ii=0;ii<N;ii++)
			fscanf(fr,"%d",&buf[ii]);

		fprintf(fw,"%lld",compt(R,N,K,buf));
		delete[]buf;
		//fgets(buf,LMT,fr);
		fputc('\n',fw);
	}
	fclose(fw);
	fclose(fr);

	return 0;
}

