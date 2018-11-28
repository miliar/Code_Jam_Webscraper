#include <fstream>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <sstream>
#include <map>
#include <hash_set>

using namespace std;

int main()
	{
	ifstream inf("A-large.in");
	ofstream ouf("A-small-attempt2.out");
	int T;
	inf >> T;
	for(int k=0;k<T;k++)
		{
		int N;
		inf >> N;
		int o=N;
		map<int,int> pole;
		while(o--)
			{
			int a,b;
			inf >> a >> b;
			pole.insert(make_pair(a,b));
			}
		int ret=0;		
		for(map<int,int>::iterator it=pole.begin();it!=pole.end();it++)
			for(map<int,int>::iterator jt=pole.begin();jt!=pole.end();jt++)
				if (((*it).first<(*jt).first&&(*jt).second<(*it).second)||((*jt).first<(*it).first&&(*jt).second>(*it).second)) ret++;
		ouf << "Case #" << (k+1) << ": " << (ret/2)  << endl;
		}
	}