#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
struct Action
{
	string Name;
	int Label;
};

int solve(std::vector<Action> & Seq)
{
	int Count = 0;
	int interval = 0;
	string LastName = Seq[0].Name;
	Count = Seq[0].Label;
	interval = Seq[0].Label;
	string tempName;
	int LastButtonLabel = 1;
	for(int i = 1; i < Seq.size(); i++)
	{
		tempName = Seq[i].Name;
		if(tempName == LastName)
		{
			interval = interval + abs(Seq[i].Label - Seq[i-1].Label);
			interval++;
			Count = Count + abs(Seq[i].Label - Seq[i-1].Label) + 1;
		}
		else if(interval >= abs(Seq[i].Label - LastButtonLabel))
		{
			LastButtonLabel = Seq[i - 1].Label;
			interval = 1;
			Count = Count + 1;
			LastName = tempName;
		}
		else
		{
			Count = Count + abs(Seq[i].Label - LastButtonLabel) - interval + 1;
			interval = abs(Seq[i].Label - LastButtonLabel) - interval + 1;
			LastButtonLabel = Seq[i - 1].Label;
			LastName = tempName;
		}
	}
	return Count;
}


int main()
{
	int T;
	int N;
	int ans;
	std::vector<Action> Seq;
	Action tempAction;
	ifstream fin("A-large.in");
	fin>>T;
	ofstream fout("A-large-ans.out");
	for(int i = 0; i < T; i++)
	{
		Seq.clear();
		fin>>N;
		for(int j = 0 ;j < N; j++)
		{
			fin>>tempAction.Name;
			fin>>tempAction.Label;
			Seq.push_back(tempAction);
		}
		ans = solve(Seq);
		fout<<"Case #"<<i+1<<": "<<ans<<"\n";
	}
	fin.close();
	fout.close();
	return 0;

}