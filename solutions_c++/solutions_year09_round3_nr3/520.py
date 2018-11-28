#include<iostream>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<iomanip>
#include<algorithm>
#include<locale>
#include<cmath>
#include<cstdlib>

using namespace std;

int main()
{
	ifstream fin
	("files\\C1.in");
	ofstream fout
	("files\\C1.out");


	int N;
	fin>>N;

	for(int i = 0; i < N; i++)
	{
		cout<<"=====Case #"<< i+1 <<"====="<<endl;
		int P, Q;
		fin>>P>>Q;
		set<int> rel;
		vector<int> all;
		for(int j = 0; j < Q; j++)
		{
			int in;
			fin>>in;
			all.push_back(in);
		}
		int minn = P*P;
		do
		{
			//cout<<"----"<<endl;
			int result = 0;
			set<int>::iterator it;
			rel.clear();
			rel.insert(0);
			rel.insert(P+1);
			for(int j = 0; j < Q; j++)
			{
				it = rel.insert(all[j]).first;
				int e = *(++it);
				it--;
				int b = *(--it);
				result +=e-b-2;
				//cout<<e<<" "<<b<<" "<<result<<endl;
			}
			minn = min(minn, result);
		}
		while(next_permutation(all.begin(), all.end()));

		fout<<"Case #"<< i+1 <<": "<<minn<<endl;
		cout<<"Case #"<< i+1 <<": "<<minn<<endl;
	}
}
