#include <cstdio>
#include <queue>
using namespace std;
#define MOD(x) (((x)>0)?(x):(-(x)))
int main()
{
	int T;
	scanf("%d",&T);
	
	for (int j = 0 ; j < T; j++)
 	{
		int N;
		scanf("%d ",&N);
		long long int currB = 1, currC = 1, totaltime = 0, currtimeB = 0,currTimeC = 0;
		for (int i = 1; i <= N;i++){
			char color;
			int button;
			scanf(" %c %d",&color,&button);
			//printf("color:%c button:%d\n",color,button);
			if (color == 'B') {
				int timeTaken = MOD(currB - button);
				if (totaltime >= timeTaken + currtimeB) {
					totaltime++;
				}
				else {
					totaltime = timeTaken + currtimeB+1;
				}
				currtimeB = totaltime;
				currB = button;
			}
			else {
                                int timeTaken = MOD(currC - button);
                                if (totaltime >= timeTaken + currTimeC) {
                                        totaltime++;
                                }
                                else {
                                        totaltime = timeTaken + currTimeC + 1;
                                }		
				currTimeC = totaltime;
				currC = button;		
			}
		}
		printf("Case #%d: %lld\n",j+1,totaltime);
		
	}
}
