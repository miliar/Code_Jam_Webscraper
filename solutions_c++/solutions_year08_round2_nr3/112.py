#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <cmath> 
#include <queue>
#include <fstream>
#include <map>

using namespace std;



int main()
{
	ifstream in("C-small.in");
	ofstream out("C-small.out");
	int testCases; string temporary; getline(in,temporary); stringstream sinple(temporary); sinple>>testCases;
	for(int tst=0; tst<testCases; tst++)
	{
		int K, n; 
		in >> K >> n; vector <int> nums(n,0);
		for(int i=0; i<n; i++)
		{
			int tem; in >> tem; nums[i]=tem;
		}
		
		vector <int> unusedPos;
		for(int i=0; i<K; i++) unusedPos.push_back(i);
		vector <int> deck(K,-1);
		int offset = 0; int count = 0; int target = 0;
		cout << "here" << endl;
		while(target<K)
		{
			offset+=target; offset = offset%unusedPos.size();
			deck[unusedPos[offset]]=target;
			target++; unusedPos.erase(unusedPos.begin()+offset);
		}
		cout << "here again" << endl;
	
	out << "Case #" << tst+1 << ": ";
	for(int i=0; i<nums.size(); i++)
	{
		out << deck[nums[i]-1]+1; if(i<nums.size()-1) out << " "; else { out << endl; }
	}
	
	}
	return -1;
}
