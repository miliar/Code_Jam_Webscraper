// r1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;


struct search_engine_t
{
	string name;
	list<int> encounters;
	void setnew(const string &a_name)
	{
		name=a_name;
		encounters.clear();
	}
	void skip_to(int step)
	{
		encounters.erase(encounters.begin(),
			lower_bound(encounters.begin(),encounters.end(),step)
		);
		//while (!encounters.empty() && encounters.front<step)
		//	encounters.pop_front();		
	}
	int front() { return encounters.front(); }
	void add_encount(int step) { encounters.push_back(step); }
	bool empty() { return encounters.empty(); }
	bool operator<(const search_engine_t &s) const { return name<s.name; } //for sorting and search
} ;

const int max_engines=100;
int n_engines;
search_engine_t engines[max_engines]; 

int calc_switches()
{
	int cur_step=0;
	int counter=0;
	for (;;)
	{
		int best_next_step=-1;
		for (int i=0;i<n_engines;++i)
		{
			search_engine_t &engine=engines[i];
			engine.skip_to(cur_step);
			if (engine.empty())
				return counter;
			else
				best_next_step=max(engine.front(),best_next_step);					
		}
		++counter;
		cur_step=best_next_step;
	}
}

int main(int argc, _TCHAR* argv[])
{
	int N;
	//1
	//ifstream fin("d:/fun/qr/SavingUniverse/sample.in");
	////ofstream fout("con:");
	//
	//2
	//ifstream fin("d:/fun/qr/SavingUniverse/A-small-attempt1.in");
	//ofstream fout("d:/fun/qr/SavingUniverse/A-small.output");
	ifstream fin("d:/fun/qr/SavingUniverse/A-large.in");
	ofstream fout("d:/fun/qr/SavingUniverse/A-large.output");
	fin>>N;
	assert(fin.good());
	assert(fout.good());

	for(int i_case=1;i_case<=N;++i_case)
	{
		cout<<i_case<<"\n";
		string tmp;
		//engines		
		fin>>n_engines;
		getline(fin,tmp);//skip enter
		assert(n_engines<=max_engines);		
		for (int i=0;i<n_engines;++i)
		{
			getline(fin,tmp);
			engines[i].setnew(tmp);
		}
		//sorting of engines for faster searching later
		sort(engines,engines+n_engines);
		
		//quieries
		int Q;
		fin>>Q;	
		getline(fin,tmp);
		static search_engine_t hack_engine;
		for (int i=0;i<Q;++i)
		{
			getline(fin,hack_engine.name);
			lower_bound(engines,engines+n_engines,hack_engine)->add_encount(i);
		}
		int n_switches=calc_switches();
		fout<<"Case #"<<i_case<<": "<<n_switches<<"\n";
	}
	fout.flush();	
	assert(fout.good());
	cout<<"\7Done.\n";

	int q;cin>>q;
	return 0;
}

