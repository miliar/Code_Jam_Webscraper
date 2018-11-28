#include <iostream>

using namespace std;

int main(int argc, char ** argv){

int T, k, R, C, i ,j;

cin >> T;

bool possible;
char painting[50][50];

for(k=1;k<=T;k++){

cout << "Case #" << k <<":" << endl;
possible = true;
cin >> R >> C ;

for (i=0;i<R;i++)
	for(j=0;j<C;j++)
	cin >> painting[i][j];
	

for(i=0;i<R && possible == true ;i++)
	for(j=0;j<C && possible == true;j++)
		if(painting[i][j] == '#'){
			if(j+1<C && painting[i][j+1] == '#' &&
				i+1 < R && painting[i+1][j] == '#'
				&& painting[i+1][j+1] == '#'){
				painting[i][j]='/';
				painting[i][j+1]='\\';
				painting[i+1][j] = '\\';
				painting[i+1][j+1] = '/';

			}
			else { possible = false; cout<< "Impossible\n"; break;}
		}
if (possible)
		
for(i=0;i<R  ;i++){
	for(j=0;j<C ;j++)
		cout<<painting[i][j];
	cout<<endl; 
}

}


return 0;
}
