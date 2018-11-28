#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>

void f (std::string s, int i){
	//std::cout << "s: " << s << std::endl;

	// parse N, s, p
	size_t spacepos = s.find(" ");
	int N = atoi( s.substr(0, spacepos).c_str());
	s.erase(0, spacepos+1);
	spacepos = s.find(" ");
	int S = atoi( s.substr(0, spacepos).c_str());
	s.erase(0, spacepos+1);
	spacepos = s.find(" ");
	int p = atoi( s.substr(0, spacepos).c_str());
	s.erase(0, spacepos+1);

	//std::cout << "N:" << N << ", S:" << S << ", p:" << p << std::endl;

	// parse t_i's
	std::vector<int> v;
	spacepos=s.find(" ");
	while (spacepos != std::string::npos){
		v.push_back( atoi( s.substr(0, spacepos).c_str()) );
		s.erase(0, spacepos+1);
		spacepos = s.find(" ");
	}
	v.push_back( atoi( s.substr(0, spacepos).c_str()) );

	// compute scores
	int scoreEnough = 0;
	int scorePotentially = 0;
	for( std::vector<int>::iterator it = v.begin(); it!=v.end(); ++it ){
		//std::cout << *it << std::endl;

		bool glatt = (*it / (1.0*3)) - (*it/3) <0.0001?true:false;
		//std::cout << "glatt: " << glatt << std::endl;

		//glatt
		int maxResUnsurprising=0, maxResSurprising=0;
		if(glatt==true && *it!=0){
			maxResUnsurprising = *it/3;
			maxResSurprising = *it/3 +1;
		}

		//nicht glatt
		if (glatt==false){
			maxResUnsurprising = *it/3 +1;
			maxResSurprising = *it/3 +2;
		}
		//std::cout << "maxResUnsurprising: " << maxResUnsurprising << ", maxResSurprising: " << maxResSurprising << std::endl;
		//std::cout << std::endl;

		if(maxResUnsurprising >= p)
			scoreEnough++;
		else if (maxResSurprising >= p)
			scorePotentially++;

	}
	//std::cout << "scoreEnough: " << scoreEnough << ", scorePotentially: " << std::min(scorePotentially, S) << std::endl;
	std::cout << "Case #" << i <<": " << scoreEnough+std::min(scorePotentially, S) << std::endl;
}

int main() {
	//f("3 1 5 15 13 11");
	//f("3 0 8 23 22 21");
	//f("2 1 1 8 0");
	//f("6 2 8 29 20 8 18 18 21");

	//f("1 1 5 14");

	std::ifstream fIn("B-small-attempt0.in");
		if( fIn ) {
		  std::string s = "";
		  getline(fIn, s);
		  //std::cout << "N: " << s << std::endl;
		  int i=1;
		  while( getline(fIn, s) ) {
		  	f(s, i);
		  	i++;
		    //std::cout << s << std::endl;
		  }
		}
		fIn.close();
	return 0;
}
