
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

ifstream in("B-large.in");
ofstream out("B-large.out");

int N;  //case number
int rA, rB;

void cal();
void main()
{
	in>>N;
	for(int i=0;i<N;i++)
	{
		cal();
		out<<"Case #"<<i+1<<": "<<rA<<" "<<rB<<endl;
		cout<<"Case #"<<i+1<<": "<<rA<<" "<<rB<<endl;
	}	
	in.close();
	out.close();
}

int convert(string st) //convert 10:10 to 610
{
	return ((st[0]-'0')*10 + (st[1]-'0'))*60 + (st[3]-'0')*10 + (st[4]-'0');
}

int compute(vector<int>& start, vector<int>& arrive)
{
	int res = start.size();
	
	int i = (int)start.size() - 1;
	int j = (int)arrive.size() - 1;

	for(;i>=0 && j>=0;)
	{
		if(start[i]>=arrive[j])
		{
			i--; j--; res--;
		}
		else
		{
			j--;
		}
	}

	return res;

}
void cal()
{
	int T;  //delay
	int nA; //number of schedule from A to B
	int nB; //from B to A
	string depart,arrive;
	vector<int> Astart;
	vector<int> Bstart;
	vector<int> Aarrive; //from B's car
	vector<int> Barrive; //from A's car
	in>>T>>nA>>nB;
	int t1,t2;
	for(int i=0;i<nA;i++)
	{
		in>>depart>>arrive;
		t1 = convert(depart);
		t2 = convert(arrive);
		Astart.push_back(t1);
		Barrive.push_back(t2+T);	
	}
	for(int i=0;i<nB;i++)
	{
		in>>depart>>arrive;
		t1 = convert(depart);
		t2 = convert(arrive);
		Bstart.push_back(t1);
		Aarrive.push_back(t2+T);	
	}
	sort(Astart.begin(),Astart.end());
	sort(Bstart.begin(),Bstart.end());
	sort(Aarrive.begin(),Aarrive.end());
	sort(Barrive.begin(),Barrive.end());
	rA = compute(Astart,Aarrive);
	rB = compute(Bstart,Barrive);


}