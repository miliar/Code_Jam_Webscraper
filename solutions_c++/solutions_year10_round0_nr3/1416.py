// Theme-Park.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int case_num=0;
	int r,k,n;
	int gi[1001];
	int gk[1001];
	int gk_next[1001];
	long long count,y;

	fstream fr("C-large-3.in",ios::in);
	  fstream fw;
	fw.open("output-3.txt",ios::out);
	fr>>case_num;
  
	for(int ii=0;ii<case_num;ii++)
	{
		int j;
		count=0;
		y=0;
		fr>>r>>k>>n;
		for(j=0;j<n;j++)
		{fr>>gi[j];}
		int cout1=0;
		int begin=0,end=0,end2=0;
		if(n>1)
		for(j=0;j<n;j++)
		{
			if(end<begin)
			   end2=end+n;
			else end2=end;
			while((cout1<k)&&(cout1+gi[end]<=k)&&(end2-begin<n))
			{
			
				cout1+=gi[end];
				end=(end+1)%n;
				end2++;

			}
			gk[j]=cout1;
			gk_next[j]=end;

			cout1=cout1-gi[begin];
			begin=(begin+1)%n;			

		}
		else{gk[0]=gi[0];gk_next[0]=0;}
		count=0;
		y=0;
		int next=0;
		for(int p=0;p<r;p++)
		{
		
			y+=gk[next];
	        next=gk_next[next];

		}
		fw<<"Case #"<<ii+1<<": "<<y<<endl;

	}

	fr.close();
	fw.close();
	return 0;
	
}

