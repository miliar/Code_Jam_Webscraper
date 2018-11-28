#include <fstream>
#include <iostream>
#include <vector>

using namespace std;
int main(int argc, char *argv[]){
		ifstream ins;
		ins.open(argv[1]);
		long Ncase;
		ins>>Ncase;
		long the_case = 0;
		while (the_case++<Ncase){
				long N;
				ins>>N;
				cout<<"Case #"<<the_case<<": ";
				std::vector<long> data;
				for (long i=0; i<N; ++i){
						long temp;
						ins>>temp;
						data.push_back(temp);
				}
				long check = data[0];
				for (long i=1; i<N; ++i){
						check ^= data[i];
				}
				if (check!=0)
						cout << "NO" <<endl;
				else {
						long ret = 0;
						sort(data.begin(), data.end());
						for (long i=1; i<N; ++i)
								ret +=data[i];
						cout<< ret<<endl;
				}

		}
		ins.close();
		return 0;
}

