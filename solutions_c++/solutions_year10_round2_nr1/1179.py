// Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;



int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("A-large.in");
	ofstream out ("A-large.out");

	int t=0;
	in >> t;
	for (int i =0;i<t;i++)
	{
		int m, n;
		in >> n >> ws >> m >>ws;
		map<string,int> have;
		map<string,int>want;
		for (int j=0;j<n;j++)
		{
			string s;
			getline(in,s,'\n');

			int pos = s.find("/",1);
			while(true)
			{		
				string temp = s.substr(0,pos);
				have[temp]++;			
				if (pos==-1)
					break;
				pos = s.find("/",pos+1);
			}
		}
		for (int j=0;j<m;j++)
		{
			string s;
			getline(in,s,'\n');

			int pos = s.find("/",1);
			while(true)
			{		
				string temp = s.substr(0,pos);
				want[temp]++;			
				if (pos==-1)
					break;
				pos = s.find("/",pos+1);
			}
		}

		int count =have.size();

		for (map<string,int>::iterator p = want.begin();p!=want.end();p++)
		{
			if (have.find(p->first)==have.end())
			{
				string s = p->first;

				int pos = s.find("/",1);
				while(true)
				{		
					string temp = s.substr(0,pos);
					have[temp]++;			
					if (pos==-1)
						break;
					pos = s.find("/",pos+1);
				}

			}

		}

		//for (map<string,int>::iterator p = want.begin();p!=want.end();p++)
		//	cout << p->first << endl;
		cout << "Case #" << i+1 <<": " << (have.size()-count) << endl;
		out << "Case #" << i+1 <<": " << (have.size()-count) << endl;

	}


	in.close();
	out.close();

	return 0;
}

