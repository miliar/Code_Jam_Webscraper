#include <iostream>
#include <fstream>
#include <set>
#include <string>;

using namespace std;

void main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");

	set<string> ss;

	int s,n,q;
	int i,j;
	int cnt;
	string str;
	
	ifs>>n;

	for(i=0; i<n; i++)
	{
		cnt=0;
		ss.clear();

		ifs>>s;
		getline(ifs,str);
		for(j=0; j<s; j++)
			getline(ifs,str);
		
		ifs>>q;
		getline(ifs,str);
		for(j=0; j<q; j++)
		{
			getline(ifs,str);
			ss.insert(str);
			if(ss.size()==s)
			{
				ss.clear();
				ss.insert(str);
				cnt++;
			}
		}
		ofs<<"Case #"<<i+1<<": "<<cnt<<endl;
	}
}