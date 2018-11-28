#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>

using namespace std;


int main()
{
	ifstream fi("credit.in");
	ofstream fo("credit.out");

	int T, N, M;
	fi>>T;

	set<string> spath;
	for(int t=1; t<=T; t++)
	{
		fo<<"Case #"<<t<<": ";
		fi>>N>>M;

		spath.clear();
		string tmp;
		for(int i=0; i<N; i++)
		{
			fi>>tmp;
			spath.insert(tmp);

			int lp=tmp.find_last_of('/');
			while(lp!=4294967296&&lp!=0)
			{
				tmp=tmp.substr(0,lp);
				spath.insert(tmp);
				lp=tmp.find_last_of('/');
			}
		}

		int count=0;
		set<string>::iterator it;
		for(int i=0; i<M; i++)
		{
			fi>>tmp;
			it=spath.find(tmp);
			while(it==spath.end())
			{
				count++;
				spath.insert(tmp);
				int lp=tmp.find_last_of('/');
				tmp=tmp.substr(0,lp);
				if(tmp=="") break;
				it=spath.find(tmp);
			}
		}
		fo<<count<<endl;
	}
}

			




