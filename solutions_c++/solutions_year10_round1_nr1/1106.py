#include<vector>
#include<iostream>
#include<fstream>
using namespace std;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int ncases;
	fin>>ncases;
	for(int Case=1;Case<=ncases;Case++){
		fout<<"Case #"<<Case<<": ";
		int n,k;
		fin>>n>>k;
		vector<vector<char> > matrix(n,vector<char>(n,'.'));
		for(int i=0;i<n;i++){
			vector<char> tmp;
			for(int j=0;j<n;j++){
				char c;
				fin>>c;
				if(c!='.'){
					tmp.push_back(c);
				}
			}
			int row = n-1;
			for(vector<char>::reverse_iterator iter=tmp.rbegin();iter!=tmp.rend();iter++){	
					matrix[row][n-i-1] = *iter;
					row--;
			}
		}
		//fin>>matrix[j][n-i-1];

		//for(int col=0;col<n;col++){
		//	int empty = 0;
		//	int row = n-1;
		//	while(matrix[row][col] == '.'){
		//		row--;
		//		empty++;
		//	}
		//	if(empty==n)continue;
		//	row=n-1;
		//	for(int i=0;i<empty;i++){
		//		matrix[row][col]=matrix[row-empty][col];
		//		matrix[row-empty][col]='.';
		//		row--;
		//	}
		//}

		bool r=false,b=false;
		for(int i=0;i<n;i++){
			int countr = 0, countb=0;
			for(int j=0;j<n;j++){
				if(matrix[i][j] == 'R'){
					countr++;countb=0;
					if(countr >= k)
						r=true;
				}
				else if(matrix[i][j] == 'B'){
					countb++;countr=0;
					if(countb >= k)
						b=true;
				}
				else{
					countr = countb = 0;
				}
			}
		}

		for(int i=0;i<n;i++){
			int countr = 0, countb=0;
			for(int j=0;j<n;j++){
				if(matrix[j][i] == 'R'){
					countr++;countb=0;
					if(countr >= k)
						r=true;
				}
				else if(matrix[j][i] == 'B'){
					countb++;countr=0;
					if(countb >= k)
						b=true;
				}
				else{
					countr = countb = 0;
				}
			}
		}

		for(int z=0;z<n;z++){
				int countr = 0, countb=0;
			for(int i=z,j=0;i>=0&&j<n;i--,j++){
				if(matrix[i][j] == 'R'){
					countr++;countb=0;
					if(countr >= k)
						r=true;
				}
				else if(matrix[i][j] == 'B'){
					countb++;countr=0;
					if(countb >= k)
						b=true;
				}
				else{
					countr = countb = 0;
				}
			}
		}
		for(int z=0;z<n;z++){
				int countr = 0, countb=0;
			for(int i=n-1,j=z;i>=0&&j<n;i--,j++){
				if(matrix[i][j] == 'R'){
					countr++;countb=0;
					if(countr >= k)
						r=true;
				}
				else if(matrix[i][j] == 'B'){
					countb++;countr=0;
					if(countb >= k)
						b=true;
				}
				else{
					countr = countb = 0;
				}
			}
		}
		for(int z=0;z<n;z++){
				int countr = 0, countb=0;
			for(int i=0,j=z;i<n&&j<n;i++,j++){
				if(matrix[i][j] == 'R'){
					countr++;countb=0;
					if(countr >= k)
						r=true;
				}
				else if(matrix[i][j] == 'B'){
					countb++;countr=0;
					if(countb >= k)
						b=true;
				}
				else{
					countr = countb = 0;
				}
			}
		}
		for(int z=0;z<n;z++){
				int countr = 0, countb=0;
			for(int i=z,j=0;i<n&&j<n;i++,j++){
				if(matrix[i][j] == 'R'){
					countr++;countb=0;
					if(countr >= k)
						r=true;
				}
				else if(matrix[i][j] == 'B'){
					countb++;countr=0;
					if(countb >= k)
						b=true;
				}
				else{
					countr = countb = 0;
				}
			}
		}
		//for(int z=k-1;z<n;z++){
		//	for(int i=z,j=0;i>=0;i--,j++){
		//		int countr = 0, countb=0;
		//		if(matrix[j][i] == 'R'){
		//			countr++;countb=0;
		//			if(countr >= k)
		//				r=true;
		//		}
		//		else if(matrix[j][i] == 'B'){
		//			countb++;countr=0;
		//			if(countb >= k)
		//				b=true;
		//		}
		//		else{
		//			countr = countb = 0;
		//		}
		//	}
		//}

		if(r && b)
			fout<<"Both"<<endl;
		else if(r)
			fout<<"Red"<<endl;
		else if(b)
			fout<<"Blue"<<endl;
		else 
			fout<<"Neither"<<endl;
	}

	return 0;
}