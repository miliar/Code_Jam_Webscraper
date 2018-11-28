#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <set>
#include <cmath>
#include <iomanip>

#include <boost/lexical_cast.hpp>

//const std::string setName = "A-test";
//const std::string setName = "A-small-practice";
//const std::string setName = "A-small-attempt0";
//const std::string setName = "A-small-attempt1";
//const std::string setName = "A-small-attempt2";
const std::string setName = "A-large";
//const std::string setName = "A-large-practice";

template<class T>
void debug(const std::vector<T> & v)
{
	std::copy(v.begin(), v.end(), std::ostream_iterator<T>(std::cout, ", "));
	std::cout << std::endl;
}

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
		int N;
		ifs >> N;
		std::vector<std::size_t> v(N);
		for(int n=0; n<N; ++n)
		{
			std::string line;
			ifs >> line;
			v[n] = line.rfind('1');
			if(v[n]==std::string::npos)
				v[n] = 0;
		}
		
		int swaps = 0;
		for(std::size_t i=0; i<v.size()-1; ++i)
		{
			if(v[i]>i)
			{
				std::size_t min_pos = i+1;
				for(; v[min_pos]>=v[i]; ++min_pos);
				
				for(; min_pos>i; --min_pos)
				{
					std::swap(v[min_pos], v[min_pos-1]);
					++swaps;
				}
				i = -1;
			}
		}
		
		
		int result = swaps;
		ofs       << "Case #" << (t+1) << ": " << result << "\n";
        std::cout << "Case #" << (t+1) << ": " << result << std::endl;
    }


    ifs.close();
    ofs.close();
    std::cout << "Done." << std::endl;

    return 0;
}
