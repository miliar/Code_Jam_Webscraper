#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}


int main(){
	int T;
	scanf("%d",&T);
	cin.ignore();
	for (int cs=1; cs<=T; cs++){
		int R, C;
		cin >>R >>C;
		char** tiles = new char* [R+1];
		for (int j=0; j<R; j++){
			tiles[j] = new char [C+1];
			cin >> tiles[j];	
		}
		
		for (int j=0; j<R; j++){
			//cout<<tiles[j]<<endl;
		}
		
		//cout<<"hi"<<endl;
		
		bool blue = false;
		bool red = true;
		
		for (int j=0; j<R; j++)
			for (int i=0; i<C; i++){
				if (tiles[j][i]=='#'){
					blue = true;
					if (i+1<C && j+1<R && tiles[j][i+1]=='#' && tiles[j+1][i]=='#' && tiles[j+1][i+1]=='#'){
						tiles[j][i]='/';
						tiles[j+1][i+1]='/';
						tiles[j][i+1] ='\\';
						tiles[j+1][i] = '\\';
					}
					else
						red = false;
				}
			}
		cout<<"Case #"<<cs<<":"<<endl;
		if ( blue && !red)
			cout<<"Impossible\n";
		else {
			for (int j=0; j<R; j++)
				{
					cout<<tiles[j]<<endl;
					
				}
		}
		for (int j=0; j<R; j++){
			delete [] tiles[j];
		}
		delete [] tiles;
		
	}
	return 0;
}
