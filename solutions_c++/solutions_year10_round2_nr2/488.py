#include <fstream>
#include <vector>

using namespace std;

struct chick{
	int x,v;
};

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for(int cases=1;cases<=t;cases++)
	{
		int n,k,b,t;
		fin >> n >> k >> b >> t;
		vector <chick> chicks;
		for(int i=0;i<n;i++)
		{
			chick temp;
			fin >> temp.x;
			chicks.push_back(temp);
		}
		for(int i=0;i<n;i++)
		{
			int temp;
			fin >> temp;
			chicks[i].v=temp;
		}
		int have_to_pick_up=0;
		int moves=0;
		int will_arrive=0;
		int min_moves=0;
		int i=n-1;
		bool must=true;
		while (must&&(i>=0))
		{
			if (will_arrive==k)
			{
				min_moves=moves;
				must=false;
			}
			int dis=b-chicks[i].x;
			if ((double)dis/(double)chicks[i].v>t)
				have_to_pick_up++;
			else
			{
				will_arrive++;
				moves+=have_to_pick_up;
			}
			i--;
		}
		if (must&&(will_arrive==k))
			{
				min_moves=moves;
				must=false;
			}
		if (must)
			fout << "Case #" << cases << ": " << "IMPOSSIBLE" << endl;
		else
			fout << "Case #" << cases << ": " << min_moves << endl;

	}

}