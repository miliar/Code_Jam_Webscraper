#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>

using namespace std;

int main(  )
{
	int otime, btime, olast, blast, time;	
	int T,N;
	scanf("%d", &T);	
	
	for(int j = 0; j<T; ++j){
		scanf("%d", &N);
		otime = 0;	olast = 1;
		btime = 0;	blast = 1;
		time = 0;
		
		for(int i = 0; i<N; ++i){
			char c;
			int x, reachtime = 0;
			cin >> c >> x;
			if(c == 'O'){
				reachtime = abs(x-olast) - (time - otime);
				olast = x;
				if ( reachtime > 0 )	time = time+reachtime;
				time++;
				otime = time;
			} else {
				reachtime = abs(x-blast) - (time - btime);
				blast = x;
				if ( reachtime > 0 )	time = time+reachtime;
				time++;
				btime = time;
			}
		}

		cout << "Case #"<<j+1 << ": " <<  time << endl;
	}
	return 0;
}
