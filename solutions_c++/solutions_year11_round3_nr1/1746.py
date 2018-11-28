#include <iostream>
using namespace std;

int map[51][51];
bool check(int i,int j)
{
	if ((map[i][j])&&(map[i+1][j])&&(map[i][j+1])&&(map[i+1][j+1])){
		map[i][j]=2;
		map[i+1][j]=3;
		map[i][j+1]=3;
		map[i+1][j+1]=2;
		return true;	
	}
	else
	return false;
}
int main(){
	int n,r,c;
	char cz;
	cin >> n;
	for (int casei=1;casei<=n;casei++){
	
	
	for (int i=0;i<51;i++)
		for (int j=0;j<51;j++){
			map[i][j]=0;
		}
	cin >> r >> c;
	for (int i=0;i<r;i++)
		for (int j=0;j<c;j++){
			cin >> cz;
			map[i][j]=(cz=='#');
		}
	bool flag=true;
	for (int i=0;i<r;i++)
		for (int j=0;j<c;j++)
			if (map[i][j]==1)
				if (check(i,j)==false){
					flag=false;
					break;
				}
	cout << "Case #"<<casei<<':'<<endl;
	if (flag){
		for (int i=0;i<r;i++){
			for (int j=0;j<c;j++)
				if (map[i][j]==0)
					cout <<'.';
				else if (map[i][j]==2)
					cout <<'/';
				else
					cout <<'\\';
			cout <<endl;
			}
	}
	else
		cout << "Impossible" << endl;
}
	return 0;
}



