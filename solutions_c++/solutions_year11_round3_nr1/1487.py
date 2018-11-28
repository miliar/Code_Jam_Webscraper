#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int T, R, C;
	string word;
	ifstream file("A-large.in");
	ofstream ofile("A-large.out");
	file >> T;
	vector<string> matrix;

	for (int i = 0; i<T; ++i){

		file >> R;
		file >> C;	

		cout << R << endl;
		cout << C << endl;

		for(int j = 0;j<R;++j){
			file >> word;
			matrix.push_back(word);


		}

		vector<string>::iterator it; 
		int count = 0, changed = 0;
		for (it = matrix.begin(); it!=matrix.end();++it)
		{

			string::iterator sit;
			for (sit = (*it).begin();sit!=(*it).end();++sit)
			{
				if (*sit=='#'){
					count++;
				}

			}
		}

		cout << count << endl;

		if (count !=0 && (count % 4)==0){
			int row = 0;

			for (it = matrix.begin(); it!=(matrix.end()-1);++it)
			{


				int column = 0;

				string::iterator sit;
				for (sit = (*it).begin();sit!=((*it).end()-1);++sit)
				{
					
					if (*sit=='#'){

						if ((matrix[row])[column]=='#' && (matrix[row+1])[column+1]=='#' && (matrix[row+1])[column]=='#' && (matrix[row])[column+1]=='#'){

							(matrix[row])[column]='/';
							(matrix[row+1])[column+1]='/';
							(matrix[row+1])[column]='\\';
							(matrix[row])[column+1]='\\';

							++changed;
							
						}

					}
					++column;
					
				}
				
				++row;
			}
		}

		ofile << "Case #" << i+1 <<": " <<  endl;
		if ((changed*4) != count)
		{
			ofile << "Impossible" << endl;
		}
		else
		{
			for(int j = 0;j<R;++j){

				ofile << matrix[j] << endl;


			}
		}
		count = 0;
		changed = 0;
		matrix.clear();

	}
	
	file.close();
	ofile.close();

	cin >> T;

}