#include<stdio.h>
#include<iostream.h>
int h,w,alt[102][102],sink[26][2],scount;

int func(int i,int j)
{
	int x;
	for(x=0;x<scount;x++)
		if((sink[x][0]==i)&&(sink[x][1]==j))
				return x;
		if((alt[i][j]<=alt[i+1][j])&&(alt[i][j]<=alt[i][j+1])&&(alt[i][j-1]>=alt[i][j])&&(alt[i][j]<=alt[i-1][j]))
			{
				sink[scount][0]=i;
				sink[scount++][1]=j;
				return func(i,j);	 
			}



		
	if((alt[i-1][j]<=alt[i][j-1])&&(alt[i-1][j]<=alt[i+1][j])&&(alt[i-1][j]<=alt[i][j+1]))
				return func(i-1,j);
	if((alt[i][j-1]<=alt[i+1][j])&&(alt[i][j-1]<=alt[i][j+1]))
				return func(i,j-1);
	if(alt[i][j+1]<=alt[i+1][j])
				return func(i,j+1);
			return func(i+1,j);

}
int main()
{
	FILE *in,*out;
	int i,j,t,num,n;


	in=fopen("in2.txt","r");
	out=fopen("out.txt","w");
	fscanf(in,"%d",&num);
	for(n=1;n<=num;n++)
	{
	scount=0;
	fscanf(in,"%d%d",&h,&w);
	printf("%d\t%d",h,w);
		for(i=0;i<h+2;i++)
		for(j=0;j<w+2;j++)
			alt[i][j]=10000;
	for(i=1;i<h+1;i++)
		for(j=1;j<w+1;j++)
			fscanf(in,"%d",&alt[i][j]);
	printf("\n");

	for(i=0;i<h+2;i++)
	{
		for(j=0;j<w+2;j++)
				printf("%d\t",alt[i][j]);
		
	printf("\n");	 }
	
	
		printf("%d\n",scount);
		for(i=0;i<scount;i++)
			printf("%d\t%d\t",sink[i][0],sink[i][1]);
		printf("\n");
		fprintf(out,"Case #%d:\n",n);	 
		for(i=1;i<h+1;i++)
		{
			for(j=1;j<w+1;j++)
					fprintf(out,"%c\t",func(i,j)+97);
		
		
			fprintf(out,"\n");
		}


}
fclose(in);
fclose(out);
}

