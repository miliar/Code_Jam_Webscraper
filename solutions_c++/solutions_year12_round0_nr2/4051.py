// TaskB.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <string>
#include <vector>
#include <map>


int main(int argc)
{
std::vector<std::map<int,int>> data;
data.resize(31);
data.at(0)[0]=0; data.at(0)[1]=0;
data.at(30)[0]=10; data.at(30)[1]=10;
data.at(29)[0]=10; data.at(29)[1]=10;
for	(int i=1; i<29; ++i)
{
	if	(i%3==0) { data.at(i)[0]=i/3; data.at(i)[1]=1+i/3;}
	if	(i%3==1) { data.at(i)[0]=1+i/3; data.at(i)[1]=1+i/3;}
	if	(i%3==2) { data.at(i)[0]=1+i/3; data.at(i)[1]=2+i/3;}
}


int T, N,S,p; 
std::cin>>T;
for (int i=0; i<T;++i) 
{
	int res=0;
	
	std::vector<int> inp;
	std::cin>>N>>S>>p;
	inp.resize(N);
	for (int j=0; j<N;++j) 
	{
		int tmp;
		std::cin>>tmp;
		if (data.at(tmp)[0]>=p) res++;
		else if ((data.at(tmp)[1]>=p)&&(S>0)) {res++; S--; }
	}
	if (i!=0) std::cout<<std::endl; 
	std::cout<<"Case #"<<i+1<<": "<<res;
}



return 0;
}

