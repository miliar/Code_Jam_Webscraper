// trains.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
int tat; //turnaround time
struct STrain
{
	int arr;
	int dep;
	bool used;
	STrain(int d, int a) {arr = a; dep = d; used = 0;};
};

int cmp_arr(STrain &t1, STrain &t2)
{
	return t1.arr<t2.arr;
};

int cmp_dep(STrain &t1, STrain &t2)
{
	return t1.dep<t2.dep;
};

bool can_be_used(STrain t1, STrain t2)
{
	return (!t1.used)&&(t1.arr<=t2.dep)&&(t2.dep - t1.arr >= tat);
}

int count(vector <STrain> from, vector<STrain> to)
{
	int res = 0;
	sort(from.begin(), from.end(), cmp_dep);
	sort(to.begin(), to.end(), cmp_arr);	
	vector<STrain>::iterator p, u;
	for(p = from.begin(); p != from.end(); p++)
	{
		u = find_first_of(to.begin(), to.end(), p, p+1, can_be_used);	
		if(u != to.end())
		{
			u->used = true;
		}
		else
		{
			res++;
		}
	}
	return res;
};


int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fi;
	FILE *fo;
	int n, na, nb;
	char c;
	fi = fopen("input.txt","r");
	fo = fopen("output.txt", "w");
	fscanf(fi, "%d", &n);
	for(int i = 0; i < n; i++)
	{
		vector <STrain> fromA;
	    vector <STrain> fromB;
		int deph, depmin, arrh, arrmin;
		int resa, resb;
		fscanf(fi, "%d", &tat);
		fscanf(fi, "%d %d", &na, &nb);
		for(int j = 0; j < na; j++)
		{
			fscanf(fi, "%d:%d %d:%d", &deph, &depmin, &arrh, &arrmin);
			fromA.push_back(STrain(deph*60+depmin, arrh*60+arrmin));
		}

		for(int j = 0; j < nb; j++)
		{
			fscanf(fi, "%d:%d %d:%d", &deph, &depmin, &arrh, &arrmin);
			fromB.push_back(STrain(deph*60+depmin, arrh*60+arrmin));
		}

		resa = count(fromA, fromB);
		resb = count(fromB, fromA);
		fprintf(fo, "Case #%d: %d %d\n", i+1, resa, resb);
	}
	fclose(fi);
	fclose(fo);
	return 0;
}

