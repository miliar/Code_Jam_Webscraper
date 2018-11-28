#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

char buf[10000];

int main()
{
	FILE *f = fopen("in.txt","r");
	int tests;
	fscanf(f,"%d",&tests);
	for(int test = 1; test <= tests; test++)
	{
		fscanf(f,"%s",&buf[0]);
		string s(buf);

		vector<int> out;

		map<char,int> x;
		x[s[0]] = 1;
		out.push_back(1);
	//	cout << s[0] << ":"<<out.back()<< " ";

		int free_number = 0;
		for(int i=1; i<s.size(); i++) {
			if(x.find(s[i]) == x.end()) {
				x[s[i]]=free_number;
				if(free_number==0)
					free_number=2;
				else
					free_number++;
			}
			out.push_back(x[s[i]]);
	//		cout << s[i] << ":" << out.back() << " ";
		}
		//cout << endl;
		int base = x.size();
		if(base==1)
			base=2;

		long long res = 0;
		for(int i=0;i<out.size();i++)
			res = res*base+out[i];

		printf("Case #%d: %lld\n",test,res);
	}
	return 0;
}
