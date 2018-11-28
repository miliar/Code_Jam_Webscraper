#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <utility>
#include <map>
#include <climits>

#define vi vector<int>
#define vii vi::iterator
#define pii pair<int,int>
#define vpi vector< pii >
#define vpii vpi::iterator

#define FOR(i,n) for (int i=0;i<n;i++)
#define FORIT(it,t,n) for (t::iterator it=n.begin();it!=n.end();it++)

#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a) ((a)<0?-(a):(a))
#define DIFF(a,b) MAX((a)-(b),(b)-(a))
#define BETWEEN(x,a,b) ((x)>=(a) && (x)<=(b))


using namespace std;

int main(int argc,char **argv)
{   
    if (argc!=3)
    {
      printf("usage: program-name inputfile outputfile\n");
      exit(1);
    }
    
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    int T,Case;
    
    fin >> T;
    
    for (Case=1;Case<=T;Case++)
    {
		int r,c;
		fin >> r >> c;
		vector< vector< char > > pic(r);
		FOR(i,r) pic[i].resize(c);
		
		FOR(i,r) FOR(j,c){
			fin >> pic[i][j];
		}
		
		bool works=true;
		
		FOR(i,r) FOR(j,c){
			if (pic[i][j]=='#'){
				if (i+1<r && j+1<c && pic[i+1][j]=='#' && pic[i][j+1]=='#' && pic[i+1][j+1]=='#'){
					pic[i][j]=pic[i+1][j+1]='/';
					pic[i+1][j]=pic[i][j+1]='\\';
				}else{
					works=false;
					break;
				}
			}
			if (!works) break;
		}
		
        fout << "Case #" << Case << ":\n";
		
		if (works){
			FOR(i,r) {
				FOR(j,c){
					fout << pic[i][j];
				}
				fout << "\n";
			}
		}else{
			fout << "Impossible\n";
		}
    }
	fin.close();
    fout.close();
}
