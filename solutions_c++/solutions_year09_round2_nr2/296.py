#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <cmath>

#include <boost/lexical_cast.hpp>

//const std::string setName = "B-test";
//const std::string setName = "B-small-practice";
//const std::string setName = "B-small-attempt0";
//const std::string setName = "B-small-attempt1";
const std::string setName = "B-large";
//const std::string setName = "B-large-practice";



int main() 
{
    const std::string inputFileName  = setName + ".in";
    const std::string outputFileName = setName + ".out";

    std::ifstream ifs( inputFileName.c_str() );
    std::ofstream ofs( outputFileName.c_str() );

    if(!ifs || ! ofs) 
    {
        std::cerr << "Openeing the files went wrong" << std::endl;
        return 1;
    }

    int T;
    ifs >> T;
    
    for(int t=0; t<T; ++t)
    {
		std::string digits;
		ifs >> digits;
		digits = "0"+digits;
		
		std::next_permutation(digits.begin(), digits.end());
		
		if(digits[0]=='0')
			digits = digits.substr(1);
		
        std::string result = digits;

	    ofs       << "Case #" << (t+1) << ": " << result <<"\n";
        std::cout << "Case #" << (t+1) << ": " << result << std::endl;
    }


    ifs.close();
    ofs.close();
    std::cout << "Done." << std::endl;

    return 0;
}
