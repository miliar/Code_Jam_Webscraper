#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;
int main()
{
	string a="welcome to code jam";
	int N;
	vector <int> res;
	char line[505];
	ifstream in("in1.txt");
	ofstream out("out1.txt");
	in>>N;
	in.getline(line, 1);
	
	for(int i=0; i<N; i++)	{
		for(int j=0; j<503; j++)
		line[j]='\n';
		int x[19];
		for(int j=0; j<19; j++)
			x[j]=0;
		string tmp;
		int total=0;
		in.getline(line, 502);
		int c=0;
		while(line[c]!='\n')
		{
			if(a[0]==line[c])
				x[0]++;
			for(int j=1; j<19; j++)
			{
				if(a[j]==line[c])
				{
					x[j]=(x[j]+x[j-1])%1000;
				}
			}
			c++;
		}
		res.push_back(x[18]);
	}
	for(int i=0; i<N; i++){
		int tmp=(res[i])%1000;
		string zeroes="0000";
		zeroes[1]=(tmp/100)+'0';
		zeroes[2]=(tmp%100)/10+'0';
		zeroes[3]=(tmp%10)+'0';
		out<<"Case #"<<i+1<<": "<<zeroes<<endl;
	}
	return 0;
}