// codejam_q_2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
using namespace std;

int main()
{

	freopen("inp.txt","r",stdin);

	freopen("out.txt","w",stdout);

	int *total;

	int mapp[31][2]={{0},{1},{1,2},{1,2},{2,2},{2,3},{2,3},{3,3},{3,4},{3,4},{4,4},{4,5},{4,5},{5,5},{5,6},{5,6},{6,6},{6,7},{6,7},{7,7},{7,8},{7,8},{8,8},{8,9},{8,9},{9,9},{9,10},{9,10},{10,10},{10},{10}};

	int testcases,i,t,n,s,p,max=0,m=0;

	cin>>testcases;

	


	t=testcases;

	while(t)
	{
		max=0;

		cin>>n;

		cin>>s;
	
		cin>>p;

		
		
		

		total=new int[n];

		for(i=0;i<n;i++)
		{
			cin>>total[i];

			


			if((total[i]>28 || total[i]<2)&&(mapp[total[i]][0]>=p))
				max++;
			else
			{
				if((mapp[total[i]][0]<p) && (mapp[total[i]][1]>=p))
				{
					if(s!=0)
					{
					s--;
					
					max++;

					
					}
				}
				else if(mapp[total[i]][0]>=p)
				{
					max++;

					m++;

					
				}
			}

			}

		
		if((m-s)<0)
			printf("Case #%d: %d\n",testcases-t+1,0);
			 
		else
		printf("Case #%d: %d\n",testcases-t+1,max);

		

		t--;

		delete[] total;
	}

}



