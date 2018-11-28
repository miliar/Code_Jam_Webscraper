//
// Author:	G2 (Jit Ray Chowdhury)
//jit.ray.c@gmail.com
// Created on Sept 13, 2009
//For Google Code Jam
//Round 1C
//problem A

#include <stdlib.h>
#include <iomanip>

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <cmath>

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
#define FORA(i,c) REP(i,size(c))
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))
using namespace std;
typedef unsigned long long LL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef vector<string> VS;

LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
//
//
//

LL R,pw;
string tmp;
char word[65],word2[65];

int main(int argc, char** argv) {
        ifstream fin("input.txt");
	ofstream fout("output.txt");

	int i,j,k,CN,L,l,l2,D,d ,cn,ascii[255],nxt=-1;

        //cout<<sizeof(R);
        fin >> CN;
         
	for (cn = 1; cn <= CN; ++cn) {
            R=0;
		fin>>word;
                cout<<word;
                for(i=0;i<255;i++)ascii[i]=-1;
                L=strlen(word);
                nxt=-1;
                for(l=0;l<L;l++)
                {
                if(ascii[word[l]]==-1)
                    {
                    
                    if(nxt>1)nxt++;
                    else if(nxt==-1)nxt=1;
                    else if(nxt==1)nxt=0;
                    else if(nxt==0)nxt=2;
                    ascii[word[l]]=nxt;
                    }
                word2[l]='0'+ascii[word[l]];
                }
                word2[l]=0;
                if(nxt<2)nxt=2;
                else nxt++;
                pw=1;R=0;
                 for(l=L-1;l>=0;l--)
                {
                     R+=pw*(word2[l]-'0');
                     pw*=nxt;
                 }
               // cout<<"base is "<<nxt<<" word is "<<word2;
                
		//debug output
                
		cout << "Case #" << cn << ": " << R<< '\n';
		//final output
                
		fout << "Case #" << cn << ": " <<R<< '\n';
	}
	//system("pause");
    return (EXIT_SUCCESS);
}

