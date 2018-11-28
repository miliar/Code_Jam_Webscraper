#include<iostream>
#include<fstream>
#include<cstdio>
#include<map>
#include<string>
#include<utility>
#include<algorithm>
#include<list>
using namespace std;

typedef struct Server{
	string name;
	int cnt;
}server;

char tmp[101];
string last;
int n, s, q;
list<server> serverList;
list<server> bufferList;
list<server>::iterator pos;
list<server>::iterator posb;
list<string> queryList;
list<string>::iterator posq;
server node;


bool ss(const server& a, const server& b)
{

	return a.cnt < b.cnt;
}


void main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	
	in.getline(tmp, 100);
	n = atoi(tmp);
	int i=0;
	while(n--)
	{
		i++;
		int cntswitch = 0;
		queryList.clear();
		serverList.clear();
		in.getline(tmp, 100);
		s = atoi(tmp);
		while(s--)
		{
			in.getline(tmp, 100);
			node.name = tmp;
			node.cnt = 0;
			serverList.push_back(node);
		}

		in.getline(tmp, 100);
		q = atoi(tmp);
		bufferList = serverList;
		bool first=true;
		
		while(q--)
		{
			in.getline(tmp, 100);
			queryList.push_back(tmp);

			pos = bufferList.begin();
			if(bufferList.size()==1 && pos->name.compare(tmp)==0)
			{
				cntswitch++;
				bufferList=serverList;

			}

			//for(pos = serverList.begin(); pos != serverList.end(); ++pos)
			for(pos = bufferList.begin(); pos != bufferList.end(); ++pos)
			{
				if(pos->name.compare(tmp)==0)
				{
					//same remove
					bufferList.erase(pos);
					break;
				}
			}


		}

		////sort
		//stable_sort(serverList.begin(), serverList.end(), ss);

		//process
		/*pos = serverList.begin();
		for(posq = queryList.begin(); posq != queryList.end(); ++posq)
		{
			if((*posq).compare(pos->name)==0)
			{
				cntswitch++;
				if(++pos == serverList.end())
					break;
			}
		}*/

		if(cntswitch==-1)
			cntswitch=0;
		out << "Case #" << i << ": " <<cntswitch << endl;
		////output
		//for(pos = serverList.begin(); pos != serverList.end(); ++pos)
		//{
		//	cout << pos->name << "  " << pos->cnt << endl;
		//}


	}
	
}