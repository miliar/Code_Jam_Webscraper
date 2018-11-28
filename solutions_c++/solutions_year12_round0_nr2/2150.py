#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <set>
#include <queue>

using namespace std;

int main(){
	int i,j,k;
	int N, T, S, p;
	int t[200];
	int apartN;
	int max[200];
	priority_queue<pair<int, int> > apart, normal;
	set<int> numbers;
	scanf("%d\n",&T);
	for(int cases=0; cases<T; cases++){
		while(!apart.empty()){
			apart.pop();
		}
		while(!normal.empty()){
			normal.pop();
		}
		numbers.clear();
		scanf("%d %d %d\n",&N, &S, &p);
		for(i=0; i<N; i++){
			max[i] = -1;
		}
		for(i=0; i<N; i++){
			scanf("%d\n",&t[i]);
		}
		for(int l=0; l<N; l++){
			//printf("%d\n",t[l]);
			for(i=0; i<=10; i++){
				for(j=i; j<=10 && j<=i+2; j++){
					for(k=j; k<=10 && k<=i+2; k++){
						if(i+j+k == t[l]){
							//printf("\t%d %d %d",i,j,k);
							if(k-i==2){
								apart.push(make_pair(k,l));
								//printf("*\n");
							}else{
								//if(k>=p) printf("#");
								//printf("\n");
								if(max[l] < k)
									max[l] = k;
								normal.push(make_pair(k,l));
							}
						}
					}
				}
			}
		}
		apartN=0;
		k=0;
		while(apartN < S && !apart.empty()){
			if(!numbers.count(apart.top().second) && max[apart.top().second]<p){
				numbers.insert(apart.top().second);
				apartN++;
				if(apart.top().first >= p)
					k++;
			}
			apart.pop();
		}
		while(numbers.size()<N && !normal.empty()){
			if(!numbers.count(normal.top().second)){
				numbers.insert(normal.top().second);
				if(normal.top().first >= p)
					k++;
			}
			normal.pop();
		}
		printf("Case #%d: ",cases+1);
		//print solution
		printf("%d\n",k);
	}
	

}
