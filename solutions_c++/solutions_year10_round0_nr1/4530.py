# include <iostream.h>
# include <conio.h>
# include <stdio.h>
# include <math.h>


class snapper
{
	private :
		int K,N,ch[5],i,cas;
	public :
		int numero(void);
		void reader(void);
		int snap(void);
};

int snapper :: numero()
{
	int y,o;
	y=ch[0];
	o=1;

	while(o<=i)
	{
		y=(y*10)+ch[o];
		o++;
	}
	return(y);
}

void snapper :: reader()
{
	int u,flag=0;
	char c;
	FILE *f,*op;

	cas=1;
	i=-1;

	f=fopen("A-small.in","r");
	op=fopen("Snapper.txt","w");

	while (c!=EOF)
	{
		c=fgetc(f);

		if (c>='0' && c<='9')
		{
			i++;
			ch[i]=c-48;
		}
		else if (i>=0)
		{
			u=numero();

			if (flag==0)
			{
				flag=1;
			}
			else
			{
				switch(flag)
				{
					case 1:N=u;flag++;break;
					case 2:K=u;
					if(snap()==0)
					fprintf(op,"Case #%d: OFF\n",cas);
					else
					fprintf(op,"Case #%d: ON\n",cas);
					cas++;
					flag=1;
				};
			}
			i=-1;
		}
	}

	fclose(f);
	fclose(op);
}

int snapper :: snap()
{
	int p;

	p=pow(2,N);
	K++;

	if (K%p==0)
	return(1);
	else
	return(0);
}

void main()
{
	snapper obj;
	clrscr();

	obj.reader();
	getch();
}