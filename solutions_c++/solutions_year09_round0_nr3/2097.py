#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

#include <boost/lexical_cast.hpp>

const std::string welcome = "welcome to code jam";
std::vector<bool> calcOccur() {
    std::vector<bool> ovec(256,false);
    for(auto it=welcome.begin(); it!=welcome.end(); ++it)
        ovec[*it] = true;
    return ovec;
}
std::vector<bool> occure = calcOccur();

std::vector<int> reduce(std::string & str)
{
    // remove all characters, that are not in use
    // and remove double occurences
    std::string result;
    std::vector<int> weights;
    for(auto it=str.begin(); it!=str.end(); ++it)
    {
        if(occure[*it])
        {
            if(result.size()>0 && (*it)==(*result.rbegin()))
            {
                ++(*weights.rbegin());
            } 
            else
            {
                result += (*it);
                weights.push_back(1);
            }
        }
	}
    str = result;

    // remove everything bevore the first 'w' and after the last 'm'
    std::string::size_type wPos = str.find('w');
    std::string::size_type mPos = str.rfind('m');
    if(wPos == std::string::npos || mPos == std::string::npos || mPos<wPos)
    	str = "";
    else
    {
    	str = str.substr(wPos, mPos-wPos+1);
    	weights = std::vector<int>(weights.begin()+wPos, weights.begin()+mPos+1);
	}

    return weights;
}

int calc(std::string & line)
{
    //std::cout << "#" << line << "#" << "\n";
    std::vector<int> weights = reduce(line);
    //std::cout << "#" << line << "#" << "\n";
    //std::cout << "#"; 
    //for(int i=0; i<weights.size(); ++i)
    //    std::cout << weights[i];
    //std::cout << "#\n";

    if(line.size() < welcome.size())
    {
        //std::cout << "life is to short\n";
        return 0;
    }

    std::vector<bool> match(line.size()-welcome.size(), 0);
    match.insert(match.end(), welcome.size(), 1);
    
    /*
    std::cout << "#";
    for(int i=0; i<match.size(); ++i)
        std::cout << ((match[i]==0)?"0":"1");
    std::cout << "#\n";
    */
    //std::cout << mul << std::endl;

    int count = 0;
    do
    {
        unsigned int wi = 0;
        bool hit = true;
        int mul = 1;
        for(unsigned int i=0; i<match.size(); ++i)
        {
            if(match[i]==1)
            {
                if(line[i] != welcome[wi])
                {
                    hit = false;
                    break;
                }
                mul *= weights[i];
                ++wi;
            }
        }
        if(hit)
            count = (count + mul) % 10000;
    }
    while(std::next_permutation(match.begin(), match.end()));

    return count % 10000;
}

int main() 
{
    //const std::string setName = "C-test";
    //const std::string setName = "C-small-attempt0";
    const std::string setName = "C-small-attempt1";
    //const std::string setName = "C-large";
    const std::string inputFileName  = setName + ".in";
    const std::string outputFileName = setName + ".out";

    std::ifstream ifs( inputFileName.c_str() );
    std::ofstream ofs( outputFileName.c_str() );

    if(!ifs || ! ofs) 
    {
        std::cerr << "Openeing the files went wrong" << std::endl;
        return 1;
    }

    int N;
    ifs >> N;
    
    for(int t=0; t<N; ++t)
    {
        std::string line;
        ifs >> std::ws;
        std::getline(ifs, line);
        int count = calc(line);
        std::string count_str = boost::lexical_cast<std::string>(count);
        count_str.insert(0, 4-count_str.size(), '0');

        ofs       << "Case #" << (t+1) << ": " << count_str <<"\n";
        std::cout << "Case #" << (t+1) << ": " << count_str <<"\n";
    }


    ifs.close();
    ofs.close();
    std::cout << "Done." << std::endl;

    return 0;
}
