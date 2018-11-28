#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int T, N, L,H,answer = 0;
	string word;
	ifstream file("C-small-attempt0.in");
	ofstream ofile("C-small-attempt0.out");
	file >> T;
	vector<int> freqv;
	int freq;

	for (int i = 0;i<T;++i)
	{
		file >> N;
		file >> L;
		file >> H;


		for(int j =0;j<N;++j){
								
				file >> freq;
				freqv.push_back(freq);
			}

		for (int k = L;k<=H;++k)
		{
			bool worked=true;
			

			vector<int>::iterator it;
			for(it =freqv.begin();it!=freqv.end();++it)
			{

				if ((*it%k) && (k%*it)){
					worked = false;
					break;
				}

			}

			if (worked == true){
				answer =k;
				break;
			}
			
		}
		ofile << "Case #" << i+1<< ": ";
		if (!answer){

			ofile << "NO" << endl;
		}
		else{

			ofile << answer << endl;
		}

		freqv.clear();
		answer =0;

	}


	file.close();
	ofile.close();

	cin >> T;

}