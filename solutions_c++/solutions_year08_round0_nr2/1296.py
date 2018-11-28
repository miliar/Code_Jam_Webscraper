#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <istream>
#include <fstream>
#include <cmath>
#include <map>
using namespace std;

vector<pair<int, int> > ab_a, ba_b, ab_b, ba_a;

bool cmp1(pair<int, int> a, pair<int, int> b)
{
	return a.first < b.first;
}

bool cmp2(pair<int, int> a, pair<int, int> b)
{
	return a.second < b.second;
}

int n, turnAround, na, nb;

int main()
{
	char temp;
	int hour, minute;
	int startT, endT;
	ifstream fin("input.in");  
	ofstream fout("results.txt", ios::app);
	int num;
	int res;
	int caseNum = 1;
	fin >> n;
	int aa, bb;
	while (n--)
	{
		aa = bb = 0;
		ab_a.clear();
		ba_b.clear();
		fin >> turnAround;
		fin >> na >> nb;
		for(int i = 0; i < na; i ++)
		{			
			fin >> hour >> temp >> minute;
			startT = hour*60+minute;
			fin >> hour >> temp >> minute;
			endT = hour*60+minute;
			ab_a.push_back(make_pair(startT, endT));
		}
		ab_b = ab_a;
//		cout << ab_a.size() << endl;
		sort(ab_a.begin(), ab_a.end(), cmp1);
		sort(ab_b.begin(), ab_b.end(), cmp2);
		for(int i = 0; i < nb; i ++)
		{			
			fin >> hour >> temp >> minute;
			startT = hour*60+minute;
			fin >> hour >> temp >> minute;
			endT = hour*60+minute;
			ba_b.push_back(make_pair(startT, endT));
		}
	   ba_a = ba_b;
//	   cout << ba_a.size() << endl;
	   
	   sort(ba_b.begin(), ba_b.end(), cmp1);
	   sort(ba_a.begin(), ba_a.end(), cmp2);
	   for(int i = 0, j = 0; i < na && j < nb;)
	   {
// 		   cout << ab_a[i].first << " " << ab_a[i].second << endl;
// 		   cout << ba_a[j].first << " " << ba_a[j].second << endl;
		   if(ba_a[j].second + turnAround > ab_a[i].first)
			   i++;
		   else
		   {
			   aa++;
			   i++;
			   j++;
		   }
	   }
	   for(int i = 0, j = 0; i < na && j < nb;)
	   {
		   if(ab_b[i].second + turnAround > ba_b[j].first)
			   j++;
		   else
		   {
			   bb++;
			   i++;
			   j++;
		   }
	   }
	   fout << "Case #" << caseNum << ": " << na-aa << " " << nb-bb << endl;
	   caseNum ++;

	}
	fin.close();
	fout.close();
	return 0;
}