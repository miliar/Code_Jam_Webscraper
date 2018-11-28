#line 3 "main.cpp"
#include  "iostream" 
#include  "vector"
#include  "string"
#include  "string.h"
#include  "algorithm" 
#include  "sstream"
#include  "set"
#include  "map"
#include  "queue"
#include  "deque"
#include  "stack"
#include "list"
#include  "bitset"
#include  "cstdio"
#include  "assert.h"
#include  "cmath"
#include  "cstdlib"
#include  "ctime"
#include  "cfloat"
using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define INF 1LL<<30

using namespace std;

int r,res;

long long memo[3000+5][20];
int tem[10000],pode[10000],val[3000+5];
bool esta[3000+5][20];

long long go(int no, int ini, int fin, int posibles){
	
	//cout<<ini<<" "<<fin
	if(ini == fin)
	{
		if(tem[ini] > posibles) 
			return INF;
		else return 0;
	}

	if(esta[no][posibles]) 
		return memo[no][posibles];
	
	long long res = INF;
	//vai1
	res = min(res, go(no * 2 + 1, ini, (ini + fin) / 2, posibles)+ go(no * 2 + 2,(ini + fin) / 2 + 1, fin, posibles));
	
	//vai 2
	res = min(res, val[no] + go(no * 2 + 1, ini, (ini + fin) / 2, posibles + 1) + go(no * 2 + 2,(ini + fin) / 2 + 1, fin, posibles + 1));

	
	esta[no][posibles] = true;
	memo[no][posibles]=res;
	return res;	
}
int main()
{

	
	freopen("Blarga.in","r",stdin);
	 freopen("C:\\Documents and Settings\\jpenam\\Escritorio\\gcj\\BLargares.out","w",stdout);
	
	int cases;
	cin>>cases;
	for(int ii=0;ii<cases;ii++)
	{
		int P; 
		cin >> P;
		int tamanho=(1 << P);
		for(int i = 0; i < tamanho; i++)
			scanf("%d", &pode[i]);
			
		vector< vector<int> > todos(P);
		
		int teng=(1<<(P-1));
		for(int i = 0; i < P; i++)
		{
			//para los nuevos
			todos[i] = vector<int> (teng);
			for(int j = 0; j < teng; j++)
				scanf("%d", &todos[i][j]);
			//cut<<teng<<endl;
			teng>>=1;
		}
		int nodo = 0;
		for(int i = todos.size() - 1; i >= 0; i--)
			for(int j = 0; j < todos[i].size(); j++)
				val[nodo++] = todos[i][j];

		int cur;
		
		for(int i = 0; i < tamanho; i++)
		{
			cur = P - pode[i];
			tem[i] = cur;
		}		

		memset(esta, false, sizeof esta);
		memset(memo,0,sizeof memo);
		long long res = go(0, 0, tamanho - 1, 0);
		
		cout<<"Case #"<<ii+1<<": ";
		cout<<res<<endl;
	}

	return 0;
}