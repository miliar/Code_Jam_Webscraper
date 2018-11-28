#include<cstdio>
#include<cstring>

struct node
{
	double p;
	char name[15];
	bool child;
};

node Tree[8000];
int count;

void parse(int P)
{
	count++;
	int c;
	while(1)
	{
		c = fgetc(stdin);
		if(c == '(') break;
	}
	//fprintf(stderr,"(");

	while(1)
	{
		c = fgetc(stdin);
		if(c <= '1' && c >= '0') break;
	}

	double p;
	double index = 1;
	if(c == '1') p = 1.00;
	else p = 0;

	while(1)
	{
		c = fgetc(stdin);
		if(c == ' ' || c == '\n') break;
		else if(c == '.') continue;
		else if(c == ')')
		{
			Tree[P].child = false;
			Tree[P].p = p;
			//fprintf(stderr,"%lf",p);
			//fprintf(stderr,")");
			return;
		}
		else
		{
			index*= 0.1;
			p += (((double)(c-48)) * index);
		}
	}
	//fprintf(stderr,"%lf",p);

	Tree[P].p = p;

	char ff[15];
	while(1)
	{
		c = fgetc(stdin);
		if(c == ')')
		{
			Tree[P].child = false;
			//fprintf(stderr,")");
			return;
		}
		else if(c == ' ' || c == '\n') continue;
		else
		{
			Tree[P].child = true;
			Tree[P].name[0] = c;
			break;
		}
	}

	int ll = 1;

	while(1)
	{
		c = fgetc(stdin);
		if(c == ' ' || c == '\n')
		{
			//fprintf(stderr," %s ",Tree[P].name);
			parse(2*P+1);
			parse(2*P+2);
			break;
		}
		else
		{
			Tree[P].name[ll] = c;
			ll++;
		}
	}

	while(1)
	{
		c = fgetc(stdin);
		if(c == ' ' || c == '\n') continue;
		if(c == ')')
		{
			//fprintf(stderr,")");
			return;
		}
	}
}

int main()
{
	int N,L,A;
	double res;
	char animal_name[15];
	char ff[102][15];
	scanf("%d\n",&N);
	for(int ii = 1;ii <= N;++ii)
	{
		memset(Tree,0,sizeof(Tree));
		count = 0;
		scanf("%d\n",&L);
		parse(0);
		//for(int i = 0;i < count;++i)
		//{
		//	printf("%d %lf %s %d\n",i,Tree[i].p,Tree[i].name,Tree[i].child);
		//}
		//fprintf(stderr,"%d\n",count);
		scanf("%d\n",&A);
		printf("Case #%d:\n",ii);
		for(int i = 0;i < A;++i)
		{
			int cc,pn;
			scanf("%s %d",animal_name,&cc);
			//fprintf(stderr,"%s %d",animal_name,cc);
			for(int j = 0;j < cc;++j) scanf("%s",ff[j]);
			res = 1;
			pn = 0;
			while(1)
			{
				//printf("%d %lf\n",pn,res);
				res *= Tree[pn].p;
				//printf("%d %lf\n",pn,res);
				if(Tree[pn].child)
				{
					//printf("I am here %d\n",pn);
					int ind = -1;
					for(int j = 0;j < cc;++j) if(strcmp(Tree[pn].name,ff[j]) == 0) {ind = j;break;}
					if(ind != -1) pn = pn*2 + 1;
					else pn = pn*2 + 2;
				}
				else break;
			}
			printf("%lf\n",res);
		}
	}
	return 0;
}
