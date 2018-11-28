/*
@ author:	xlh
@ algorithm:	DP
*/

#include <map>
#include <algorithm>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;


const int MAXNUM = 999999999;

int case_count;
char l[1000];
int temp;
int server_cnt, question_cnt;
string question, last_question;

ifstream inf;
ofstream outf;

int main()
{
//open the file
	inf.open(L"Saving the Universe.in");
	outf.open(L"Saving the Universe.txt");
	inf>>case_count;

	for(int case_number=1; case_number<=case_count; case_number++)
	{
		string server;
		map<string, int> answer_map, newstate_map;

		inf>>server_cnt;
		inf.getline(l, 1000);
		for(int i=0; i<server_cnt; i++)
		{
			inf.getline(l,1000);
			server = l;
			answer_map[server] = 0;
			newstate_map[server] = MAXNUM;
		}
		inf>>question_cnt;
		inf.getline(l, 1000);
		for(int i=0; i<question_cnt; i++)
		{
			inf.getline(l,1000);
			question = l;
			for(map<string, int>::iterator it=newstate_map.begin(); it!=newstate_map.end(); it++)
				it->second = MAXNUM;
			newstate_map[question] = answer_map[question];
			for(map<string, int>::iterator it=answer_map.begin(); it!=answer_map.end(); it++)
			{
				if(it->first == last_question)
					continue;
				for(map<string, int>::iterator jt=newstate_map.begin(); jt!=newstate_map.end(); jt++)
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
			answer_map = newstate_map;
			last_question = question;
		}
		int ans = MAXNUM;
		for(map<string, int>::iterator it=answer_map.begin(); it!=answer_map.end(); it++)
			if(it->second < ans && it->first != last_question)
				ans = it->second;
		outf<<"Case #"<<case_number<<": "<<ans<<endl;
	}


//close the file
	inf.close();
	outf.close();
	return 1;
}