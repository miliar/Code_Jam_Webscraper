#include<fstream>
using namespace std;
void ExpandNode(int**,char**,int,int,int,int,char&);
int main()
{
	fstream fin,fout;
	fin.open("B-large.in",ios::in);
	fout.open("B-large.out",ios::out);
	int N,H,W;
	fin>>N;
	int i,j,k;
	int **In=NULL;
	char **Out=NULL;
	char flag;
	for(i=0;i<N;i++)
	{
		if(In)
		{
			for(j=0;j<H;j++)
				if(In[j])
					delete[] In[j];
			delete[] In;
		}
		if(Out)
		{
			for(j=0;j<H;j++)
				if(Out[j])
					delete[] Out[j];
			delete[] Out;
		}
		fin>>H>>W;
		In=new int*[H];
		Out=new char*[H];
		for(j=0;j<H;j++)
		{
			In[j]=new int[W];
			Out[j]=new char[W];
		}
		for(j=0;j<H;j++)
		{
			for(k=0;k<W;k++)
			{
				fin>>In[j][k];
				Out[j][k]='\0';
			}
		}
		flag='a'-1;
		for(j=0;j<H;j++)
		{
			for(k=0;k<W;k++)
			{
				ExpandNode(In,Out,H,W,j,k,flag);
			}
		}
		fout<<"Case #"<<i+1<<":"<<endl;
		for(j=0;j<H;j++)
		{
			for(k=0;k<W;k++)
			{
				fout<<Out[j][k];
				if(k!=(W-1))
					fout<<' ';
			}
			fout<<endl;
		}
	}
	return 0;
}
void ExpandNode(int **In,char **Out,int H,int W,int x,int y,char &flag)
{
	if(Out[x][y]=='\0')
	{
		int in0=In[x][y],in1=10000,in2=10000,in3=10000,in4=10000;
		if(x!=0)
		{
			in1=In[x-1][y]; //North
		}
		if(y!=0)
		{
			in2=In[x][y-1]; //West
		}
		if(y!=(W-1))
		{
			in3=In[x][y+1]; //East
		}
		if(x!=(H-1))
		{
			in4=In[x+1][y]; //North
		}
		if(in0<=in1&&in0<=in2&&in0<=in3&&in0<=in4)
		{
			Out[x][y]=++flag;
		}
		else
		{
			int in=in1<=in2?in1:in2;
			in=in<=in3?in:in3;
			in=in<=in4?in:in4;
			if(in==in1)
			{
				ExpandNode(In,Out,H,W,x-1,y,flag);
				Out[x][y]=Out[x-1][y];
			}
			else if(in==in2)
			{
				ExpandNode(In,Out,H,W,x,y-1,flag);
				Out[x][y]=Out[x][y-1];
			}
			else if(in==in3)
			{
				ExpandNode(In,Out,H,W,x,y+1,flag);
				Out[x][y]=Out[x][y+1];
			}
			else if(in==in4)
			{
				ExpandNode(In,Out,H,W,x+1,y,flag);
				Out[x][y]=Out[x+1][y];
			}
		}
	}
	return;
}
