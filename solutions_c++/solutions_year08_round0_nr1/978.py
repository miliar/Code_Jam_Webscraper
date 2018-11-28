#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void main()
{
	int n, s, q;
	istream &in = cin;
	//ostream &out = cout;
	ofstream out("out.txt");
	char buf[101] = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff";
	in>>n;
	for(int i = 0; i < n; ++ i)
	{
		in>>s;
		in.get();
		vector<string> engines(s, string(buf));
		vector<string>::iterator p = engines.begin();
		for(; p != engines.end(); ++ p)
		{
			getline(in, *p);
			cout<<*p<<endl;
		}

		in>>q;
		in.get();
		string temp(buf);
		//vector<int> index(q, -1); 
		vector<bool> search(s, false);
		//vector<int>::iterator j = index.begin();
		int count = 0;
		int time = 0;
		//for(; j != index.end(); ++ j)
		for(int j = 0; j < q; ++ j)
		{
			getline(in, temp);
			int k = 0;
			for(p = engines.begin(); p != engines.end(); ++ p, ++ k)
			{
				if(temp == *p) 
				{
				//	*j = k;
					break;
				}
			}
			if(! search[k]) 
			{
				if(++count == s) 
				{
					++ time;
					count = 1;
					for(vector<bool>::iterator m = search.begin(); m != search.end(); ++ m) (*m) = false;
				}
				search[k] = true;
			}
		}
		out<<"Case #"<<(i+1)<<": "<<time<<endl;
	}
	out.close();
	system("out.txt");
}