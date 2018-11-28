#include <cstdio>
#include <vector>

using namespace std;
FILE *fin;
FILE *fout;
int t;
int cas;
int c,d,n;
struct Cob
{
	char c1;
	char c2;
	char cmb;
};

struct Opp
{
	char o1;
	char o2;
};

Cob cob[38];
Opp opp[30];

char invo[110];
char data[110];
int p;


void init()
{
	int i;
	Cob tcob;
	Opp topp;


	fscanf(fin,"%d",&c);
	char temp[4];
	for(i = 1;i <= c;i++)
	{
		fscanf(fin,"%s",&temp);
		tcob.c1 = temp[0];
		tcob.c2 = temp[1];
		tcob.cmb = temp[2];
		cob[i] = tcob;
	}


	fscanf(fin,"%d",&d);

	for(i = 1;i <= d;i++)
	{
		fscanf(fin,"%s",&temp);
		topp.o1 = temp[0];
		topp.o2 = temp[1];
		opp[i] = topp;
	}
	
//	for(i = 1;i <= d;i++)
//	{
//		printf("%c %c \n",opp[i].o1,opp[i].o2);
//	}


	fscanf(fin,"%d ",&n);
	
	for(i = 1;i <= n;i++)
	{
		fscanf(fin,"%c",&invo[i]);
	}
}


void combine()
{
	int i;
	if(p >= 2)
	{
		for(i = 1;i <= c;i++)
		{
			if(data[p] == cob[i].c1 && data[p-1] == cob[i].c2  )
			{
				p --;
				data[p] = cob[i].cmb;
			}

			else if(data[p] == cob[i].c2 && data[p-1] == cob[i].c1)
			{
				p --;
				data[p] = cob[i].cmb;
			}
		}
	}
}


void opposed()
{
	int i;
	int j;
	int k;
	int flag = 0;
	for(i = 1;i <= p; i ++)
	{
		for(j = 1;j <= d;j++)
		{
			if(data[i] == opp[j].o1)
			{
				for(k = 1;k <= p;k++)
				{
					if(data[k] == opp[j].o2 && i != k)
					{
						p = 0;
						flag = 1;

						break;
					}
				
				}			
			}

			else if(data[i] == opp[j].o2)
			{
				for(k = 1;k <= p;k++)
				{
					if(data[k] == opp[j].o1 && i != k)
					{
						p = 0;
						flag = 1;

						break;
					}
				
				}			
			}

			if(flag) break;
		
		}

		if(flag ) break;
	
	}	


}

void work()
{
	int i;
	char tt;
	p = 0;
	for(i = 1;i <= n;i++)
	{
		tt = invo[i];
		p++;
		data[p] = tt;

		combine();

		opposed();
	//	printf("p = %d\n",p);
	}

}


int main()
{

	fin = fopen("B-large.in","rb");
	fout = fopen("b.out","wb");

	int i;
	fscanf(fin,"%d",&t);
	for(cas = 1;cas <= t;cas ++)
	{
		init();
		work();
	//	printf("p = %d\n",p);
		fprintf(fout,"Case #%d: [",cas);
		//printf("Case #%d: [",cas);
		for(i = 1;i <= p-1;i++)
		{
			fprintf(fout,"%c, ",data[i]);
			//printf("%c, ",data[i]);
		}
		if(p)
		{
			fprintf(fout,"%c]\n",data[p]);
			//printf("%c]\n",data[p]);
		}	
		else
		{
			//printf("]\n");
			fprintf(fout,"]\n");
		}
	}

	return 0;
}
