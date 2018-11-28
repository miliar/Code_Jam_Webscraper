#define _AFXDLL

#include <stdio.h>
#include <afx.h>

#include "math.h"

#include <set>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>

using std::set;
using std::stringstream;
using std::fstream;
using std::cout;
using std::cin;

using std::vector;
using std::string;

using std::pair;
using std::map;

using std::sort;

#define maxlen 3

map<vector<string>, int> wordCount;
vector<int> totalCounts;
vector<string> queries;
int totalcount;

void Read(const string& filename)
{
	totalCounts.resize(maxlen + 1);
	fstream input(filename.c_str(), std::ios::in);

	int counter = 0;
	while (!input.eof())
	{
		if (counter % 100 == 0)
			cout << counter << std::endl;
		++counter;

		char str[10000];
		input.getline(str, 10000);
		queries.push_back(str);

		stringstream ss(str);

		vector<string> data;
		
		while (!ss.eof())
		{
			string s;
			ss >> s;

			data.push_back(s);
			if (data.size() > maxlen)
			{
				for (int i = 0; i < data.size() - 1; ++i)
					data[i] = data[i + 1];
				data.pop_back();
			}
			for (int i = 0; i < data.size(); ++i)
			{
				vector<string> tmpData(data.begin() + i, data.end());
				++wordCount[tmpData];
				++totalCounts[tmpData.size()];
				++totalcount;
			}
		}
	}
}

vector<pair<int, double> > bestAnswers;
double search(const vector<string>& source, int position)
{
	if (position >= source.size())
		return 1;
	if (bestAnswers[position].first != 0)
		return bestAnswers[position].second;

	string res = "";
	double max = 0;
	int bestMarker = 0;
	for (int i = 1; (i <= maxlen) && (i + position <= source.size()); ++i)
	{
		vector<string> curOtr (source.begin() + position, source.begin() + position + i);
		
		int count = wordCount[curOtr];
		if (count == 0)
			count = 1;
		int totalCount = totalCounts[i];

		double prob = (double)count / totalcount;
		double curMax = prob * search(source, position + i);
		if (curMax > max)
		{
			max = curMax;		
			bestMarker = i + position;
		}
	}
	bestAnswers[position].first = bestMarker;
	bestAnswers[position].second = max;
}

string SegmentQuery(const string& query)
{
	stringstream ss(query);
	vector<string> vQuery;

	while (!ss.eof())
	{
		string s;
		ss >> s;
		if (s != "")
			vQuery.push_back(s);
	}

	bestAnswers.clear();
	bestAnswers.resize(vQuery.size(), std::make_pair(0,0));
	search(vQuery, 0);

	vector<int> positions;
	positions.push_back(0);
	positions.push_back(bestAnswers[0].first);

	while ((positions[positions.size() - 1] != bestAnswers.size()) && (bestAnswers[positions[positions.size() - 1]].first != 0))
		positions.push_back(bestAnswers[positions[positions.size() - 1]].first);

	string ans;

	for (int i = 0; i < positions.size() - 1; ++i)
	{
		for (int j = positions[i]; j < positions[i + 1]; ++j)
			ans += vQuery[j] + " ";
		if (i != positions.size() - 2)
			ans += " | ";
	}
	/*
	for (int j = positions[positions.size() - 1]; j < vQuery.size() - 1; ++j)
		ans += vQuery[j] + " ";
	ans += vQuery[vQuery.size() - 1];*/
	return ans;		
}

typedef long long int64;

int64 pow(int64 n, int64 a)
{
	if (a == 0)
		return 1;
	if (a == 1)
		return n;

	int64 tmp = pow(n, a / 2);
	return tmp * tmp * pow(n, a % 2);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int64 num;
	cin >> num;
	for (int64 i = 0;i < num; ++i)
	{
		int64 n,k;
		cin >> n>>k;
		int64 power = pow(2,n);
		int64 res = (k + 1)%power;
		if (res == 0)
			cout << "Case #" << i + 1 << ": ON\n";
		else
			cout << "Case #" << i + 1 << ": OFF\n";
	}
	return 0;


	Read("2000queries2process.txt");
	cout << "Read: OK!" << std::endl;
	fstream output("queriessegment.txt", std::ios::out);
	for (int i = 0; i < queries.size(); ++i)
	{
		if (i % 100 == 0)
			cout << i << std::endl;
		output << SegmentQuery(queries[i]) << std::endl;
	}
	output.close();
	return 0;
}