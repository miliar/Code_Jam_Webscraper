#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int C;
	cin>>C;
	for(int test=1; test<=C; test++){
		int A,N,M; cin>>N>>M>>A;
		bool done=false;
		for(int x1=0; x1<=N; x1++)
			for(int x2=x1; x2<=N; x2++)
				for(int y1=0; y1<=M; y1++)
					for(int y2=0; y2<=M; y2++)
						if(abs(x1*y2-x2*y1)==A){
							done=true;
							printf("Case #%d: 0 0 %d %d %d %d\n", test, x1,y1,x2,y2);
							goto out;
						}
out:    if(!done)
			printf("Case #%d: IMPOSSIBLE\n", test);
	}
	return 0;
}
