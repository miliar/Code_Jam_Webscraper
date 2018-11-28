/* By Joshua Daniel Wilks - UW CS Student

------------Code Jam 2008 -------------*/


#include <list>
#include <fstream>
#include <iostream>



int main(int argc, char **argv){
	std::string word;

	std::ifstream infile;
        infile.open ("smallA.in", std::ifstream::in);

	 std::ofstream outfile;
	 outfile.open ("test.out");

	


	//TEST CASES
	getline(infile,word);
	int testCases = atoi(word.c_str()); 

	//for each test case
	int frequency;
	int result = 0;
	std::list<int> frequencyList;
	int p, k, l;

	for ( int testnumber = 0 ; testnumber < testCases ; testnumber++){
		result = 0;
		
		infile >> p >> k >> l;

		for (int a=0;a < l; a ++){
			infile >> frequency;
			frequencyList.push_back(frequency);
		}
		

		frequencyList.sort();
		frequencyList.reverse();	
	
// 		std:: list<int>::iterator it;
// 
//  		std::cout << "mylist contains:";
//  		 for ( it=frequencyList.begin() ; it != frequencyList.end(); it++ )
//   		  std::cout << " " << *it;
// 		


		for (int i = 1 ;i <= p; i ++){
			for( int j = 0 ;j < k; j++){	
				if(!frequencyList.empty()){
				result += ((int)frequencyList.front() * i);
				frequencyList.pop_front();}
			}
		}
		outfile<< "Case #"<<testnumber+1<<": "<<result<<std::endl;
	result = 0;
	frequencyList.clear();

	}


	
	infile.close();
	outfile.close();
}

