#include <iostream.h>
#include <fstream>
#include <string>
using namespace std;

void main()
{
	ifstream ins;
	ofstream ous;
	string line;
	int L,D,N,number,col;
	
	char p[1024]={0};
	ins.open("d:\\A-small-attempt1.in");
    ous.open("d:\\b.txt");
	ins>>L>>D>>N;//����ռ�
	char **data=new char*[D];//��һά
	char **flag= new char*[D];
	for( int i=0; i<D; i++)
	{
		data[i] = new char[L+1];  //����ڶ�ά��ÿһ�еĿռ䡣
		flag[i] = new char[L];
	}
	for(i=0;i<D;i++)
	{
       ins>>data[i];
	}
	for(i=1;i<=N;i++)
	{
		ins>>p;
		//�㷨����
		//col ��������
		col=-1;
		int in=0;
		//memset(flag,0,L*D*sizeof(char));
		for(int j=0;j<D;j++)
		{
		    memset(flag[j],0,L*sizeof(char));
		}
		for(j=0;j<strlen(p);j++)
		{
		   if(p[j]=='(')
		   {
		      col++;
			  in=1;
		   }
		   else if(p[j]==')')
		   {			  
		      in=0;		   
		   }
		   else
		   {
			   if(in==0)
			   {
				   col++;
			   }
				   for(int k=0;k<D;k++)
				   {
					   if(data[k][col]==p[j])
					   {
						   flag[k][col]=1;
					   }
				   }	  
		   }
		}
        number=0;
		for(int ii=0;ii<D;ii++)
		{
			int sum=0;
			for (int jj=0;jj<L;jj++)
			{   
				
				if (flag[ii][jj]==1)
				{
					sum++;
				}
				
			}
			if (sum==L)
			{
				number++;
			}
		}
	    ous<<"Case # "<<i<<" :"<<number<<endl;
	}
	
  ins.close();
  ous.close();
}