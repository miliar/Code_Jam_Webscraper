#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <algorithm>
#include <string>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <ctime>
#include <cmath>
#include <numeric>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define REP(i,b) For(i,1,b)

int main(int argc, char* argv[])
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int NumTest;
	scanf("%d", &NumTest);

	For(iTest, 1, NumTest){
		int N,M;
		scanf("%d %d\n",&N,&M);
		set<string> allPaths;
		string currDir;
		For(iDir,1,N){
			cin>>currDir;
			allPaths.insert(currDir);
			int i=1;
			while(i<currDir.length()){
				string temp;
				if(currDir[i]=='/'){
					temp.assign(currDir,0,i);
					allPaths.insert(temp);
				}
				i++;
			}
		}
		int64 numTotal = 0;
		For(jDir,1,M){
			cin>>currDir;
			int i=1;
			set<string>::iterator findit;
			findit=allPaths.find(currDir);
			if(findit==allPaths.end()){
				numTotal++;
				allPaths.insert(currDir);
			}
			while(i<currDir.length()){
				string temp;
				if(currDir[i]=='/'){
					temp.assign(currDir,0,i);
					findit=allPaths.find(temp);
					if(findit==allPaths.end()){
						numTotal++;
						allPaths.insert(temp);
					}
				}
				i++;
			}
		}
		printf("Case #%d: %lld\n", iTest,numTotal);
	}
}