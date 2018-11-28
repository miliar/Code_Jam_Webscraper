#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream IN("A-small-attempt0.in");
ofstream OUT("A-small-attempt0.out");

int main(){
   int NC;
   IN >> NC;
   for (int cas=1; cas<=NC; cas++){
		int pressed = 0;
		
		int P, K, L;
		IN >> P >> K >> L;
		
		vector <int> frec(L);
		
		for (int i = 0; i < L; i++) IN >> frec[i];
		
		int level = 1, j=1;
		vector <int>::iterator M;
		for (int i = 0; i < L; i++, j++) {
			M = max_element(frec.begin(), frec.end());
			pressed += (*M)*level;
			frec.erase(M);
			if (j==K) {
				j=0;
				level++;
			}
		}
   
   
       OUT << "Case #" << cas << ": " << pressed << endl;
   }
}
