
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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

ifstream in("A-large.in");
ofstream out("A-large.out");

int N;
int cal();
void main()
{
	in>>N;
	for(int i=0;i<N;i++)
	{
		int r = cal();
		out<<"Case #"<<i+1<<": "<<r<<endl;
		cout<<"Case #"<<i+1<<": "<<r<<endl;



	}	
	in.close();
	out.close();
}

int wn;  //word count
int sn;  //seq count
int data[1024];
int cost[105][1024];

int compute(int choice, int pos)
{
	if(cost[choice][pos])
		return cost[choice][pos];
	int& p = cost[choice][pos];
	if(data[pos] == choice)
	{
		p = 10000;
		return p;
	}
	int i = pos+1;
	for(;i<sn;i++)
	{
		if(data[i]==choice)
			break;
	}

	if(i==sn)
	{
		p = 1;
		return p;
	}
	p = compute(0,i)+1;
	for(int j=1;j<wn;j++)
	{
		p = min(p,compute(j,i)+1);
	}
	return p;

}

int cal()
{
	
	
	memset(data,255,sizeof(data));
	memset(cost,0,sizeof(cost));
	cout<<sizeof(cost)<<endl;


	map<string,int> mp;
	in>>wn;
	int count = 0;
	char tmp[120];
	in.getline(tmp,120); //remove the "/n"
	string s;
	for(int i=0;i<wn;i++)
	{
		in.getline(tmp,120);
		s = tmp;
		mp[s] = count++;
	}

	in>>sn;
	if(sn==0)
		return 0;
	in.getline(tmp,120);
	count=0;
	for(int i=0;i<sn;i++)
	{
		in.getline(tmp,120);
		s = tmp;
		data[count++] = mp[s];		

	}
	cout<<"finished parsing one case"<<endl;
	int res = 10000;

	for(int i=0;i<wn;i++)
	{
		res = min(res,compute(i,0)-1);

	}
	return res;








}