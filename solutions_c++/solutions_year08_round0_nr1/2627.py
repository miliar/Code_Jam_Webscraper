#include <vector>

#include <fstream>
#include <iostream>


void printVector(std::vector<std::string> vectorStack){
	
	for (int i = 0 ; i < vectorStack.size(); i++ ){
		std::cout<<vectorStack[i]<<std::endl;
	}
		std::cout<<"/n"<<std::endl;

}

bool checkInVector(std::vector<std::string> vectorStack,std::string word){
	if (vectorStack.empty())	
		return false;

	for (int i = 0 ; i < vectorStack.size(); i++ ){
		if (vectorStack[i]==word){
		return true;}

	}

	return false;
}


int main(int argc, char **argv){
	char line[256];
	std::string word;
	std::vector<std::string> searchEngines;
	std::vector<std::string> searchEnginesUsed;

	 std::ofstream outfile;
	  outfile.open ("small.out");

	std::ifstream infile;
        infile.open ("A-small-attempt4.in", std::ifstream::in);


	//TEST CASES
	getline(infile,word);
	int testCases = atoi(word.c_str()); 
	//std::cout << testCases<<std::endl;

	int result = 0;
	//For each test Cases

	for (int i = 0; i < testCases; i++){
		getline(infile,word);
		int numSearchEngines = atoi(word.c_str()); 
		//std::cout << numSearchEngines<<std::endl;
	
		//For each search engine .. Add to vector

		for (int j = 0; j < numSearchEngines ; j++){
			getline(infile,word);
			searchEngines.push_back(word);
			//std::cout << word<<std::endl;	
		}
		
		getline(infile,word);
		int numSearches = atoi(word.c_str()); 
		//std::cout << numSearches<<std::endl;

		
		
		for (int k = 0; k < numSearches ; k++){
			getline(infile,word);
			if (checkInVector(searchEngines,word)){
				if (checkInVector(searchEnginesUsed,word)){
				}
				else{
					searchEnginesUsed.push_back(word);
					if (searchEnginesUsed.size()==searchEngines.size()){
						result++;
						searchEnginesUsed.clear();
						searchEnginesUsed.push_back(word);}
	
					
				}
				//std::cout << word<<std::endl;	
			}
			//Search is valid in all engines
			else{}
			
		}
	
		outfile<<"Case #"<<i+1<<": "<<result<<std::endl;

/*	printVector(searchEngines);
printVector(searchEnginesUsed);*/
	searchEngines.clear();
	searchEnginesUsed.clear();
	result=0;
	}

infile.close();
outfile.close();
}

