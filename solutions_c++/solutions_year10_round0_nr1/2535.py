#include<iostream>
#include<fstream>
using namespace std;

ofstream outfile("res.txt", ios::out);
int T,N,K;

int main()
{
	while(cin>>T)
	{
		int count;
		for(count = 1; count <= T; count++)
		{
			cin>>N>>K;
			__int64 cir = (1 << N);	
			outfile<<"Case #"<<count<<": ";
			if((K+1) % cir == 0)
				outfile<<"ON"<<endl;
			else
				outfile<<"OFF"<<endl;
		}
	}
	outfile.close();
	return 0;
}
