#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	int T,N;
	long K;
	int light[35]={0};
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
	fin>>T;
	int n=1;
	while(n<=T)
	{
		fin>>N>>K;
		int i=0,j=0;
		int state;
		light[1]=1;
		for(i=2;i<=N;i++)
		{
			light[i]=(light[i-1]+1)*2-1;
		}
		state=(K+1)%(light[N]+1);
		fout<<"Case #"<<n<<": ";
		if(state==0)
			fout<<"ON"<<endl;
		else
			fout<<"OFF"<<endl;
		n++;
	}
	fin.close();
	return 0;
}