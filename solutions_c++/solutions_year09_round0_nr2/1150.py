#include <stdio.h>
#include "stdafx.h"
#include <stdlib.h>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct _rankinfo {
	int H;
	int W;
	int value;
} rankinfo;

int T,H,W;
vector<vector<int> > flow;
vector<vector<int> > mp;
vector<int> line;
vector<int> zerovector;
vector<rankinfo> rank;
rankinfo raw;

bool comp(const rankinfo &a, const rankinfo &b)
{
	if (a.value < b.value)
		return true;

	if (a.value > b.value)
		return false;

	if (a.H < b.H)
		return true;

	if (a.H > b.H)
		return false;

	if (a.W < b.W)
		return true;

	return false;
}

int getAltitudes(int h, int w) 
{
	if (h < 0 || h >= H)
		return 10001;

	if (w < 0 || w >= W)
		return 10001;

	return flow[h][w];
}

int main()
{


	FILE *fin = fopen("D:\\b.in", "r");
	FILE *fout = fopen("D:\\b.txt", "w");


	fscanf(fin, "%d", &T);

	for (int cs = 1; cs <= T; cs++)
	{
		mp.clear();
		flow.clear();
		line.clear();
		rank.clear();
		zerovector.clear();

		fscanf(fin, "%d%d", &H, &W);
		
		for (int w = 0; w < W; w++)
			zerovector.push_back(0);

		for (int h = 0; h < H; h++)
		{
			mp.push_back(zerovector);
			line.clear();
			for (int w = 0; w < W; w++)
			{
				int value;
				fscanf(fin, "%d", &value);
				line.push_back(value);
				raw.H = h;
				raw.W = w;
				raw.value = value;
				rank.push_back(raw);
			}
			flow.push_back(line);
		}

		sort(rank.begin(), rank.end(), comp);
		int seqnum = 0;

		for (vector<rankinfo>::iterator itr = rank.begin(); itr != rank.end(); ++itr)
		{
			int seq = -1;

			int w = itr->W;
			int h = itr->H;
			int value = itr->value;
			int North = getAltitudes(h-1, w);
			if (North < value)
			{
				value = North;
				seq = mp[h-1][w];
			}

			int West = getAltitudes(h, w-1);
			if (West < value)
			{
				value = West;
				seq = mp[h][w-1];
			}

			int East = getAltitudes(h, w+1);
			if (East < value)
			{
				value = East;
				seq = mp[h][w+1];
			}

			int South = getAltitudes(h+1, w);
			if (South < value)
			{
				value = South;
				seq = mp[h+1][w];
			}
			
			if (seq == -1)
			{
				++seqnum;
				seq = seqnum;
			}

			mp[h][w] = seq;
		}
		
		map<int, char> hash;
		hash.clear();
		char ch = 'a';

		for (int h = 0; h < H; h++)
			for (int w = 0; w < W; w++)
			{
				if (hash.find(mp[h][w]) == hash.end())
				{
					hash[mp[h][w]] = ch;
					mp[h][w] = ch;
					ch++;
				}
				else
					mp[h][w] = hash[mp[h][w]];
			}

		fprintf(fout, "Case #%d:\n", cs);
		for (int h = 0; h < H; h++)
		{
			fprintf(fout, "%c", mp[h][0]);
			for (int w = 1; w < W; w++)
			fprintf(fout, " %c", mp[h][w]);
			fprintf(fout, "\n");
		}
	}

	return 0;
}






		



