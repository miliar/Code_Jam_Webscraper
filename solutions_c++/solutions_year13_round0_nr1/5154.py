#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int rslt=-1;
struct wrd
{
	char c[10];
	int nc;
	wrd()
	{
		nc=1;
	}
};
struct line
{
	wrd w[5];
	int nw;
	line()
	{
		nw=1;
	}
};

struct page
{
	line l[6000];

	int nl;
	page()
	{
		nl=1;
	}
};

/**/
int main()
{
	page pg;
	int x,n=0,i=0,j=0,k=0;
	printf("hello world!!\n------------\n\n");
FILE* f=fopen("A-large.in","r");
FILE* fw=fopen("A-large.out","w");
			if(fw==NULL) printf("could not open");
if(f==NULL)
{
	printf("unable to open file");
}



	 while  ( ( x = fgetc( f ) ) != EOF )
            {
				n++;
				if(x==13 || x==10)
				{
					pg.l[i].w[j].c[k]=NULL;
					i++;
					pg.nl++;
					j=0;k=0;
				}
				else if(x==32)
				{
					pg.l[i].w[j].c[k]=NULL;
					j++;k=0;
					pg.l[i].nw++;

				}
				else
				{
					pg.l[i].w[j].c[k]=x;
					pg.l[i].w[j].nc++;
					k++;
				}
            }

			
            fclose( f);/**/
			char *c="6";
			//printf("%s",c);
			printf("%d\n\n-----\n",atoi(pg.l[0].w[0].c));

			int t=atoi(pg.l[0].w[0].c);

			for (i=0;i<t;i++)
			{
				int ln=5*i+1;

				rslt=-1;

				
				
				char l1[5],l2[5],l3[5],l4[5];
				l1[4]=NULL;
				l2[4]=NULL;
				l3[4]=NULL;
				l4[4]=NULL;
				for (j=0;j<4;j++)
				{
					l1[j]=pg.l[ln].w[0].c[j];
					l2[j]=pg.l[ln+1].w[0].c[j];
					l3[j]=pg.l[ln+2].w[0].c[j];
					l4[j]=pg.l[ln+3].w[0].c[j];
				}
				

				

				if(strcmp(l1,"XXXX")==0||strcmp(l1,"XXXT")==0||strcmp(l1,"XXTX")==0||strcmp(l1,"XTXX")==0||strcmp(l1,"TXXX")==0) rslt=1;
				if(strcmp(l2,"XXXX")==0||strcmp(l2,"XXXT")==0||strcmp(l2,"XXTX")==0||strcmp(l2,"XTXX")==0||strcmp(l2,"TXXX")==0) rslt=1;
				if(strcmp(l3,"XXXX")==0||strcmp(l3,"XXXT")==0||strcmp(l3,"XXTX")==0||strcmp(l3,"XTXX")==0||strcmp(l3,"TXXX")==0) rslt=1;
				if(strcmp(l4,"XXXX")==0||strcmp(l4,"XXXT")==0||strcmp(l4,"XXTX")==0||strcmp(l4,"XTXX")==0||strcmp(l4,"TXXX")==0) rslt=1;
				
				if(strcmp(l1,"OOOO")==0||strcmp(l1,"OOOT")==0||strcmp(l1,"OOTO")==0||strcmp(l1,"OTOO")==0||strcmp(l1,"TOOO")==0) rslt=0;
				
				if(strcmp(l2,"OOOO")==0||strcmp(l2,"OOOT")==0||strcmp(l2,"OOTO")==0||strcmp(l2,"OTOO")==0||strcmp(l2,"TOOO")==0) rslt=0;
				if(strcmp(l3,"OOOO")==0||strcmp(l3,"OOOT")==0||strcmp(l3,"OOTO")==0||strcmp(l3,"OTOO")==0||strcmp(l3,"TOOO")==0) rslt=0;
				if(strcmp(l4,"OOOO")==0||strcmp(l4,"OOOT")==0||strcmp(l4,"OOTO")==0||strcmp(l4,"OTOO")==0||strcmp(l4,"TOOO")==0) rslt=0;

				//printf("\nresult=%d\n",rslt);

				//char l1[4],l2[4],l3[4],l4[4];
				
				for (j=0;j<4;j++)
				{
					l1[j]=pg.l[ln+j].w[0].c[0];
					l2[j]=pg.l[ln+j].w[0].c[1];
					l3[j]=pg.l[ln+j].w[0].c[2];
					l4[j]=pg.l[ln+j].w[0].c[3];
				}
				
				if(strcmp(l1,"XXXX")==0||strcmp(l1,"XXXT")==0||strcmp(l1,"XXTX")==0||strcmp(l1,"XTXX")==0||strcmp(l1,"TXXX")==0) rslt=1;
				if(strcmp(l2,"XXXX")==0||strcmp(l2,"XXXT")==0||strcmp(l2,"XXTX")==0||strcmp(l2,"XTXX")==0||strcmp(l2,"TXXX")==0) rslt=1;
				if(strcmp(l3,"XXXX")==0||strcmp(l3,"XXXT")==0||strcmp(l3,"XXTX")==0||strcmp(l3,"XTXX")==0||strcmp(l3,"TXXX")==0) rslt=1;
				if(strcmp(l4,"XXXX")==0||strcmp(l4,"XXXT")==0||strcmp(l4,"XXTX")==0||strcmp(l4,"XTXX")==0||strcmp(l4,"TXXX")==0) rslt=1;
				
				if(strcmp(l1,"OOOO")==0||strcmp(l1,"OOOT")==0||strcmp(l1,"OOTO")==0||strcmp(l1,"OTOO")==0||strcmp(l1,"TOOO")==0) rslt=0;
				
				if(strcmp(l2,"OOOO")==0||strcmp(l2,"OOOT")==0||strcmp(l2,"OOTO")==0||strcmp(l2,"OTOO")==0||strcmp(l2,"TOOO")==0) rslt=0;
				if(strcmp(l3,"OOOO")==0||strcmp(l3,"OOOT")==0||strcmp(l3,"OOTO")==0||strcmp(l3,"OTOO")==0||strcmp(l3,"TOOO")==0) rslt=0;
				if(strcmp(l4,"OOOO")==0||strcmp(l4,"OOOT")==0||strcmp(l4,"OOTO")==0||strcmp(l4,"OTOO")==0||strcmp(l4,"TOOO")==0) rslt=0;

				
				for (j=0;j<4;j++)
				{
					l1[j]=pg.l[ln+j].w[0].c[j];
					l2[j]=pg.l[ln+j].w[0].c[3-j];
					
				}
				
				//printf("\n%s\n",l1);

if(strcmp(l1,"XXXX")==0||strcmp(l1,"XXXT")==0||strcmp(l1,"XXTX")==0||strcmp(l1,"XTXX")==0||strcmp(l1,"TXXX")==0) rslt=1;
				if(strcmp(l2,"XXXX")==0||strcmp(l2,"XXXT")==0||strcmp(l2,"XXTX")==0||strcmp(l2,"XTXX")==0||strcmp(l2,"TXXX")==0) rslt=1;
				if(strcmp(l3,"XXXX")==0||strcmp(l3,"XXXT")==0||strcmp(l3,"XXTX")==0||strcmp(l3,"XTXX")==0||strcmp(l3,"TXXX")==0) rslt=1;
				if(strcmp(l4,"XXXX")==0||strcmp(l4,"XXXT")==0||strcmp(l4,"XXTX")==0||strcmp(l4,"XTXX")==0||strcmp(l4,"TXXX")==0) rslt=1;
				
				if(strcmp(l1,"OOOO")==0||strcmp(l1,"OOOT")==0||strcmp(l1,"OOTO")==0||strcmp(l1,"OTOO")==0||strcmp(l1,"TOOO")==0) rslt=0;
				
				if(strcmp(l2,"OOOO")==0||strcmp(l2,"OOOT")==0||strcmp(l2,"OOTO")==0||strcmp(l2,"OTOO")==0||strcmp(l2,"TOOO")==0) rslt=0;
				if(strcmp(l3,"OOOO")==0||strcmp(l3,"OOOT")==0||strcmp(l3,"OOTO")==0||strcmp(l3,"OTOO")==0||strcmp(l3,"TOOO")==0) rslt=0;
				if(strcmp(l4,"OOOO")==0||strcmp(l4,"OOOT")==0||strcmp(l4,"OOTO")==0||strcmp(l4,"OTOO")==0||strcmp(l4,"TOOO")==0) rslt=0;
				
				if(rslt==-1)
				for (j=0;j<4;j++)
				{
					for(k=0;k<4;k++)
					if(pg.l[ln+j].w[0].c[k]=='.') rslt=2;
					
				}/**/

			
				char* r;
				//printf("\n-----\n");
				
				if(rslt==0)r="O won";
				if(rslt==1)r="X won";
				if(rslt==2)r="Game has not completed";
				if(rslt==-1)r="Draw";
				printf("Case #%d: %s\n",i+1,r);
				fprintf(fw,"Case #%d: %s\n",i+1,r);

			}

			fclose(fw);

			scanf("%d",&x);
}