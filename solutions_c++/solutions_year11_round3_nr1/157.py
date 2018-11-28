#include <iostream>
#include <cstdio>

using namespace std;

char pic[51][51];
int r,c;

bool replace(int cr, int cc){
	if (pic[cr][cc] == '#')
		pic[cr][cc] = '/';
	else
		return false;
	if (pic[cr+1][cc] == '#')
		pic[cr+1][cc] = '\\';
	else
		return false;
	if (pic[cr][cc+1] == '#')
		pic[cr][cc+1] = '\\';
	else
		return false;
	if (pic[cr+1][cc+1] == '#')
		pic[cr+1][cc+1] = '/';
	else
		return false;
	return true;
}

int main(){
	int tc, t;
	int i,j,k;
	bool can;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tc;
	for (t=0; t<tc; t++){
		cin >> r >> c;
		for (i=0; i<r; i++)
			cin >> pic[i];

		can = true;
		for (i=0; i<r; i++)
			for (j=0; j<c; j++)
				if (pic[i][j]=='#')
					if (!replace(i,j)){
						can = false;
						i=r+1;
						j=c+1;
					}

		printf("Case #%d:\n", t+1);
		if (can){
			for (i=0; i<r; i++){
				for (j=0; j<c; j++)
					cout << pic[i][j];
				cout << endl;
			}
		}else
			cout << "Impossible\n";



		/*for (i=0; i<r; i++){
			for (j=0; j<c; j++)
				cout << pic[i][j];
			cout << endl;
		}*/

	}
}