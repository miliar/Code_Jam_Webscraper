// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <set>
#include <vector>
#include <list>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	fstream in("C-small-attempt0.in",ios::in);
	fstream out("C-small.out",ios::out);

	int T,R,K,N;
	int i,j,u,v;
	int g[1001];
	int max[1001];
	int jump[1001];
	bool flag;
	int pos;
	int sum;
	int result;

	in>>T;
	for(i=0;i<T;i++)
	{
		result=0;
		in>>R>>K>>N;
		for(j=0;j<N;j++)
		{
			in>>g[j];
			max[j]=g[j];
		}
		flag=false;
		sum=0;
		for(j=0;j<N;j++)
		{
			sum+=g[j];
			if(sum>K)
			{
				flag=true;
				break;
				
			}
		}

		
		if(flag)
		{
			for(j=0;j<N;j++)
			{
				u=j;
				if(++u==N)
					u=0;
				while((max[j]+g[u])<=K)
				{			
					max[j]+=g[u];
					if(++u==N)
						u=0;
				}
				jump[j]=u;
			}
/*
			for(j=0;j<N;j++)
				cout<<max[j]<<" ";
			cout<<endl;
			for(j=0;j<N;j++)
				cout<<jump[j]<<" ";
			cout<<endl;*/


			pos=0;
			for(j=0;j<R;j++)
			{
				result+=max[pos];
				pos=jump[pos];
			}

		}else
		{
			result=R*sum;
		}
		out<<"Case #"<<1+i<<": "<<result<<endl;

	}


		
	

	in.close();
	out.close();
	return 0;
}

