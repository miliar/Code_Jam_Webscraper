#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <list>

int main(int argc, char** argv){
	if(argc != 2) {
		std::cerr << "No input file given" << std::endl;
		return 1;
	}
	std::string buffer;
	int t;
	std::istringstream istr;
	std::ifstream inputFile;
	inputFile.open(argv[1]);
	
	getline(inputFile, buffer);
	istr.str(buffer);
	istr >> t;
	istr.clear();
	buffer = "";
	
	int i, position, last;
	long r, k, j, n, nextRunTotal, euros;
	std::queue<long> waitingQueue;
	std::list<long> nextRun;
	std::list<long>::iterator iter;
	for(i = 0; i < t; ++i) {	
		getline(inputFile, buffer);
		position = buffer.find(' ');
		istr.str(buffer.substr(0, position));
		istr >> r;
		istr.clear();
		last = position+1;
		position = buffer.find(' ', last);
		istr.str(buffer.substr(last, position-last));
		istr >> k;
		istr.clear();
		last = position+1;
		istr.str(buffer.substr(last));
		istr >> n;
		istr.clear();
		buffer = "";
		
		getline(inputFile, buffer);
		position = -1;
		for(j = 0; j < n; ++j) {
			last = position + 1;
			position = buffer.find(' ' , last);
			istr.str(buffer.substr(last, position-last));
			waitingQueue.push(0);
			istr >> waitingQueue.back();
			istr.clear();			
		}
		
		euros = 0;
		for(j = 0; j < r; ++j) {
			nextRunTotal = 0;
			while(nextRunTotal + waitingQueue.front() <= k) {
				nextRun.push_back(waitingQueue.front());
				waitingQueue.pop();
				nextRunTotal += nextRun.back();
				if(waitingQueue.empty()) break;
			}
			for(iter = nextRun.begin(); iter != nextRun.end(); ++iter) {
				waitingQueue.push(*iter);
			}
			nextRun.clear();
			euros += nextRunTotal;		
		}
		std::cout <<"Case #" << i+1 << ": " << euros << std::endl;
		buffer = "";
		while(!waitingQueue.empty()) {
			waitingQueue.pop();
		}
	}
	
	inputFile.close();
	
	
	return 0;
}
