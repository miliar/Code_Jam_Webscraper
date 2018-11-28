#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<list>
#include<cmath>
#include<cstring>
using namespace std;

int X, S, R, N;
int B, E, W;
long double wyn, T;
vector<int> predkosci;

int main(){
	int testy;
	scanf("%d", &testy);
	for(int t = 1; t <= testy; t++){
		predkosci.clear();
		scanf("%d %d %d %Lf %d", &X, &S, &R, &T, &N);
		for(int i = 0; i < N; i++){
			scanf("%d %d %d", &B, &E, &W);
			while(B<E){
				predkosci.push_back(W+S);
				B++;
			}
//			printf("%d %d ", W, W+S);
/*for(int i = 0; i < predkosci.size(); i++)
printf("%d ", predkosci[i]);
printf("\n");//*/
		}
		while(predkosci.size()<X)
			predkosci.push_back(S);
		sort(predkosci.begin(), predkosci.end());
		wyn = 0;
		for(int i = 0; i < X; i++){
			if(T>wyn+(long double)(1)/(predkosci[i]+R-S))
				wyn += (long double)(1)/(predkosci[i]+R-S);
			else if(T<=wyn)
				wyn += (long double)(1)/predkosci[i];
			else{
				long double j;
				for(j = 0.0; T>wyn+j/(predkosci[i]+R-S); j+=0.00000001);
				wyn += j/(predkosci[i]+R-S) + (1.0-j)/(predkosci[i]);
			}//*/
//printf("%d ", predkosci[i]);
		}
//printf("\n");
		printf("Case #%d: %.10Lf\n", t, wyn);
	}
	return 0;
}
