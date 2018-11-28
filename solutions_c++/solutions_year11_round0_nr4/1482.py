#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip.h> 
using namespace std;

double factor(int n){
		double ret = 1.;
		for (int i=2; i<=n; ++i)
				ret *= i;
		return ret;
}

int min(vector<int> data, int start){
		int the_min = data[start], min_indx = start;
		for (int ii=start; ii<data.size(); ++ii)
				if (the_min>data[ii]){
						the_min=data[ii];
						min_indx = ii;
				}
		return min_indx;
}
int main(int argc, char *argv[]){
		ifstream ins;
		ins.open(argv[1]);
		int Ncase;
		ins>>Ncase;
		int the_case = 0;
		while (the_case++ < Ncase){
				int N;
				ins>>N;
				vector<int> data;
				//cout<<" ++++++ ";
				double counter = 0.;
				for (int i=0; i<N; ++i){
						int temp;
						ins>>temp;
						data.push_back(temp);
				//		cout<<temp<<" ";
						if (temp!=i+1)
								counter +=1.;
				}
				cout.setf(ios::showpoint);   
				//cout<<"Case #"<<the_case<<": "<<setiosflags(ios::fixed)<<setprecision(6)<<out<<std::endl;
				cout<<"Case #"<<the_case<<": "<<setiosflags(ios::fixed)<<setprecision(6)<<counter<<std::endl;
		}
        ins.close();
        return 0;
}
