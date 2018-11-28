#include <stdio.h>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <functional>
#include <iostream>
#include <sstream>
#include <ctime>
#include <fstream>
using namespace std;
struct point {
	long long x;
	long long y;
};
int main(int argc, char* argv[])
{
	if (argc != 2) return -1;

	ifstream inFile;
	inFile.open(argv[1]);
	if (!inFile) return 1;

	int num_of_test = 0;
	inFile>>num_of_test;

	vector<struct point> v1;
	vector<int> vr;
	map<pair<int, int>, int> pmap;
	for (int i=0; i<num_of_test; ++i) {
		// reading inputs
		int n, A, B, C, D, x0, y0, M;
		n=A=B=C=D=x0=y0=M=0;
		inFile>>n>>A>>B>>C>>D>>x0>>y0>>M;

		// generate x, y
		struct point temp;
		temp.x=x0;
		temp.y=y0;
		//cout<<"x: "<<temp.x<<", y:"<<temp.y<<endl;
		v1.push_back(temp);
		for (int i=1; i<n; ++i)
		{
			temp.x=(A * temp.x + B) % M;
			temp.y=(C * temp.y + D) % M;
			//cout<<"x: "<<temp.x<<", y:"<<temp.y<<endl;
			v1.push_back(temp);
		}
		//cout<<"======================="<<endl;
		// start to process
		int count=0;
        for (int a=0; a<n; ++a)
			for (int b=0; b<n; ++b)
				for (int c=0; c<n; ++c)
		{
			if ((v1[a].x==v1[b].x && v1[a].y==v1[b].y) || 
				 (v1[b].x==v1[c].x && v1[b].y==v1[c].y) || 
				 (v1[a].x==v1[c].x && v1[a].y==v1[c].y))
				continue;

			int t1=(v1[a].x + v1[b].x + v1[c].x) % 3;
			int t2=(v1[a].y + v1[b].y + v1[c].y) % 3;
			if (!(t1 || t2))
			{
				count++;
				int first = (v1[a].x + v1[b].x + v1[c].x) / 3;
				int second = (v1[a].y + v1[b].y + v1[c].y) / 3;
				pmap[make_pair(first, second)]=0;
			}
		}

		// save results
		//int count=pmap.size();
		vr.push_back(count/6);
		pmap.clear();
        v1.clear();
	} // end of tests loop
    
	ofstream outfile ("output.dat");
	for (int i=0;i<vr.size();++i)
		outfile<<"Case #"<<i+1<<": "<<vr[i]<<endl;

	return 0;
}

