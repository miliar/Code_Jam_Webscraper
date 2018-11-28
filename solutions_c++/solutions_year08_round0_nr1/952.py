#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<vector>
#include<bitset>

using namespace std;
using std::bitset;

int process();
size_t count(vector<bool> x);

vector<string> searcher;
vector<string> query;

int main()
{
	int N,S,Q;
	string stn;
	cout<<"Input the filename:"<<endl;
		//从文件输入
	string filename;
	cin>>filename;
	ifstream infile(filename.c_str());

	if(!infile)
	{
		cerr<<"error: enable to open input file: "
			<<filename<<endl;
		exit(0);
	}

	getline(infile, stn);
	stringstream input_string(stn);
	input_string>>N;

	ofstream outfile("out.txt");

	for(int i=0;i<N;i++)
	{
		getline(infile, stn);
		stringstream S_string(stn);
		S_string>>S;
		
		for(int j=0;j<S;j++)
		{
			getline(infile, stn);
			searcher.push_back(stn);
		}

		getline(infile, stn);
		stringstream Q_string(stn);
		Q_string>>Q;

		for(int j=0;j<Q;j++)
		{
			getline(infile, stn);
			query.push_back(stn);
		}

		int temp=process();

		searcher.clear();
		query.clear();

		outfile<<"Case #"<<i+1<<": "<<temp<<"\n";
		cout<<"Case #"<<i+1<<": "<<temp<<endl;
	}

	outfile.close();

	return 0;
}

int process()
{
	int ensw=0;
	size_t n = searcher.size();
	vector<bool> insearch;
	insearch.resize(n);
	for(size_t i=0;i<n;i++)
		insearch[i]=false;
	
	//cout<<"*****************************"<<endl;
	for(size_t i=0;i<query.size();i++)
	{
		//cout<<"*****************************"<<endl;
		for(size_t j=0;j<searcher.size();j++)
		{
			if(query[i]==searcher[j])
				insearch[j]=true;
			else
				continue;

			size_t co=count(insearch);
			if(co<n)
				break;
			else if(co==n)
			{
				ensw++;
				for(size_t k=0;k<n;k++)
					insearch[k]=false;
				insearch[j]=true;
			}
			else
				cout<<"n err!"<<endl;
			break;
		}
	}
	return ensw;
}

size_t count(vector<bool> x)
{
	size_t co=0;
	for(size_t i=0;i<x.size();i++)
	{
		if(x[i]==true)
			co++;
	}
	//cout<<co<<endl;
	return co;
}