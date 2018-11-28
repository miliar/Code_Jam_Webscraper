#include <stdio.h>
#include <vector>

struct DATE
{
	int p1,p2;
	bool operator==(DATE& tmp)
	{
		return (p1==tmp.p1&&p2==tmp.p2)||(p1==tmp.p2&&p2==tmp.p1);
	}
	
};

int main()
{
	FILE *f=fopen("C-small-attempt0.in","rb");
	if(!f)
	{
		printf("Fail to open file\n");
		return 0;
	}
	int T,A,B,*out;
	fscanf(f,"%d\n",&T);
	out=new int[T];
	std::vector<DATE> vout;
	
	for(int i=0;i<T;i++)
	{
		vout.clear();
		fscanf(f,"%d %d\n",&A,&B);
		if(A<10)
		{
			out[i]=0;
			continue;
		}

		int k=1;
		int temp=A;
		while(A/k)
			k*=10;
		for(int j=A;j<=B;j++)
		{
			for(int m=10;m<=k/10;m*=10)
			{
				bool flag=true;
				int newnum=(j%m)*(k/m)+j/m;
				if(newnum==j)
					continue;
				if(newnum<=B&&newnum>=A)
				{
					DATE tm;
					tm.p1=j;tm.p2=newnum;
					for(std::vector<DATE>::iterator it=vout.begin();it!=vout.end();it++)
					{
						if(*it==tm)
						{
							flag=false;
							break;
						}
					}
					if(flag)
						vout.push_back(tm);
				}
			}
		}
		out[i]=vout.size();
	}
	fclose(f);

	f=fopen("out.txt","wb");
	for(int i=0;i<T;i++)
		fprintf(f,"Case #%d: %d\n",i+1,out[i]);
	fclose(f);

	delete[] out;
	return 0;
}