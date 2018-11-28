// Q Problem B. Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include "string"
#include "fstream"
#include "iostream"
using namespace std;

int main()
{
	ifstream entra("B-small-attempt2.in");
	ofstream fuera("Data.txt");
	int T,C,D,N,j,k;
	char *inv;
	string comb,op,obj;
	entra>>T;
	for(int i=1;i<=T;i++)
	{
		comb.erase(0,comb.size());
		op.erase(0,op.size());
		obj.erase(0,obj.size());
		entra>>C;
		comb.append(10,'a');
		for(j=0;j<C;j++)
		{
			comb.erase(0,comb.size());
			entra>>comb;
		}
		entra>>D;
		op.append(10,'b');
		for(j=0;j<D;j++)
		{
			op.erase(0,op.size());
			entra>>op;
		}
		entra>>N;
		inv=new char[N+1];
		obj.append(1,'c');
		k=1;
		for(j=0;j<N;j++,k++)
		{
			entra>>inv[j];
			obj.append(1,inv[j]);
			if(obj.size()>2)
			if((comb.at(0)==obj.at(k)&&comb.at(1)==obj.at(k-1))||(comb.at(1)==obj.at(k)&&comb.at(0)==obj.at(k-1)))
			{
				obj.replace(k-1,2,comb.substr(2,1));
				k--;
			}
			if(obj.size()>2)
			if(obj.at(k)==op.at(0))
				for(int l=(k-1);l>0;l--)
					if(obj.at(l)==op.at(1))
					{
						obj.erase(1,obj.size()-1);
						k=0;
						break;
					}
			if(obj.size()>2)
			if(obj.at(k)==op.at(1))
				for(int l=(k-1);l>0;l--)
					if(obj.at(l)==op.at(0))
					{
						obj.erase(1,obj.size()-1);
						k=0;
						break;
					}
		}
		fuera<<"Case #"<<i<<": [";
		if(obj.size()>1)
		{
			j=1;
			for(j=1;j<obj.size()-1;j++)
				fuera<<obj.at(j)<<", ";
			fuera<<obj.at(j)<<"]"<<endl;
		}
		else
			fuera<<"]"<<endl;
	}
}
