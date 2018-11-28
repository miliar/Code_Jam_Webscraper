// g++ -O3 -o minsearch minsearch.cpp
// Bertrand Nouvel Google Jam Qualif 2008


#include <ext/hash_map>
#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;
using namespace __gnu_cxx;


// max name of search engines
#define MAX_LEN 65536

// max number of changes
#define BOOM 0x6FFFFFFF;

int T,S;

struct eqstr
{
  bool operator()(const char* s1, const char* s2) const
  {
    return strcmp(s1, s2) == 0;
  }
};

hash_map<const char*, int, hash<const char*>, eqstr> searchengines;

int * cursearchengines_cpath;
int cursearchengines_cpathmin;

int get_next_e(int & E) {
	hash_map<const char*, int, hash<const char*>, eqstr>::iterator it;
	static char x[MAX_LEN+1];
	if (E==0) {
		//printf("Strange !!!\n",it->first);
		return -1;
	}
	if (!(fgets(x,MAX_LEN,stdin ))) 
		return -1;
	E--;
	while ((it=searchengines.find(x))==searchengines.end()) {
		if (E==0)
			return -1;
		if (!(fgets(x,MAX_LEN,stdin))) return -1;
		E--;
	}
	//printf("%s\n",it->first);
	// ok we have a search engine we just get its number no...
	return (*(((int *)(void *)it->first)-1));  
}

void minsearch() {
	int e;
	int E;
	scanf("%d\n",&E);
	while ((e=get_next_e(E))!=-1) {
		// check if we change to some search engine may be better than current result of these search engines
		// then update
		//printf("%d\n",e);
		for (int s=0; s<S;s++) {
			if (cursearchengines_cpath[s]>(cursearchengines_cpath[e]+1)) {
				cursearchengines_cpath[s]=cursearchengines_cpath[e]+1;
				//printf("%d=>%d\n",s, cursearchengines_cpath[e]+1);
			}
		}
		cursearchengines_cpath[e]=BOOM;
	}
}

int main(int argc, char ** argv) {
	scanf("%d\n",&T);

	
	for (int t=0; t<T;t++) {
		scanf("%d\n",&S);
		//printf("%d\n",S);
		searchengines.clear();
		for (int s=0; s<S;s++) {
			char * st = new char [MAX_LEN+sizeof(int)+1]; 
			(*((int*)(void *)st))=s;
			fgets(st+sizeof(int),MAX_LEN,stdin);
			//printf("%d,%s\n",s,st+sizeof(int));
			searchengines[st+sizeof(int)]=1;
		}

		cursearchengines_cpath=new int[S];

		for (int s=0; s<S;s++) {
			cursearchengines_cpath[s]=0;
		}
		
		minsearch(); 
	

		cursearchengines_cpathmin=cursearchengines_cpath[0];
		for (int s=0; s<S;s++) {
			if (cursearchengines_cpath[s]<cursearchengines_cpathmin) {
				cursearchengines_cpathmin=cursearchengines_cpath[s];
			}
		}
		std::cout << "Case #"<< (t+1) << ": " << cursearchengines_cpathmin << "\n";

		delete [] cursearchengines_cpath;
	}
	

	
	// TODO: to be clean, clean the memory

	return 0;
}
