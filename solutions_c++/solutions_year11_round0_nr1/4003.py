
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctype.h>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define pb push_back
#define sz size()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORALL(i,x) for(int i=0;i<x.size();i++)
#define FORALLR(i,x) for(int i=x.size()-1;i>=0;i--)
#define SWAP(x,y) (x)+=(y);y=(x)-(y);x=(x)-(y);
#define lint long long
#define MAX 1000
#define INF 1<<30

typedef vector<int> vi;
typedef vector<string> vs;

int cases,caseno;

int input(){
	return 1; 
}
void process(){
    int tasks;
	int preO = 1 , preB = 1,move;
	int moveO = 0, moveB = 0, btn;
	char bot;
	int totalMove = 0;
	cin >> tasks;
	while( tasks-- ){
		cin >> bot;
		cin >> btn;
		if( bot == 'O' ){
			move = abs( btn - preO );
			if( move > moveB ){
				totalMove += move + 1 - moveB;
				moveO += move + 1 - moveB;
			}else{
				totalMove++;
				moveO++;
			}
			moveB = 0;
			preO = btn;
		}else if( bot == 'B'){
			move = abs( btn - preB );
			if( move > moveO ){
				totalMove += move + 1 - moveO;
				moveB += move + 1 - moveO;
			}else{
				totalMove++;
				moveB++;
			}
			moveO = 0;
			preB = btn;
		}
	}

	cout<<"Case #"<<(++caseno)<<": " << totalMove << endl;

}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cases;
	while(cases--){
		input();
		process();
	}
}
