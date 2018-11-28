#include <stdio.h>
#include <string.h>

#define MAX 30

char engines[100][105], queries[105];//caile initiala si reverse
char engine[105];
bool curat[105];

int n, s, q, y, nengines, pos;

int posl, posc;//pozitiile omului pe linie si coloana

FILE *f_in, *f_out;

int print_solutie(int id)
{
	fprintf(f_out,"Case #%d: %d\n",id+1,y);
	return 0;
}

int rezolva()
{
	f_in = fopen("A-large.in","r");
	f_out = fopen("output.txt","w");
	fscanf(f_in,"%d",&n);
	char temp;
	fscanf(f_in,"%c",&temp);//pentru '\n'
	for(int i=0; i < n; i++)
	{

		memset(engines, 0, sizeof(engines));
		memset(engine, 0, sizeof(engine));
		memset(queries, 0, sizeof(queries));
		memset(curat, 1, sizeof(curat));
		
		y = 0;
		nengines = 0;
		
		fscanf(f_in,"%d",&s);//nr de search engines
		fscanf(f_in,"%c",&temp);//pentru '\n'
		
		for(int i=0;i<s;i++)
		{
			memset(engine, 0, sizeof(engine));
			fgets(engine,105,f_in);
			strcpy(engines[i],engine);
			
			//fscanf(f_in,"%c",&temp);//pentru '\n'
		}	

		fscanf(f_in,"%d",&q);//nr de search engines
		fscanf(f_in,"%c",&temp);//pentru '\n'
		
		for(int i=0;i<q;i++)
		{
			memset(queries, 0, sizeof(queries));
			fgets(queries,105,f_in);
			pos = 0;
			while(strcmp (queries,engines[pos]) != 0)
				pos++;
			if(curat[pos] == 1)
			{//nu l-am mai gasit
				curat[pos] = 0;
				nengines++;
				if(nengines == s)
				{//am folosit toate enginurile fac switch
					y++;
					
					memset(curat, 1, sizeof(curat));
					curat[pos] = 0;
					nengines = 1;
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
