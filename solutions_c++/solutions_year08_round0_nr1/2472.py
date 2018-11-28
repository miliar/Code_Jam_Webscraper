#include <iostream>
#include <string>
#include <fstream>

using namespace std;


class Engine
{
	private:

		int S;
		int Q; 
		string *eng_name;
		int *eng_id;
		int *eng_freq;
		int *query_id;

	public:

		int switches;

		Engine()
		{
			eng_name = NULL;
			eng_id = NULL;
			eng_freq = NULL;
			query_id = NULL;
			switches=0;
		}
		~Engine()
		{
			delete [] eng_name;
			delete [] eng_id;
			delete [] eng_freq;
			delete [] query_id;
		}
		void Engine_get_input();
		void Engine_show();
		void Query_show();
		int Engine_id(string);
		void Engine_freq_show();
		void reset_eng_freq();
		int eng_freq_rate();
		void Engine_switches();
};

void Engine::reset_eng_freq()
{

	for(int i=0;i<S;i++)
		eng_freq[i]=0;
}

int Engine::eng_freq_rate()
{

	int sum = 0;

	for(int i=0;i<S;i++)
		if(eng_freq[i]>0) sum++;
	return sum;
}

void Engine::Engine_switches()
{


	int i=0;
	while(i<Q)
	{
		while((eng_freq_rate()<S)&&(i<Q))
		{
			
			eng_freq[query_id[i]]=eng_freq[query_id[i]]+1;
			Engine_freq_show();
			i++;
		}
		if(eng_freq_rate()==S)
		{
			reset_eng_freq();
			switches++;
			i--;
		}

	}
}



int Engine::Engine_id(string arg)
{


	int flag_id = -1;
	for(int i=0;(i<S)&&(flag_id==-1);i++)
		if(arg==eng_name[i])
			flag_id = i;
	

	if(flag_id==-1) cout << "\nERROR\n";
	return flag_id;
}


void Engine :: Engine_show()
{

	for(int i=0;i<S;i++)
		cout << eng_name[i] << endl;

}

void Engine :: Engine_freq_show()
{

	for(int i=0;i<S;i++)
		cout << eng_freq[i] << '\t';
cout << endl;

}


void Engine :: Query_show()
{

	for(int i=0;i<Q;i++)
		cout << query_id[i] << endl;

}

void Engine :: Engine_get_input()
{

	//Get number of test cases
	string dummy;

	cin >> S;
	getline(cin, dummy);

	eng_name = new string[S];
	eng_id = new int[S];
	eng_freq = new int[S];	

	for(int i=0;i<S;i++)
	{ 
		getline(cin,eng_name[i]);
		eng_id[i] = i;
		eng_freq[i]=0;
	}

	cin >> Q;
	getline(cin, dummy);		

	cin.clear();
	query_id = new int[Q];
	string arg;


	for(int i=0;i<Q;i++)
	{
		getline(cin,arg);
		query_id[i] = Engine_id(arg);
	}
	cin.clear();

}



int main()
{

	int N;
	int *sw;

	cin >> N;
	sw = new int[N];	

	int i=0;
	while(i<N)
	{
		Engine engines;

		engines.Engine_get_input();
		//	cout <<endl;
		//	engines.Engine_show();
		//	cout <<endl;
		//	engines.Query_show();
		//	cout <<endl;
		//	engines.Engine_freq_show();
		//	cout << endl;
		engines.Engine_switches();
		sw[i] = engines.switches;
		i++;

	}

	fstream f("output.txt",ios::out);

	for(int i=0;i<N;i++)
		f << "Case #" << i+1 << ": " << sw[i] << endl;

	f.close();
	delete [] sw;

}
