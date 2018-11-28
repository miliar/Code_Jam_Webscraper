
#include <malloc.h>
#include <iostream>
#include <fstream>
using namespace std;

//#define _SKY_DEBUG


struct group{
	int people;
	group* pNext;
};


static unsigned long long * result = 0;
static group* root = 0;
static int T = 0;


inline
void output(){
	///output
	ofstream f1("e:\\C-small-attempt0.out");
	if( !f1 ) return;

	for (int i = 0; i != T; i++){		
		f1 << "Case #" << i+1 << ": " << result[i] << endl;
	}

}


int main(){
	///get T
	ifstream fin("e:\\C-small-attempt0.in");
	fin >> T;
	int myCount = T;
	int retCount = 0;

	/// malloc out result
	if ( T >= 0 ){
		result = (unsigned long long *)malloc(T * sizeof(unsigned long long));
	}


	while( myCount != 0 ){
		
		unsigned long R = 0;
		unsigned long k = 0;
		unsigned long N = 0;
		
		///get R, k, N
		fin >> R;
		fin >> k;
		fin >> N;


		///initial chain
		struct group* lastGroup = root;
		for(int i = 0; i != N; i++){
			///get g(i)
#ifdef _SKY_DEBUG
			unsigned long g = i+1;
#else
			unsigned long g = 0;
			fin >> g;
#endif
			struct group* thisGroup = 
				(struct group* ) malloc ( sizeof(group) );
			if( !thisGroup) continue;
			thisGroup->people = g;
			thisGroup->pNext = 0;
			if(lastGroup == 0){
				root = thisGroup;
			}
			else{
				lastGroup->pNext = thisGroup;
			}
			lastGroup = thisGroup;
		}
		lastGroup->pNext = root; ///circle the chain
		
		unsigned long long total = 0;
		///calculate
		for( int i = 0; i != R; i++){
			int vacancy = k;
			struct group* go = root;
			for( int j = 0; j != N; j++){
				vacancy = vacancy - go->people;
				if( vacancy < 0 ){
					///this group can not board, next loop will start from this group
					root = go;
					break;
				}
				else{
					/// add money
					total += go->people;
				}
				go = go->pNext;
			}
		}
		///add this ret to result
		if ( result != 0 )
			result[retCount] = total;

		///free this loop
		struct group* go = root;
		struct group* before = root;
		for( int i = 0; i != N; i++){
			if( before != 0 ){
				go = before->pNext;
				free(before);
				before = 0;
			}
			before = go;
		}
		root = 0;

		myCount--;
		retCount++;
	
	}

	output();
	///free result
	if(result != NULL )
		free(result);

	return 0;
}