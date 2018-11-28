
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include<fstream>
using namespace std;
struct node 
{
	int x,y;
};
int N;
int n;
//#define SMALL
#define LARGE
int main()
{
	
#ifdef SMALL
	
	ifstream infile("C:\\Users\\qingpingw\\Desktop\\A-small-attempt0.in");
	ofstream outfile("C:\\Users\\qingpingw\\Desktop\\A-small.out");
#endif
#ifdef LARGE
	ifstream infile("C:\\Users\\qingpingw\\Desktop\\A-large.in");
	ofstream outfile("C:\\Users\\qingpingw\\Desktop\\A-large.out");
#endif

	int i,j,k;
	int T;
	int count=0;
	infile>>T;
	for(i=1;i<=T;i++)
	{
		infile >> N;
		count=0;
		struct node num[1005];
		for( j=0;j<N;j++)
		{
			infile>>num[j].x>>num[j].y;
		}
		for( j=0;j<N;j++)
			for( k=j+1;k<N;k++)
				if((num[j].x<num[k].x && num[j].y>num[k].y)||(num[j].x>num[k].x && num[j].y<num[k].y))
					count++;
   
		outfile<<"Case #"<<i<<": ";
				outfile<<count<<endl;
	}
	system("pause");
	return 0;
}
