#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <sstream>
#include <set>
using namespace std;
int main(){
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int t, c, d, n;
	string s, str, cad;
	
	scanf("%d\n", &t);
	for( int ii=1;ii<=t;ii++ ){
		getline(cin, s);
		istringstream ent(s);
		ent>>c;
		vector<string> combine, opossed;
		for( int i=0;i<c;i++ ){
			ent>>str;
			combine.push_back(str);
		}
		ent>>d;
		for( int i=0;i<d;i++ ){
			ent>>str;
			opossed.push_back(str);
		}
		ent>>n>>cad;
		string sol="";
		for( int i=0;i<n;i++ ){
			int band=1;
			if( sol.length()>0 ){
				for( int j=0;j<combine.size();j++ ){
					if( combine[j][0]==sol[sol.length()-1] && combine[j][1]==cad[i] ){
						band=0;
						sol.erase(sol.length()-1,1);
						sol+=combine[j][2];
					}
					if( combine[j][1]==sol[sol.length()-1] && combine[j][0]==cad[i] ){
						band=0;
						sol.erase(sol.length()-1,1);
						sol+=combine[j][2];
					}
				}	
			}
			if( sol.length()>0 && band ){
				for( int j=0;j<sol.length();j++ ){
					for( int k=0;k<opossed.size();k++ ){
						if( opossed[k][0]==sol[j] && opossed[k][1]==cad[i] ){
							sol="";band=0;
						}
						if( opossed[k][1]==sol[j] && opossed[k][0]==cad[i] ){
							sol="";band=0;
						}
					}	
				}
			}
			if( band ) sol+=cad[i];
		}
		printf("Case #%d: ", ii);
		putchar('[');
		for( int i=0;i<sol.length();i++ ){
			if( i ) printf(", ");
			printf("%c", sol[i]);
		}
		putchar(']');
		putchar('\n');
	}
	return 0;
}









