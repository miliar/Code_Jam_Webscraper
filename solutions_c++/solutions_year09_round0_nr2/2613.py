


#include<stdio.h>
int i2,j2,temp,w,l,visited[200][200],x[200][200],visited2[200][200];
char graph[200][200],c='a';
int check(int i,int j)
{
	int order,order2,k,min=100000,a[200],i1[200],j1[200];
	i2=-1;
	j2=-1;
	order=0;
	if(graph[i][j]!=' ')
	visited2[i][j]=1;
	if((x[i-1][j]<x[i][j])&&((i-1)>=0))
	{
		a[order]=x[i-1][j];
		i1[order]=i-1;
		j1[order]=j;
		order++;
	}
	
	if((x[i][j-1]<x[i][j])&&((j-1)>=0))
	{
		a[order]=x[i][j-1];
		i1[order]=i;
		j1[order]=j-1;
		order++;
	}	
	if((x[i][j+1]<x[i][j])&&((j+1)<w))
	{
		a[order]=x[i][j+1];
		i1[order]=i;
		j1[order]=j+1;
		order++;
	}
		if((x[i+1][j]<x[i][j])&&((i+1)<l))
	{
		a[order]=x[i+1][j];
		i1[order]=i+1;
		j1[order]=j;
		order++;
	}	
	
	for(k=0;k<order;k++)
	{
		if(a[k]<min)
		{
			temp=k;
			min=a[k];	
		}
	}

	if(order>0)
	{
	i2=i1[temp];
	j2=j1[temp];
	}
	return(temp);
}
void calc(int i,int j)
{
	graph[i][j]=c;
	visited[i][j]=1;
	
	if((x[i+1][j]>x[i][j])&&((i+1)<l)&&(visited[i+1][j]==0))
	{
		temp=check(i+1,j);
		if((i2==i)&&(j2==j))
			calc(i2+1,j2);
	}
	if((x[i-1][j]>x[i][j])&&((i-1)>=0)&&(visited[i-1][j]==0))
	{
		temp=check(i-1,j);
		if((i2==i)&&(j2==j))
			calc(i2-1,j2);
	}
	if((x[i][j+1]>x[i][j])&&((j+1)<w)&&(visited[i][j+1]==0))
	{
		temp=check(i,j+1);
		if((i2==i)&&(j2==j))
			calc(i2,j2+1);
	}
	if((x[i][j-1]>x[i][j])&&((j-1)>=0)&&(visited[i][j-1]==0))
	{
		temp=check(i,j-1);
		if((i2==i)&&(j2==j))
			calc(i2,j2-1);
	}
	if(visited2[i][j]==0)
	{temp=check(i,j);
	if((temp!=-1)&&(visited[i2][j2]==0)&&(j2!=-1))
	calc(i2,j2);
	}
	return;
}
	
int main()
{
	int i,j,k,n;

	FILE *in=fopen("B-large.in","r");
	FILE *out=fopen("B-large.out","w");
	fscanf(in,"%d",&n);
	for(k=0;k<n;k++)
	{	fscanf(in,"%d %d",&l,&w);
		c='a';
	for(i=0;i<l;i++)
	{
		for(j=0;j<w;j++)
		{
			graph[i][j]=' ';
			visited[i][j]=0;
			visited2[i][j]=0;
			fscanf(in,"%d",&x[i][j]);
		}
	}
	for(i=0;i<l;i++)
	{
		for(j=0;j<w;j++)
		{
			if(visited[i][j]==0)
			{
				calc(i,j);
				c++;
			}
			
		}
	}
	fprintf(out,"Case #%d:\n",k+1);
	for(i=0;i<l;i++)
	{
		for(j=0;j<w;j++)
		{
			if(j!=0)
			fprintf(out," %c",graph[i][j]);
			else
				fprintf(out,"%c",graph[i][j]);
		}
		fprintf(out,"\n");
	}

	}
}
			

					


