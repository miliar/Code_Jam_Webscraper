//#include "stdafx.h"
#include <string>
#include <fstream>
using namespace std;
std::ifstream in ("input");
std::ofstream out("output");

	int wlkm[19],cur;
	string str="welcome to code jam";
	string strin;
bool next()
{
	while(cur>=0)
		if(wlkm[cur]>strin.length()-1-(18-cur)) 
			cur--;
		else
		{
			if(str[cur]==strin[++wlkm[cur]]) 
				if(cur==18)
					return true; 
				else wlkm[++cur]=wlkm[cur-1];
		}
	return false;
}
int main()
{
	int i,j,n,k,count;
	in>>n;
	getline(in,strin);//перевод каретки
	for(k=0;k<n;k++)
	{
		getline(in,strin);
		for(j=0;j<strin.length();j++)
			if(str[0]==strin[j]) {wlkm[0]=j;break;}
		if(j<strin.length())
		for(i=1;i<19;i++)
			for(j=wlkm[i-1]+1;j<strin.length();j++)
			{
				if(str[i]==strin[j]) {wlkm[i]=j;break;}
			}
		cur=18;
		if(j<strin.length())
		{ count=1;
		while(next())
		{
			count++; 
			if(count==10000) count=0;
		}
		}else count=0;
		out<<"Case #"<<k+1<<": ";
		if(count<10) out<<"000";else
			if(count<100) out<<"00";else
				if(count<1000) out<<"0";
		out<<count<<'\n';
	}
	in.close();
	out.close();
	return 0;
}


