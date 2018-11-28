#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int noc;int m;
char buff[9999];
char moves[999];
char val[999];
FILE *fg;

void open(char * fileName);
void calc(char * s,int cno);

struct robot
{
	char type;
	int pos;
	int buff;
	int bflag;
};
int total=0;
void open(char * fileName)
{
	FILE *fp=fopen(fileName,"r");
	strcpy(buff,"");
	int k=1;int y;
	while(fgets(buff,9999,fp)!=NULL)
	{
		
		if(k==1)
		{
			noc=atoi(buff);
			y=noc-1;
			k++;
			continue;
		}		
		printf("\n**********************case %d**************************\n",noc-y);
		calc(buff,noc-y);
		y--;
		total=0;
		//break;
	}
	//printf("\nNumber of cases:%d",noc);
}
void calc(char * s,int cno)
{
	int cnt=0;
	int p=0;
	//printf("\n got %s with noc:%d",s,noc);
	printf("\n moves %d",atoi(&s[p]));
	struct robot orange,blue;
	orange.pos=1;
	blue.pos=1;
	orange.buff=0;
	blue.buff=0;
	orange.bflag=0;
	blue.bflag=0;
	
	p++;
	while(s[p]!='\0')
	{
		while(s[p]!=' ')
		p++;
		while(s[p]==' ')
		p++;
		
		cnt++;
			
		//If orange robot move found
		if(s[p]=='O')
		{
			orange.bflag=1;
			p++;
			printf("\nfound orange; go for button number");
			while(s[p]==' ')
			p++;
			
			
			strcpy(val,"");
			
			//while complete value is read		
			while(s[p]!=' ')
			{
				strcat(val,&s[p]);
				p++;
				if(s[p]=='\0')
				break;
			}
			
			int value=atoi(val);
			
			
				printf("\nfound val:%d",atoi(val));
				///////////////////////////////////
				
				if(value>orange.pos)
				 m=(value-orange.pos);
				else
				 m=(orange.pos-value);
				
				m++;
				
				if(m<=orange.buff)
				{
					total=total+1;
					blue.buff=blue.buff+1;
				}
				else
				{
					total=total+m-orange.buff;
					blue.buff=blue.buff+m-orange.buff;
				}
					
			
			orange.buff=0;			
			orange.pos=value;
			
		    printf("\nTotal:%d",total);
			///////////////////////////////////
		}
		else	//If blue robot move found
		{
			blue.bflag=1;
			p++;
			printf("\nfound blue; go for button number");
			while(s[p]==' ')
			p++;
						
			strcpy(val,"");
			
			//while complete value is read		
			while(s[p]!=' ')
			{
				strcat(val,&s[p]);
				p++;
				if(s[p]=='\0')
				break;
			}
				
			
			int value=atoi(val);
			printf("\nfound val:%d",atoi(val));
							
				if(value>blue.pos)
				 m=(value-blue.pos);
				else
				 m=(blue.pos-value);
				m++;

				if(m<=blue.buff)
				{
					total=total+1;
					orange.buff=orange.buff+1;
				}
				else
				{
					total=total+m-blue.buff;
					orange.buff=orange.buff+m-blue.buff;
				}		
			
			blue.buff=0;
			
			blue.pos=value;
		    printf("\nTotal:%d",total);
			
			//////////////////////////////////
		}
		
		
	}
	fprintf(fg,"Case #%d: %d\n",cno,total);
	total=0;
	
}
int main(int argc,char*argv[])
{

	fg=fopen("A-small-0.out","w");
	total=0;
	open(argv[1]);
	
	return 0;
}