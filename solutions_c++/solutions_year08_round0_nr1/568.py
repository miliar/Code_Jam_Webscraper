#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;


int N;

char endline[128];

string readString(){
	char str[128];
	scanf("%[^\n]s",str);
	//printf("%s.\n",str);
	scanf("\n");
	return str;
}

int main(){

	int d;
	scanf("%d",&d);
	for (int testCase=1; testCase<=d; ++testCase){
		scanf("%d",&N); scanf("\n");
		map< string, int > Tmap;
		for (int i=0; i<N; ++i){
			Tmap[readString()]=i;
		}


		int result=0;
		vector<bool> vis(N,false);
		int visited=0;
		
		int M;
		scanf("%d",&M); scanf("\n");
		while (M--){
			int t=Tmap[readString()];
			if (t>=0 && !vis[t]){
				vis[t] = true;
				++visited;
			}
			if (visited==N){
				++result;
				visited=1;
				vis.assign(N,false);
				vis[t] = true;
			}
		}
 		printf("Case #%d: %d\n",testCase,result);
	}

	return 0;
}

