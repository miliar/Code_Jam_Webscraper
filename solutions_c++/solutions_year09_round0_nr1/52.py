#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

string word,pat;
vector<string> words;
int len,d,n;

int main() {
    ifstream fin("A-large.in");
    FILE *fout=fopen("A-large.out","w");
    fin >> len >> d >> n;
    for (int i=0;i<d;i++) {
    	fin >> word;
    	words.push_back(word);
    }
    for (int i=1;i<=n;i++) {
    	fin >> pat;
    	int st=0;
    	for (int j=0;j<words.size();j++) {
    		int match=1, j2=0;
    		for (int k=0;k<pat.size();k++,j2++) {
    			int ok=0;
    			if (pat[k]=='(') {
    				k++;
    				while (pat[k]!=')') {
    					if (pat[k]==words[j][j2]) ok=1;
    					k++;
    				}
    			} else {
    				if (pat[k]==words[j][j2]) ok=1;
    			}
    			if (!ok) match=0;
    		}
    		st+=match;
    	}
    	fprintf(fout,"Case #%d: %d\n",i,st);
    }
    return 0;
}
