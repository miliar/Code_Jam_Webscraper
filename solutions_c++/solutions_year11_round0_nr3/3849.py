#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main()
{
	int T,N, temp;
	ifstream file("C-small-attempt0.in");
	ofstream ofile("C-small-attempt0.out");
	list<int> sweets;
	file >> T;

	for (int i = 0; i<T;++i){

		sweets.clear();

		file >> N;
		for (int j = 0; j< N;++j){

			file >> temp;
			sweets.push_back(temp);


		}
		bool possible = false;
		int maxvalue = 0;
		int loops = (1<<N)/2;
		for (int j = 1; j<loops;++j){
			int index = 0, sum1 =0, sum2 = 0,xsum1 = 0,xsum2 = 0;

			for(list<int>::iterator it = sweets.begin();it !=sweets.end(); ++it,++index)
			{

				if (((j>>index)&1)==1){
					sum1+=*it;
					xsum1^=*it;
				}
				else{
					xsum2^=*it;
					sum2+=*it;
				}

			}

			if (xsum1==xsum2){
				possible = true;
				if (sum1 > maxvalue)
					maxvalue = sum1;
				if (sum2 > maxvalue)
					maxvalue = sum2;

			}
		}
		ofile << "Case #" << i+1 << ": ";
		if (possible)
			ofile << maxvalue << endl;
		else
			ofile << "NO" << endl;

	}

	file.close();
	ofile.close();
	
}