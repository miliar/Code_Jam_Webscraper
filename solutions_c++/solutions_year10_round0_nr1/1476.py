#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
using namespace std;


int main(int argc,char **argv)
{
	int CASES;
	cin >> CASES;
	for(int cn=1;cn<=CASES;++cn)
	{
		int N,K;
		cin >> N >> K;
		int G = (1<<N)-1;
		K &= G;
		printf("Case #%d: %s\n",cn,((K==G)?"ON":"OFF") );
	}
	return 0;
};
