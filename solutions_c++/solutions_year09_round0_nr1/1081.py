#include <fstream>
#include <string>
#include <set>
#include <vector>

using namespace std;

int L, D, N;	//Length, worDs, the Number of test
string* words;
string aword;
class test{
public:
	set<char> token[15];
	int n;
	test() : n(0) {}
	test & operator ++() {
		n++;
		return *this;
	}
};
test* tests;
test* atest;

void in(){
	ifstream fin("A-large.in");
	
	fin >> L >> D >> N;
	int DD=D, NN=N;
	words = new string[DD]; tests = new test[NN];
	while(DD--) fin >> words[DD];
	while(NN--){
		fin >> aword;
		int it;			//in the word
		int start=0;	//0:) 1:(
		int i=0;		//token
		int mi=aword.size();
		char k;
		for(it=0; it<mi; ++it){
			k=aword.data()[it];
			if(k=='('){ start=1; }
			else if(k==')'){ start=0, i++; }
			else{
				tests[NN].token[i].insert(k);
				if(start==0) i++;
			}
		}
	
	}

	fin.close();

}

void proc(){
	int i, j, k;
	for(i=0; i<D; ++i){			//all words
		for(j=0; j<N; ++j){		//all tests
			atest=&tests[j];
			for(k=0; k<L; ++k){	//all letters
				if(atest->token[k].find(words[i].data()[k]) == atest->token[k].end()){	//no
					break;
				}
			}
			if(k==L){
				(*atest)++;
			}
		}
	}
}

void out(){
	ofstream fout("output.txt");
	int i;
	for(i=0; i<N; ++i){
		fout << "Case #" << i+1 << ": " << tests[N-i-1].n << endl;
	}
	fout.close();
	delete [] words; delete [] tests;
}

int main(void){
	in();
	proc();
	out();
	vector<int> a;
	
	return 0;
}


/*
int* a;
a=(int*)malloc(sizeof(int)*n);

a[0]
a[n-1];

free(a);
*/