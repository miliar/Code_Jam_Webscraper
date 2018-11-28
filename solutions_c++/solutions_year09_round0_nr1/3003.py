#include <iostream>
#include <fstream>
#include <string>
#include <deque>
#include <limits.h>

using namespace std;

int main()	{
	ifstream in("fileAB.in");
	ofstream ou("fileAB.ou");

	size_t L,D,N;
	in>>L>>D>>N;

	deque<string> dic(D);
	for(size_t i = 0;i < D;++i)	{
		in>>dic[i];
	}

	deque<deque<string>> cas(N);
	string temp;
	for(size_t i = 0;i < N;++i)	{
		in>>temp;
		for(size_t j = 0;j < L;++j)
			if(temp[0]=='(')	{
				cas[i].push_back(temp.substr(1,temp.find(')') - 1));
				temp.erase(0,temp.find(')')+1);
			}
			else	{
				cas[i].push_back(temp.substr(0,1));
				temp.erase(0,1);
			}
	}
	size_t *casNum = new size_t[N];
	for(size_t i = 0;i < N;++i) casNum[i] = 0;
	for(size_t i = 0;i < D;++i)	{
		for(size_t j = 0;j < N;++j)	{
			bool answer = true;
			for(size_t l = 0;l < L;++l)	{
				if(cas[j][l].find(dic[i][l]) == ULONG_MAX)	{
					answer = false;
					break;
				}
			}
			if(answer)
				casNum[j]++;
		}
	}
	for(size_t i = 0;i < N;++i)
		ou<<"Case #"<<(i+1)<<": "<<casNum[i]<<endl;

	in.close();
	ou.close();
	return 0;
}