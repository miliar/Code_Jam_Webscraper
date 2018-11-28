/*#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;


int main()
{
	//vector<int> a(5);
	//vector<vector<int> > prueba(8,a);
	/*vector<vector<int> > prueba;
	prueba.push_back(*(new vector<int>));
	prueba[0].push_back(9);
	cout<<prueba[0][0];

	vector<vector<int> > memo;
	vector<int> temp(150);
	memo=*(new vector<vector<int> >(150,temp));
	memo[0][0]=9;
	cout<<memo[0][0];

	return 0;
}*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;
vector<vector<int> >memo;
vector<string> buscadores,palabras;
int DP(int s,int q)
{
	int r=0,indice;
	/*if(buscadores[s].compare(palabras[q])==0)
	{
		r=memo[q][s];

	}
	else
	{
		r=memo[q][s];
	
	}*/
	r=memo[q][s];
	if(r!=-1)
		return r;
	else if(q==palabras.size()-1)
	{
		if(buscadores[s].compare(palabras[q])==0)
		{
			r=1;
		}
		else
		{
			r=0;
		}
	}
	else
	{	
		if(buscadores[s].compare(palabras[q])!=0)
		{
			r=DP(s,q+1);
		}
		else
		{
			int temp=100000;
			for(int i=0;i<buscadores.size();++i)
			{
				if(i!=s)
				{
					int aux=DP(i,q+1)+1;
					if(aux<temp)
						temp=aux;
				}
			}
			r=temp;
		}
	}
	memo[q][s]=r;
	return r;
}


int main()
{
	ifstream entrada("A-large.in");
	ofstream salida("salida.out");
	int N;
	entrada>>N;
	for(int _N=0;_N<N;_N++)
	{
		vector<int> _memo(101,-1);
		memo.clear();
		memo.resize(1001,_memo);
		int S,Q;
		buscadores.clear();
		palabras.clear();
		string cadena;
		entrada>>S;
		getline(entrada,cadena);
		for(int _S=0;_S<S;_S++)
		{			
			getline(entrada,cadena);
			buscadores.push_back(cadena);
		}
		entrada>>Q;
		getline(entrada,cadena);
		for(int _Q=0;_Q<Q;_Q++)
		{
			getline(entrada,cadena);
			palabras.push_back(cadena);
		}
		int r;
		if(Q==0)
			r=0;
		else
		{
			int temp=100000;
			for(int i=0;i<buscadores.size();++i)
			{
			//	memo.clear();
			//	memo.resize(1001,_memo);
				int aux=DP(i,0);
				if(aux<temp)
					temp=aux;
				if(temp==0)
					break;
			}
			r=temp;
		}
			
		salida<<"Case #"<<_N+1<<": "<<r<<endl;

	}
	return 0;
}