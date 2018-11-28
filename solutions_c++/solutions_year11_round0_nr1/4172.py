#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

int main()
{
	int T, N, temp, opos, bpos;
	char color;
	vector<int> orange;
	vector<int> blue;
	vector<char> order;
	ifstream file("A-large.in");
	ofstream ofile("A-large.out");
	file >> T;
	for (int i = 0; i<T; i++){

		opos = 1; bpos = 1; orange.clear(); blue.clear();order.clear();


		file >> N;
		for (int j = 0; j<N; j++)
		{
			file >> color;
			file >> temp;
			if( color =='O')
				orange.push_back(temp);
			if (color == 'B')
				blue.push_back(temp);
			order.push_back(color);

		}

		vector<int>::iterator bit = blue.begin();
		vector<int>::iterator oit = orange.begin();
		vector<char>::iterator orderit = order.begin();

		int time = 0;

		while(true){

			bool press = false;	



			if (bit !=blue.end()){
				int bdifference = *bit - bpos;

				if(bdifference){
					bdifference = bdifference/abs(bdifference);
					bpos+=bdifference;
				}
				else{
					if (*orderit =='B'){
						++bit;
						++orderit;
						press = true;
					}
				}
			}

			if (oit !=orange.end()){
				int odifference = *oit - opos;



				if(odifference){
					odifference = odifference/abs(odifference);
					opos+=odifference;

				}
				else{
					if (*orderit =='O' && !press){
						++oit;
						++orderit;
					}
				}
			}
			++time;

			if ((bit ==blue.end())&& (oit == orange.end()))
				break;
		}


		ofile << "Case #" << i+1 <<": " << time << endl;

	}




	file.close();
	ofile.close();

}