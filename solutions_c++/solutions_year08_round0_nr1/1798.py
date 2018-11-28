#include <string>
#include <fstream>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

int cc;
int temp;
int sc, qc;
string question, last_question;

ifstream inf;
ofstream outf;
map<string, int> am, nm;

void readdata()
{
	string s;
	char cl[1000];
	inf>>sc;
	inf.getline(cl, 1000);
	for(int i=0; i<sc; i++)
	{
		inf.getline(cl,1000);
		s = cl;
		am[s] = 0;
		nm[s] = 999999999;
	}
	inf>>qc;
	inf.getline(cl, 1000);
}

void slove()
{
	char cl[1000];
	for(int i=0; i<qc; i++)
	{
		inf.getline(cl,1000);
		question = cl;
		for(map<string, int>::iterator it=nm.begin(); it!=nm.end(); it++)
			it->second = 999999999;
		nm[question] = am[question];
		for(map<string, int>::iterator it=am.begin(); it!=am.end(); it++)
		{
			if(it->first == last_question)
				continue;
			for(map<string, int>::iterator jt=nm.begin(); jt!=nm.end(); jt++)
			{
				if(jt->first == question)
					continue;
				if(it->first == jt->first)
					temp = it->second;
				else
					temp = it->second + 1;
				if(temp < jt->second)
					jt->second = temp;
			}
		}
		am = nm;
		last_question = question;
	}
}

int main()
{
	inf.open(L"input.txt");
	outf.open(L"output.txt");
	inf>>cc;

	for(int cn=1; cn<=cc; cn++)
	{
		am.clear();
		nm.clear();

		readdata();

		slove();

		int answer = 999999999;
		for(map<string, int>::iterator it=am.begin(); it!=am.end(); it++)
			if(it->second < answer && it->first != last_question)
				answer = it->second;
		outf<<"Case #"<<cn<<": "<<answer<<endl;
	}


	inf.close();
	outf.close();
	return 0;
}