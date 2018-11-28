#include <vector>
#include <iostream>

using namespace std;

int main(){
	int cases, row, col;
	char temp;
	bool pos;
	vector <vector <char> > grid;
	cin>>cases;
	for (int a=1; a<=cases; a++){
		pos = true;
		cin>>row>>col;
		for (int i=0; i< row; i++){
			grid.push_back(vector <char> (col));
			for (int j=0; j<col; j++){
				cin>>temp;
				grid[i][j]=temp;;
			}
		}
		for (int i=0; i<row; i++){
			for (int j=0; j<col; j++){
				if (grid[i][j]=='#')
					if (i+1 < row && j+1 <col && grid[i+1][j] == '#' && grid [i][j+1]== '#' && grid [i+1][j+1]== '#'){
						grid[i][j]='/';
						grid[i][j+1]=92;
						grid[i+1][j]=92;
						grid[i+1][j+1]='/';
					}
					else{
						pos=false;
						break;
					}
			}
		}
		cout<<"Case #"<<a<<":"<<endl;
		if (pos)
			for (int i=0; i<row; i++){
				for (int j=0; j<col; j++)
					cout<<grid[i][j];
				cout<<endl;
			}
		else
			cout<<"Impossible"<<endl;
		grid.clear();
	}
	return 0;
}

