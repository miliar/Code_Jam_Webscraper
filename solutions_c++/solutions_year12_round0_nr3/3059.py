#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;

//istream& fin = cin;
//ifstream fin ("C-sample.txt");
ifstream fin ("C-small-attempt0.in");
ofstream fout ("C-small-attempt0.out");
//ifstream fin ("C-large.in");
//ofstream fout ("C-large.out");
//ostream& fout = cout;

int main(){
	int t,a,b,rs;
	char buff[10], ab[10], bb[10];
	fin >> t;
	for(int i=1; i<=t; i++){
		fin >> a >> b;
		sprintf(ab,"%d",a);
 		sprintf(bb,"%d",b);
		rs = 0;
		for(int j=a; j<=b; j++){
			sprintf(buff,"%d",j);
			int len = strlen(buff);
			for(int k=1; k<len; k++){
				// no leading zero
				if(buff[k]=='0'){
					continue;
				}
				bool match = true;
				
				// greater than itself
				for(int l=0; l<len; l++){
					if(buff[(k+l)%len]==buff[l]){
						if(l==len-1){
							match = false;
						}
						continue;
					}
					match = (buff[(k+l)%len]>buff[l]);
					break;
				}
        if(!match){
					continue;
				}
				
				// greater than or equals to B
				for(int l=0; l<len; l++){
					if(buff[(k+l)%len]==bb[l]){
						continue;
					}
					match = (buff[(k+l)%len]<=bb[l]);
					break;
				}
				if(!match){
					continue;
				}
				
				// repeat pattern, e.g. 1212
				
				
				rs++;
			}
		}
		fout << "Case #" << i << ": " << rs << endl;
	}
	system("pause");
}
