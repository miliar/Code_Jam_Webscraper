#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream.h>
struct Array{
	int id;
	int data;
	char root;
	bool foot_print;
}**array;

struct Array2{
	int x;
	int y;
}*b;

char Root='a';

char findroot (int,int,int ,int);

void main()
{
	ofstream fout("out.txt");
	int num;    
	int *p;    
	int array_x,array_y;

	cin >> num;

	char ***a;
	a=new char **[num];

	b=new Array2[num];

	for(int i=0;i<num;i++)
	{
		
		cin >> array_x>>array_y;
		a[i]=new char *[array_x];

		b[i].x=array_x;
		b[i].y=array_y;
		for(int k=0;k<array_x;k++)
		{
			a[i][k]=new char[array_y];
		}


		int num=array_x*array_y;

		p=(int *)malloc(sizeof(int)*(num));
		for(int j=0;j<num;j++)
		{
			cin>>p[j];
		}
		array=(Array **)malloc(sizeof(Array *)*(array_x));

		for(int m=0;m<array_x;m++)
		{
			array[m]=(Array *)malloc(sizeof(Array)*(array_y));
		}	
		for(m=0;m<array_x;m++)
		{
			for(int n=0;n<array_y;n++)
			{
				array[m][n].id=m*array_y+n;
				array[m][n].data=p[m*array_y+n];
				array[m][n].foot_print=false;
			}
		}

		for(m=0;m<array_x;m++)
		{
			for(int n=0;n<array_y;n++)
			{
				if(array[m][n].foot_print==false)
				{
					array[m][n].root=findroot(m,n,array_x,array_y);
				}
				a[i][m][n]=array[m][n].root;
			}
			
		}

		Root='a';
		
	}
	cout <<endl;

	for(i=0;i<num;i++)
	{
		fout<<"Case #"<<i+1<<": "<<endl;
		for(int j=0;j<b[i].x;j++)
		{
			for(int k=0;k<b[i].y;k++)
			{
				fout<<a[i][j][k]<<" ";
			}
			fout<<endl;
		}
	}

}


char findroot(int x,int y,int a,int b)
{
	if(array[x][y].foot_print==true)
		return array[x][y].root;
	else
	{
		array[x][y].foot_print=true;

		int x1=x;
		int y1=y;
		if((x1-1>=0)&&(array[x1-1][y1].data<array[x][y].data))
		{
			x=x1-1;
			y=y1;
		}
		if((y1-1>=0)&&(array[x1][y1-1].data<array[x][y].data))
		{
			x=x1;
			y=y1-1;
		}
		if((y1+1<=b-1)&&(array[x1][y1+1].data<array[x][y].data))
		{
			x=x1;
			y=y1+1;
		}
		if((x1+1<=a-1)&&(array[x1+1][y1].data<array[x][y].data))
		{
			x=x1+1;
			y=y1;
		}
		if(x==x1&&y==y1)
		{
			return Root++;
		}
		else 
		{
			char mark=findroot(x,y,a,b);
			array[x][y].root=mark;
			return mark;
		}
	}
}




