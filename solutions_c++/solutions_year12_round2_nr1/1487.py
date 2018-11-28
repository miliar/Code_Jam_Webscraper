// Problem A. Safety in Numbers.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream in("Small.in");
	ofstream out("Sdata.txt");
	int T,N,tN;
	double aux,tot;
	vector<int> S;
	vector<float> ans;
	in>>T;
	for(int t=1;t<=T;++t)
	{
		S.clear();
		tot=0;
		in>>N;
		ans.resize(N);
		for(int n=0;n<N;++n)
		{
			in>>aux;
			S.push_back(aux);
			tot+=aux;
		}
		out<<"Case #"<<t<<": ";

		tN=N;
		for(int n=0;n<N;++n)
		{
			aux=(double)(tot*2/N-S[n])*100/tot;
			if(aux<0)
			{
				aux=0;
				tN--;
			}
			ans[n]=aux;
		}
		if(tN!=N)
		{
			aux=tot;
			for(int n=0;n<N;++n)
			{
				if(ans[n]!=0)
				{
					aux+=S[n];
				}
			}
			for(int n=0;n<N;++n)
			{
				if(ans[n]!=0)
				{
					ans[n]=(double)(aux/tN-S[n])*100/tot;
				}
			}
		}

		out.setf(ios::fixed,ios::floatfield);
		for(int n=0;n<N;++n)
		{
			out<<ans[n];
			if(n!=N-1)
			{
				out<<' ';
			}
		}
		/*for(int n=0;n<N;++n)
		{
			aux=(double)(tot*2/N-S[n])*100/tot;
			out<<(aux>0?aux:0);
			if(n!=N-1)
			{
				out<<' ';
			}
		}*/
		
		out<<'\n';
	}
	return 0;
}