#include<iostream>
#include<fstream>
using namespace std;

int main(){
	ifstream is("2010Qua\\A.txt");	
	ofstream os("2010Qua\\Ao.txt");
	int C;
	while(is>>C)
	{
		for (int i = 1; i <= C; ++i)
		{
			int N, K;  is>>N>>K;
			os<<"Case #"<<i<<": ";
			K %= (1<<N);
			if (K == (1<<N)-1)
				os<<"ON"<<endl;
			else
				os<<"OFF"<<endl;
		}
	}

}