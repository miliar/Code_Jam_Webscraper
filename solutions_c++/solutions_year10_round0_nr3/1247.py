
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <stdlib.h>

using namespace std;

//Redirect input to the exe.

typedef struct grp{
		int count;
		long long size;
}group;

main(){
	int T = 0; cin >> T;

	for(int i=0; i<T; i++){
		long long answer = 0;
		long long R=0, k=0, N=0;cin >>R >> k >> N;
		queue<group> Q;
		for(int n=0; n<N; n++){
			group gr;	
			long long G=0; cin>>gr.size; gr.count=-1;
			Q.push(gr);
		}

		for(long long r=0; r<R; r++){
			long long kk = k;
			while(!Q.empty() && kk >= Q.front().size && Q.front().count != r){
				group first = Q.front();
				Q.pop();
				kk = kk - first.size;
				answer+=first.size;
				first.count = r;
				Q.push(first);
			}
		}

		cout << "Case #" << i+1 << ": " << (answer) << endl;
	}
}
