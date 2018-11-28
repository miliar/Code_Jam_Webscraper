
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int sortFunction( const void *a, const void *b)
{
   const char** astr = (const char**)a;
   const char** bstr = (const char**)b;
   //cout<<*astr<<" "<<*bstr<<"\n";
   return strcmp(*astr, *bstr);
}

vector<int> findwordindices(char c, char **words, vector<int> indices, int l)
{
	vector<int> ninds;
	int n = indices.size();
	for(int i = 0; i < n; i++) {
		int x = indices[i]; 
		//cout<<consider<<" "<<x<<" "<<l<<" "<<c<<" "<<words[x][l]<<endl;
		if(words[x][l] == c) {
			ninds.push_back(x);
			//cout<<"inserted "<<x<<endl;
		}
	}
	//sort(indexes.begin(), indexes.end());
	//cout<<"ninds for "<<c<<indexes.size()<<endl;		
	return ninds;	
		
}
int main(int argc, char** argv)
{
	//read N
	int L, D, N; 
	cin>>L>>D>>N;
	//cout<<L<<D<<N;
	//read lines
	char **words = new char*[D];
	int i = 0;
	vector<int> indices; 
	while(D-- > 0) {
		words[i] = new char[L+1];
		memset(words[i], 0, L+1);
		cin>>words[i];	
		//cout<<words[i]<<"\n";
		indices.push_back(i);
		i++;
	}
	qsort(words, i, sizeof(char*), sortFunction);
	int x = 0;
	vector<int> exinds = indices;
	while(x++ != N) {
		string patternstr;
		cin>>patternstr;
		
		const char* pattern = patternstr.c_str();
		//cout<<pattern;
		int pi = 0;
		D = i;
		
		indices = exinds;
		for(int i = 0 ; i < L; i++) {
			if(pattern[pi] == '(') {
				vector<int> cinds;
				while(pattern[++pi] != ')') {
					vector<int> pinds = findwordindices(pattern[pi], words, indices, i);
					int pl = pinds.size();
					for(int p = 0; p < pl; p++) {
						cinds.push_back(pinds[p]);
					}
				}
				indices = cinds;
			} else {
				indices = findwordindices(pattern[pi], words, indices, i);
				//cout<<indices.size()<<endl;
			}
			pi++;
			sort(indices.begin(), indices.end());
		}
		cout<<"Case #"<<x<<": "<<indices.size()<<"\n";
		//delete[] pattern;
	}
	while(D-- > 0) {
		delete[] words[D];
	}
	delete[] words;
	return  0;
	
}
