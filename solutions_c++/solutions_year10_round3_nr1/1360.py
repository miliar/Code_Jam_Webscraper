#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

typedef pair<int,int> corda;

int t, n, n1, n2;
vector<corda> lista;

static bool compareCorda(corda lhs, corda rhs){
	return(abs(lhs.first-lhs.second) < abs(rhs.first-rhs.second));

}


int main(){
	scanf("%d", &t);

	for(int i1=1; i1<=t; i1++){
		scanf("%d", &n);
		
		lista.clear();
		for(int i=1; i<=n; i++){
			scanf("%d %d", &n1, &n2);
			lista.push_back(make_pair(n1,n2));
		}

		sort(lista.begin(), lista.end(), compareCorda);

		int total=0;
		corda c1,c2;
		for(int i=0; i<n; i++){
			for(int j=0; j<i; j++){
				if((lista[i].first >= lista[j].first &&
				lista[i].second <= lista[j].second) ||
 				(lista[i].first <= lista[j].first &&
				lista[i].second >= lista[j].second))
				total++;
			}			
		}

		printf("Case #%d: %d\n", i1, total);				
	}	

	return(0);
}
