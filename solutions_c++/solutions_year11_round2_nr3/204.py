#include <iostream>
#include <vector>
using namespace std;

int T, N, M;
vector<vector<int> > h;
int farbs, best;
int col[10], final[10];
bool flag;
	
void read_case()
{
	vector<int> rAB, rBA;
	int A, B;
	int pA, pB, p;
	int U[10], V[10];
	
	cin>>N>>M;
	h.clear();
	
	for (int i=1; i<=N; i++)
		rAB.push_back(i);
	h.push_back(rAB);
	
	for (int w=0; w<M; w++)
		cin>>U[w];
	for (int w=0; w<M; w++)
		cin>>V[w];
	
	for (int w=0; w<M; w++)
	{
		A = U[w];
		B = V[w];
		for (int i=0; i<h.size(); i++)
		{
			pA = -1;
			pB = -1;
			for (int j=0; j<h[i].size(); j++)
			{
				if (h[i][j]==A)
					pA = j;
				if (h[i][j]==B)
					pB = j;
			}
			if (pA==-1 || pB==-1)
				continue;
			rAB.clear();
			rBA.clear();
			
			p=pA;
			do
			{
				rAB.push_back(h[i][p]);
				p = (p+1)%(h[i].size());
			} while (h[i][p]!=B);
			rAB.push_back(B);
			
			p=pB;
			do
			{
				rBA.push_back(h[i][p]);
				p = (p+1)%(h[i].size());
			} while (h[i][p]!=A);
			rBA.push_back(A);
			
			h[i].clear();
			h[i] = rAB;
			h.push_back(rBA);
			
			break;
		}
	}
	/*
	for (int i=0; i<h.size(); i++)
	{
		cout<<"ROOM "<<i<<" : "<<endl;
		for (int j=0; j<h[i].size(); j++)
			cout<<h[i][j]<<" ";
		cout<<endl;
	}
	*/
}

void check()
{
	bool used[10];
	bool ok(true);
	
	for (int i=0; i<h.size(); i++)
	{
		for (int j=1; j<=farbs; j++)
			used[j] = false;
		for (int j=0; j<h[i].size(); j++)
			used[col[h[i][j]]] = true;
		for (int j=1; j<=farbs;j++)
			if (!used[j])
				ok = false;
	}
	
	if (ok)
	{
		best = farbs;
		for (int i=1; i<=N; i++)
			final[i] = col[i];
		flag = true;
	}
}

void paint(int v)
{
	if (flag)
		return;
	if (v>N)
		check();
	else
	{
		for (int c=1; c<=farbs; c++)
		{
			col[v] = c;
			paint(v+1);
		}
	}
}

int lin_search()
{
	for (int i=1; i<=N; i++)
	{
		farbs = i;
		flag = false;
		//cout<<"FARBS :"<<farbs<<endl;
		paint(1);
		if (best<farbs)
			break;
	}
	
	cout<<best<<endl;
	for (int i=1; i<N; i++)
		cout<<final[i]<<" ";
	cout<<final[N]<<endl;
}
	
int main()
{
	cin>>T;
	for (int i=0; i<T; i++)
	{
		cout<<"Case #"<<i+1<<": ";
		read_case();
		lin_search();
	}
	return 0;
}


