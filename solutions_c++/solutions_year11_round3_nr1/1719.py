
#include<stdio.h>
#include<conio.h>
#include<malloc.h>

int R, C;
char v[50][50];
bool fi(int x, int y);
void main()
{
	FILE *f,*g;
	f=fopen("input","r");
	g=fopen("output","w");
	int tc;
	bool aux;
	
	 fscanf(f,"%d",&tc);

	 for(int k=0;k<tc;k++)
	 {
		 aux=true;
		 fscanf(f,"%d %d\n",&C,&R);
		
		 for(int i=0;i<50;i++)
			for(int j=0;j<50;j++)
				 v[i][j]='!';
		 
		 for(int i=0;i<C;i++)
		 {
			 for (int j=0;j<R;j++)
			 {
				 char c;
				 fscanf(f,"%c",&c);
				 v[i][j]=c;
			 }
			 fscanf(f,"\n");
		 }
		 for(int i=0;i<C;i++)
		 {
			 for (int j=0;j<R;j++)
			 {
				 if(v[i][j]=='#')
					 if(!fi(i,j))
					 {
						 aux=false;
						 break;
					 }
			 }
			 if(!aux)
				 break;
		 }
		

		 fprintf(g,"Case #%d:\n",(k+1));
		 if(!aux)
			{
				fprintf(g,"Impossible\n");
		 }
		 else
		 
		for(int i=0;i<C;i++)
		 {
			 for (int j=0;j<R;j++)
			 {
				 fprintf(g,"%c",v[i][j]);
			 }
			fprintf(g,"\n");
		}
		 

	 }
 
 fcloseall();
}

bool fi(int x, int y)
{
	int s=0;
	for(int i=y;i<R;i++)
		if(v[x][i]=='#'&& x<C)
			{
				s++;
				if(v[x+1][i]!='#')
					return false;
				else
				{
					if(v[x][i-1]=='/'&&i>y)
						{
							v[x][i]='\\';
							v[x+1][i]='/';
						}
					else
						{
							v[x][i]='/';
							v[x+1][i]='\\';
						}
				}
		}
		else
			break;
	if(s%2!=0)
		return false;
	return true;
}