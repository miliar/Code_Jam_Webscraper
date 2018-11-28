#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

struct vine
{
	int distance;
	int length;
	int best;
};

void solve(int x)
{
	int num_of_vines;
	fin>>num_of_vines;
	vine* vines = new vine[num_of_vines + 5];
	for (int i = 1;i <= num_of_vines;++i)
	{
		fin>>vines[i].distance>>vines[i].length;
		vines[i].best = 0;
	}
	int len_between_ledges;
	fin>>len_between_ledges;
	vines[1].best = vines[1].distance;
	bool flag = false;

	for (int i = 1;i <= num_of_vines;++i)
	{
		if (vines[i].distance + vines[i].best >= len_between_ledges)
		{
			flag = true;
			break;
		}
		else
		{
			for (int j = i+1; j <= num_of_vines && (vines[j].distance - vines[i].distance) <= vines[i].best; ++j)
			{
				vines[j].best = max(vines[j].best, min(vines[j].distance - vines[i].distance, vines[j].length));
			}
		}
	}
	delete []vines;

	fout<<"Case #"<<x<<": ";
	if (flag == true)
	{
		fout<<"YES"<<endl;
	} 
	else
	{
		fout<<"NO"<<endl;
	}


}

int main()
{

	int num_of_case = 0;
	fin>>num_of_case;
	for (int i = 0;i < num_of_case;++i)
	{
		solve(i+1);
	}
}