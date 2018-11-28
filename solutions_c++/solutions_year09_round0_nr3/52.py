#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int t;
string s;
string p="welcome to code jam";
int f[600][100];
char ch;

int main() {
    ifstream fin("C-large.in");
    FILE *fout=fopen("C-large.out","w");
    fin >> t;
    getline(fin,s);

    for (int test=1;test<=t;test++) {
    	printf("%d/%d\r",test,t);
    	getline(fin,s);
    	for (int j=0;j<p.size();j++) {
    		if (p[j]==s[0] && j==0) f[0][j]=1; else f[0][j]=0; //i==0
    		for (int i=1;i<s.size();i++) {
    			f[i][j]=f[i-1][j];
    			if (p[j]==s[i]) {
    				if (j==0) {
    					f[i][j]+=1;
    				} else {
						f[i][j]+=f[i-1][j-1];
    				}
    			}
    			f[i][j]%=10000;
    		}
    	}
    	fprintf(fout,"Case #%d: %04d\n",test,f[s.size()-1][p.size()-1]);
    }
    return 0;
}
