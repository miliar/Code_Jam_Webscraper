#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>
using namespace std;
struct Indexer
{
	int count;
	struct Indexer *indexer;

};
struct Indexer* InitIndexer()
{
	struct Indexer* indexer=new Indexer[10];
	for(int i=0;i<10;i++)
	{
		indexer[i].count=0;
		indexer[i].indexer=0;
	}
	return indexer;
}
void Insert(struct Indexer* indexer, unsigned int num)
{
	if(indexer)
	{
		while(num/10>=1)
		{
			unsigned int numMod=num%10;
			indexer[numMod].count=indexer[numMod].count+1;
			if(!indexer[numMod].indexer)
			{
				struct Indexer *newIndexer=InitIndexer();
				indexer[numMod].indexer=newIndexer;
			}
			indexer=indexer[numMod].indexer;
			num=num/10;
		}
		indexer[num].count=indexer[num].count+1;
	}

}
bool search(struct Indexer* indexer, unsigned int num)
{
	if(indexer)
	{
		while(num/10>=1)
		{
			unsigned int numMod=num%10;
			if(indexer[numMod].count>0)
			{
				indexer=indexer[numMod].indexer;
			}
			else return false;
			num=num/10;
		}
		if(indexer&&indexer[num].count>0)
		{
			int lastCount=0;
			struct Indexer *lastIndexer=indexer[num].indexer;
			if(lastIndexer)
			{
				for(int i=0;i<10;i++)
				{
					lastCount=lastCount+lastIndexer[i].count;
				}
				if(indexer[num].count>lastCount) return true;
				else return false;
			}
			else return true;

		}
		else return false;
	}
	return false;
}

int main()
{
	const int digits=6;
	char num[digits];
	int A=1111;
	int B=2222;
	int count=0;
	char m[digits];;
	ifstream obj("input.txt");
	ofstream obj2("output.txt");
	int totalcases;
	obj.getline(num,digits);
	totalcases=atoi(num);
	for(int cases=0;cases<totalcases;cases++)
	{
		//obj.getline(num,digits,' ');
		//A=atoi(num);
		//obj.getline(num,digits,' ');
		//B=atoi(num);
		struct Indexer* indexer1=InitIndexer();
		struct Indexer* indexer2=InitIndexer();

		obj>>A;
		obj>>B;
		count=0;
		for(int n=A;n<=B;n++)
		{
			itoa(n,num,10);
			for(int z=1;z<digits&&num[z]!='\0';z++)
			{
				int k=0;
				int j;
				for(j=z;j<digits&&num[j]!='\0';j++)
				{
					m[k]=num[j];
					k++;
				}
				int l=0;
			
				for(;k<digits&&l<z;k++)
				{
					m[k]=num[l];
					l++;
				}
				m[k]='\0';
				int m1=atoi(m);
				if(m1>=A&&m1<=B&&n!=m1)
				{
					if(search(indexer1,m1)&&search(indexer2,n))
					{
					}
					else if(search(indexer1,n)&&search(indexer2,m1))
					{
					}
					else
					{
						count++;
						Insert(indexer2,m1);
						Insert(indexer1,n);
						//cout<<n<<","<<m1<<endl;
					}
				
				}
			}
		}
		obj2<<"Case #"<<cases+1<<": "<<count<<endl;
	}
	return 0;
}
