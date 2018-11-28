#include <iostream>
#include <fstream>
//#include <stdlib.h>
#include <string.h>
using namespace std;
short P,N;
int tp[100];
int mp[100];
int rp[100];
short find(short K)
{
	short temp=0;
	for(int i=0; i<N;i++)
	{
		if(mp[i]>=K)
			temp++;
	}
	return temp;
}

short finds(short K)
{
	short temp=0;
	for(int i=0; i<N;i++)
	{
		if(mp[i]==K)
			if(rp[i]!=1)
			temp++;
	}

	


	return temp;
}

int main()
{

	ifstream fi;
	ofstream fo;
	short T,S,temp;
	int count=0;

	fi.open("B-large.in");
	fo.open("B-large.out");
	fi>>T;
	for(int cases=0;cases<T;cases++)
	{
		
		fi>>N; fi>>S; fi>>P;
		for(int i=0; i<N; i++)
		{
			fi>>tp[i];
		}
		
		for(int i=0; i<N; i++)
		{
			mp[i]=tp[i]/3;
			rp[i]=tp[i]%3;
			if(tp[i]%3!=0)
			mp[i]++;
		}

                if(P==0) count=N;
		else 
		{
			count=find(P);
			if(P!=1)
			{
				temp=finds(P-1);
				if (temp<=S)
				count+=temp;
				if (temp>S)
				count+=S;
			}
		}

		fo<<"Case #"<<cases+1<<": "<<count<<endl;
		count=0;
		temp=0;
	}


	fi.close();
	fo.close();
	return 0;
}
