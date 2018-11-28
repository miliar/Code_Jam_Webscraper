#include <iostream>
#include <fstream>
using namespace std;

int state[40];
int k;
int n;
int T;
int num;

int Min(int a,int b)
{
	return (a<b)?a:b;
}

int main()
{
	ifstream ifs("in.txt");
	ofstream ofs("out.txt");
	
	ifs>>T;
	
	for(int l=0;l<T;l++){
	num=1;
	
	ifs>>n;
	ifs>>k;
	
	for(int u=0;u<40;u++)
	state[u]=0;
	
	for(int i=0;i<k;i++)
	{
		for(int j=0;j<Min(num,n);j++)
		{	
			state[j]=1-state[j];
		}
		int count=0;
		
		while(state[count]==1)count++;
		
		num=count+1;
	}
	
	ofs<<"Case #"<<l+1<<": ";
	if(num>=n+1)ofs<<"ON"<<endl;
	else ofs<<"OFF"<<endl;
	}
	
	return 0;

}