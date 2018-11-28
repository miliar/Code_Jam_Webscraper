#include <boost/thread.hpp>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>

int *results;
void mainprocess(int i, int r, int k, int n, const std::vector<int> data);
int main(){
	int size;
	std::string line;
	std::cin >> size;

	results=new int[size];
	boost::thread **threads=new boost::thread*[size];

	std::getline(std::cin,line);
	for(int i=0;i<size;i++){
		int r,k,n;
		std::cin >> r;
		std::cin >> k;
		std::cin >> n;
		std::getline(std::cin,line);
		std::getline(std::cin,line);
		std::istringstream iss(line);
		std::vector<int> data;
		while(!iss.eof()){
			int s;
			iss>>s;
			data.push_back(s);
		}
		threads[i]=new boost::thread(boost::bind(mainprocess,i,r,k,n,data));
		//size=1;break;
	}

	for(int i=0;i<size;i++){
		threads[i]->join();
		delete threads[i];
	}

	for(int i=0;i<size;i++){
		if(i!=0) std::cout << std::endl;
		std::cout << "Case #" << i+1 << ": " << results[i];
	}

	delete [] threads;
	delete [] results;
	return 0;
}
//////////////////////////////////////////////////////

void mainprocess(int thread, int r, int k, int n, const std::vector<int> data){
	int acc_num=0;
	int num=0,nextnum=0;
	int i=0,starti;
	

	for(int j=0;j<r;j++){
		num=0;nextnum=0;
		starti=i;
		while(nextnum <= k){
			num=nextnum;
//			std::cout << data[i%n] << std::endl;
			nextnum+=data[i%n];
			i++;
			if(starti%n == i%n){
				if(nextnum <= k) num=nextnum;
				break;
			}
		}
		i--;
//		std::cout << "==" << num << "==" << std::endl;

		acc_num+=num;
	}

	results[thread]=acc_num;
}



