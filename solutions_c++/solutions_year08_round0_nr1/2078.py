#include < iostream >
#include < string >
#include < fstream >
using namespace std;
ifstream inFile;
ofstream outFile;
char en[1000];
string eng[1000], que;
int p, n, s, q, b[10000], sum, t;
bool e[1000];

int main(){
	inFile.open("input.dat",ios::in);
	outFile.open("output.dat",ios::out);
    inFile >> n;
	for( int i = 1; i <= n; i ++ ){
		t = 0;
		inFile >> s;
		inFile.getline(en,100);
		//outFile << n << endl << s << endl;
		for( int j = 1; j <= s; j ++ ){
			inFile.getline(en,100);
			eng[j] = en;
			//outFile << eng[j] << endl;
			e[ j ] = false;
		}
        sum = 0;
		inFile >> q;
		inFile.getline(en,100);
		for( int j = 1; j <= q; j ++ ){
			inFile.getline(en, 100);
			que = en;
			for( int k = 1; k <= s; k ++ ){ 
			    if( que == eng[ k ] ){
					if( e[ k ] == false ){
				        e[ k ] = true;  sum ++;
						p = k;
					    break;
					}
				}
			}
			if( sum == s ){
				t++;
				for( int k = 1; k <= s; k ++ ) e[ k ] = false;
				e[ p ] = true;
				sum = 1;
			}
		}
		outFile << "Case #" << i << ": " << t << endl;

	}
	inFile.close();
	outFile.close();

	return 0;
}