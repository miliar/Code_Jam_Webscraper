#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>


#define MAX 110
using namespace std;

int points[MAX];

int main() {

	int t, T, i, N, s, p, surprise, result, d;	
		
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d %d %d",&N,&s,&p);
		for(i=0; i<N; ++i)
			scanf("%d",&points[i]);

		for(i=0, result=0, surprise=0; i<N; ++i){
			switch(points[i]%3){
				case 0:	if(points[i]/3 >= p)
									result++;
								else if(points[i]!=0 && points[i]!= 30 && points[i]/3+1 >= p)
									surprise++;
								break;
				case 1:	if((points[i]+2)/3 >= p)
									result++;
								break;
				case 2:	if((points[i]+1)/3 >= p)
									result++;
								else if(points[i]!=29 && (points[i]+4)/3 >= p)
									surprise++;
								break;
			}
	/*		if(points[i]%3 == 1) {
				if((points[i]+2)/3 >= p)
					result++;
				if(d+1 >= p) {
					++result;
				}
			}
			else if(points[i]%3 == 2) {
				d = (points[i]-2)/3;
				if(d+1 >= p) {
					++result;
				}
				else if(d+2 >= p) {
					if(points[i]!=29)
						++surprise;
				}
			}
			else {
				d = points[i]/3;
				if(d >= p) {
					++result;
				}
				else if(d+1 >= p) {
					if(points[i]!= 30 && points[i]!= 0) {
						++surprise;
					}
				}
			}
	*/
		}
		if(surprise > s)
			result += s;
		else
			result += surprise;		
		printf("Case #%d: %d\n",t, result);
	}
	return 0;
}

