// Bertrand Nouvel Google Jam 2008

#include <ext/hash_map>
#include <list>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <iostream>

using namespace std;
using namespace __gnu_cxx;

struct eqstr
{
  bool operator()(const char* s1, const char* s2) const
  {
    return strcmp(s1, s2) == 0;
  }
};

hash_map<const char*, int, hash<const char*>, eqstr> searchengines;
int T,S;


//

// max per key
// num key
// alphabet



int charfreq[1000]; // arbitrary limit but ok
int chardepth[1000]; // depth of key

// k (number of touch)
int P,K,L;

int find_most_frequent() {
	int m=0, fm;
	while (chardepth[m]!=-1) {
		m++;
	}
	fm=chardepth[m];
	for (int i=m;i<L;i++) {
		if (chardepth[i]==-1) {
			if (charfreq[i]>fm) {
				fm=charfreq[m=i];
			}
		}
	}
	return m;
}

void computekey_depths() {
	int bk;
	int cd;
	for (int i=0; i<L; i++) {
		bk=find_most_frequent();
		cd=(i/K);
		chardepth[bk]=(1+cd);
	}
}


int main(int argc, char ** argv) {
	int res;
	scanf("%d\n",&T);
	
	for (int t=0; t<T;t++) {
		scanf("%d %d %d\n",&P, &K, &L);
		
		for (int i=0; i<L; i++) {
			chardepth[i]=-1;	
			scanf("%d",charfreq+i);
		}

		computekey_depths();
		res=0;
		for (int i=0;i<L;i++) {
			res+=charfreq[i]*chardepth[i];
		}
		std::cout << "Case #"<< (t+1) << ": " << res << "\n";
	}
	

	

	return 0;
}
