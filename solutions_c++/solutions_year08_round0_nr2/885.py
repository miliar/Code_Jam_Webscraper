#include <stdio.h>
#include <string.h>

#define MAX 30

int ab[205][2], ba[205][2];//caile initiala si reverse
char line[105];


int n, na, nb, t, trenuria, trenurib, nv;

int h1, m1, h2, m2;//timp temp

FILE *f_in, *f_out;

int print_solutie(int id)
{
	fprintf(f_out,"Case #%d: %d %d\n",id+1,trenuria,trenurib);
	return 0;
}

int rezolva()
{
	f_in = fopen("B-large.in","r");
	f_out = fopen("output.txt","w");
	fscanf(f_in,"%d",&n);
	char temp;
	fscanf(f_in,"%c",&temp);//pentru '\n'
	for(int i=0; i < n; i++)
	{

		memset(ab, 0, sizeof(ab));
		memset(ba, 0, sizeof(ba));


		
		trenuria = 0;
		trenurib = 0;
		
		fscanf(f_in,"%d",&t);//timpul de intoarcere
		fscanf(f_in,"%d %d",&na,&nb);//cate curse din A si cate din B
		fscanf(f_in,"%c",&temp);//pentru '\n'
		nv = 0;
		for(int i=0;i<na;i++)
		{
			memset(line, 0, sizeof(line));
			fgets(line,105,f_in);
			
			sscanf(line,"%d:%d %d:%d",&h1,&m1,&h2,&m2);
			m1 = m1 + h1*60;
			m2 = m2 + h2*60 + t;
			
			ab[nv][0] = 0;
			ba[nv][0] = 1;
			
			ab[nv][1] = m1;
			ba[nv][1] = m2;
			
			nv = nv + 1;
			//fscanf(f_in,"%c",&temp);//pentru '\n'
		}	
		for(int i=0;i<nb;i++)
		{
			memset(line, 0, sizeof(line));
			fgets(line,105,f_in);
			
			sscanf(line,"%d:%d %d:%d",&h1,&m1,&h2,&m2);
			m1 = m1 + h1*60;
			m2 = m2 + h2*60 + t;
			
			ab[nv][0] = 1;
			ba[nv][0] = 0;
			
			ab[nv][1] = m2;
			ba[nv][1] = m1;
			
			nv = nv + 1;
			//fscanf(f_in,"%c",&temp);//pentru '\n'
		}
		//trebuie sa sortez ab si ba; atentie la ab[0] si ba[0] cand elementele sunt egale, are prioritete cel cu 1
		
		for(int i=0;i<nv-1;i++)
			for(int j=i+1;j<nv;j++)
				if( (ab[j][1] < ab[i][1]) || (ab[j][1] == ab[i][1] && ab[j][0] > ab[i][0]))
				{
					//interschimb
					int t1,t2;
					t1 = ab[j][1];
					t2 = ab[j][0];
					
					ab[j][0] = ab[i][0];
					ab[j][1] = ab[i][1];
					
					ab[i][0] = t2;
					ab[i][1] = t1;
				}
		
		for(int i=0;i<nv-1;i++)
			for(int j=i+1;j<nv;j++)
				if( (ba[j][1] < ba[i][1]) || (ba[j][1] == ba[i][1] && ba[j][0] > ba[i][0]))
				{
					//interschimb
					int t1,t2;
					t1 = ba[j][1];
					t2 = ba[j][0];
					
					ba[j][0] = ba[i][0];
					ba[j][1] = ba[i][1];
					
					ba[i][0] = t2;
					ba[i][1] = t1;
				}
		//aici am totul sortat si ma apuc sa numar AB si BA in trenuria si trenurib
		trenuria = 0;
		trenurib = 0;
		int cateamina = 0;
		int cateaminb = 0;
		
		for( int i=0; i<nv; i++)
		{
			if(ab[i][0] == 1)//e tren care a ajuns
			{
				cateamina++;
			}else//e tren care pleaca
			{
				if(cateamina > 0)
				{
					cateamina--;
				}else//trebuie s aplece unu si nu am trenuri disponibile in A
				{
					trenuria++;
				}
			}
		}
		
		for( int i=0; i<nv; i++)
		{
			if(ba[i][0] == 1)//e tren care a ajuns
			{
				cateaminb++;
			}else//e tren care pleaca
			{
				if(cateaminb > 0)
				{
					cateaminb--;
				}else//trebuie s aplece unu si nu am trenuri disponibile in A
				{
					trenurib++;
				}
			}
		}
		//daca totul e corect am solutia in maze
		//trebuie doar sa gasesc inceputul si sfarsitul labirintului
		//stiu ca liniile merg de la 0 la maxl, si coloanele de la minc la maxc
		print_solutie(i);
	}
	
	fclose(f_in);
	fclose(f_out);
	return 0;
}
int main()
{
	rezolva();
	printf("aaaa");
}
