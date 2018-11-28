#include <fstream>
#include <queue>

using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");

int main()
{
	int T, R, k, N, i, e, Gi, S, Res;
	queue<int> G;
	queue<int> go;
	fin>>T;
	for(i=0;i<T;++i)
	{
		fin>>R>>k>>N;
		for(e=0;e<N;++e)
		{
			fin>>Gi;
			G.push(Gi);
		}
		S = 0;
		Gi = 0;
		Res = 0;
		for(e=0;e<R;++e)
		{
			S = 0;
			while(((S + G.front()) <= k) && !G.empty())
			{
				Gi = G.front();
				S += Gi;
				G.pop();
				go.push(Gi);
			}
			while(!go.empty())
			{
				G.push(go.front());
				go.pop();
			}
			Res += S;
		}
		fout<<"Case #"<<i+1<<": "<<Res<<endl;
		while(!G.empty())
			G.pop();
	}
	return 0;
}
