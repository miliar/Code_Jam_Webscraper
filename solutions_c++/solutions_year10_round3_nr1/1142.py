#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

int main(){
	int T, N;
	freopen("c:\\jam\\A-small-attempt0.in", "r",stdin);
	scanf ("%d", &T);
int case =1;
	while(T--){
		
		scanf("%d", &N);
		int A[N], B[N];
		for (int i=0; i<N; i++)	scanf("%d%d", &A[i], &B[i]);
		int count =0;
		for (int i=0; i<N-1; i++){
			for (int j=i+1; j<N; j++){
				if (A[i]>A[j]&&B[i]<B[j]) count++;
				else if(A[i]<A[j]&&B[i]>B[j]) count++;
			}
		}
		cout << "Case #"<< case<<": "<<count<<endl;
C++;
}
	
	

}
