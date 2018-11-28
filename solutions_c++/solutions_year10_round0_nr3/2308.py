#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <vector>
#include <map>

#define INF 2000000000
#define mp make_pair

using namespace std;

int cases, r, k, n;
int temp;
int counter = 1;
queue<int> line;

bool read(){
	if(!cases--) return false;
	scanf("%d%d%d", &r, &k, &n);
	
	while(!line.empty()) line.pop();
	
	for(int i = 0; i < n; i++){
		scanf("%d", &temp);
		line.push(temp);
	}
	return true;
}

void process(){
	int profit = 0;
	queue<int> requeue;
	int riding;
	int pops = 0;
	int rides = 0;
	
	while(r--){
		riding = 0;
		rides++;
		while(!line.empty() && riding + line.front() <= k){
			riding += line.front();
			requeue.push(line.front());
			line.pop();
			pops++;			
		}
		profit += riding;
		while(!requeue.empty()){
			line.push(requeue.front());
			requeue.pop();
		}
		
		if(pops != 0 && pops%n == 0){	
			profit += profit*(r/rides);
			r %= rides;
		}
	}
	
	printf("Case #%d: %d\n", counter++, profit);
}

int main(){

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d", &cases);
	
	while(read()){		
		process();
	}
	
	return 0;
}
