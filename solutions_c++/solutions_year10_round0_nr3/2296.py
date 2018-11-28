#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream fin("C.in");
	ofstream fout("C.out");
	int T;
	long R;
	long K;
	int N;
	long g[1010];
	fin>>T;
	int n=1;
	while(n<=T)
	{
		int money=0;
		fin>>R>>K>>N;
		int i=0,j=0,time=0,turn=0,now=0;
		for(i=0;i<N;i++)
			fin>>g[i];
		for(time=1;time<=R;time++)
		{
			int gnum=1;
			now=0;
			turn=turn%N;
			now=g[turn];
			turn=(turn+1)%N;
			while((now+g[turn])<=K && gnum<N)
			{
				now=now+g[turn];
				turn=(turn+1)%N;
				gnum++;
			}
			money=money+now;
		}
		fout<<"Case #"<<n<<": ";
		fout<<money<<endl;
		cout<<"Case #"<<n<<": ";
		cout<<money<<endl;
		n++;
	}
	fin.close();
	return 0;
}