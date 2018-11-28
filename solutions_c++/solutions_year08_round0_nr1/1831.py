
#include <stdio.h>
#include <fstream.h>
#include <string.h>

char search[10000][1000];
char query[10000][1000];
int d[10000][1000];
void main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t;
	in>>t;
	int i;
	for(i=0;i<t;i++)
	{
		int j;
		int s,q;
		//input search engines
		in>>s;in.ignore();
		for(j=0;j<s;j++)
		{
			in.getline(search[j],200);
		}
		//input queries
		in>>q;in.ignore();
		for(j=0;j<q;j++)
		{
			in.getline(query[j],200);
		}
		//initialize d[0][s]
		for(j=0;j<s;j++)
		{
			if( !strcmp(search[j],query[0]))
				d[0][j]=-1;
			else
				d[0][j]=0;
		}
		//process queries
		for(j=1;j<q;j++)
		{
			int k;
			for(k=0;k<s;k++)
			{
				if( !strcmp(search[k],query[j]) ) //������ k�δ� ���� �� ����.
				{
					d[j][k]=-1;
				}
				else if( d[j-1][k]==-1) //���� �̰� �ƴϿ����� switch�� �ؾ� �Ѵ�.
				{
					int l;
					int min=-1;//�ּҰ��� ã�Ƽ�
					for(l=0;l<s;l++)
					{
						if( d[j-1][l]!=-1 && (min==-1 || min > d[j-1][l]))
							min=d[j-1][l];
					}
					d[j][k]=min+1;//����ġ�� �ϹǷ� +1 �� ���ش�.
				}
				else
					d[j][k]=d[j-1][k];
			}
		}
		int min=-1;//�� ������ �ּҰ��� ã�´�.
	/*	if( q==0 ) 
			min=0;
		else*/
		{
			for(j=0;j<s;j++)
			{
				if( d[q-1][j] != -1 && (min==-1 || min > d[q-1][j]))
					min=d[q-1][j];
			}
		}
		out<<"Case #"<<i+1<<": "<<min<<endl;
	}
}
