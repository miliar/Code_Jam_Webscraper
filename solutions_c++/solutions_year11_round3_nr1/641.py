#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
using namespace std;


//char grid[100][100];

bool makeSquare (vector<string> &rows, int rn, int cn){
	if(rn>=rows.size() || cn>=rows[0].size())
		return false;
	if(rows[rn][cn] == '/' || rows[rn][cn] == '\\')
		return true;
	if(rows[rn][cn] == '.')
		return true;
	/*if(rows[rn][cn] == '#' && (rn+1>=rows.size() || cn+1 >= rows[0].size()))
		return false;*/
	if(rows[rn][cn] == '#' || rows[rn][cn+1] == '#' || rows[rn+1][cn+1] == '#' || rows[rn+1][cn] == '#')
		if(rows[rn][cn] == '.' || rows[rn][cn+1] == '.' || rows[rn+1][cn+1] == '.' || rows[rn+1][cn] == '.')
			return false;

	if(rows[rn][cn] == '#' && rows[rn][cn+1] == '#' && rows[rn+1][cn+1] == '#' && rows[rn+1][cn] == '#'){
		rows[rn][cn] = '/';
		rows[rn][cn+1] = '\\';
		rows[rn+1][cn] = '\\';
		rows[rn+1][cn+1] = '/';
	}
	return true;
}

int main(int argc, char ** argv)
{
#ifdef KOMPA_NA_MISHO
	freopen ("in.txt","r",stdin);
#endif
	/////////////////////////////Code goes here:
	int T;
	cin>>T;
	for(int tt=1; tt<=T; tt++){
		
		int r,c;
		cin>>r>>c;
		vector<string> rows(r);
		for(int i=0; i<r; i++)
		{
			cin>>rows[i];
			rows[i].append(".");			
		}
		rows.push_back(string(c+1,'.'));
		bool possible = true;
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				if(!makeSquare(rows,i,j))
					possible = false;
			}
		}
		cout<<"Case #"<<tt<<":\n";
		if(possible){
			for(int i=0; i<r; i++){
				for(int j=0; j<c; j++)
					cout<<rows[i][j];
				cout<<endl;
			}
		}
		else
			cout<<"Impossible\n";
		
		
	}
	

	////////////////////////////////////////////
#ifdef KOMPA_NA_MISHO
	fclose (stdin);
#endif
	return 0;
}