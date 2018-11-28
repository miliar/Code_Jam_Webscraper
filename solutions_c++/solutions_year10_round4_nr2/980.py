#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int M[2000];
char f[10000];

int main() {
	int T,P,lulz,buy,buyo,done,aux,it,c;
	cin >> T;
	for(int cs=1;cs<=T;cs++) {
		buyo=0; buy=0;
		cin >> P;
		for(int i=0;i< (1<<P);i++) {
			cin >> M[i];
		}
		getchar();
		for(int i=0; i<P; i++) {
				c=' ';
				while(c!='\n' && c!=EOF)
					c=getchar();
		}
		done=0;
		for(int i=0; i<P && !done; i++) {
			it=0;
			for(int j=0; j< (1<<i); j++) {
				aux=P;
				for(int k=0; k< (1<<(P-i)); k++) {
					aux=min(aux,M[it]);
					it++;
				}
				if(aux < P) {
					it-=(1<<(P-i));
					for(int k=0;k < (1<<(P-i));k++) {
						M[it]++;
						it++;
					}
					buy++;
				}
			}
			if(buyo == buy)
				done=1;
			buyo = buy;
		}		
		cout << "Case #" << cs << ": " <<  buy  << '\n';
	}
	return 0;
}
