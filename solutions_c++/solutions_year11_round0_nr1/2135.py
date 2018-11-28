#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct state
{
	string robot;
	int button;
};

int process(vector<state> seq)
{
	int last = -1;
	int start = 0;
	int time = 0;
	int prev = 0;
	int i=0;
	while(i < (int) seq.size())
	{
		start = seq[i].button;
		if(prev != 0)
		{
			int dist = seq[i].button;
			if(last >= 0)
				dist = abs(dist - seq[last].button);
			else
				dist -= 1;
			if(prev >= dist)
				start = 1;
			else
				start = dist - prev + 1;
		}
		int j = i+1;
		int num = 0;
		bool has_seq = false;
		while(j < (int)seq.size() && seq[j].robot == seq[i].robot)
		{
			num += abs(seq[j].button - seq[j-1].button) + 1;
			j++;
			has_seq = true;
		}
		last = i-1;
		if(has_seq)
		{
			i = j;
		}
		else
		{
			i++;
		}
		prev = num + start;
		time += prev;
	}
	return time;
}

void main()
{
	ifstream f("Input.txt");
	ofstream outfile("Output.txt");
	int T, N;
	f >> T;
	for(int i=0; i<T; i++)
	{
		f >> N;
		vector<state> seq;
		for(int j=0; j<N; j++)
		{
			string label;
			int button;
			f >> label >> button;
			state s;
			s.robot = label; s.button = button;
			seq.push_back(s);
		}
		int time = process(seq);
		outfile << "Case #" << i+1 << ": " << time << endl;
	}
	outfile.close();
	f.close();
}