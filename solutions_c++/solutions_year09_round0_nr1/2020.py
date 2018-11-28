#include <iostream>
#include <fstream>
#include <vector>

std::vector<std::string> dict;
int L, D, N;

int findMatchCount(const std::string & code)
{
    std::vector<std::string> digits;
    bool diverse = false;
    for(unsigned int i=0; i<code.size(); ++i)
    {
        if(code[i] == '(') {
            diverse = true;
            digits.push_back("");
            continue;
        }
        if(code[i] == ')') {
            diverse = false;
            continue;
        }

        if(diverse) {
            digits.back().append(1,code[i]);
        }
        else
            digits.push_back(std::string(1,code[i]));
        
    }

    int count = 0;
    for(auto it = dict.begin(); it!=dict.end(); ++it)
    {
        bool matches = true;
        for(int l=0; l<L; ++l)
            if(digits[l].find(it->at(l)) == std::string::npos )
                matches = false;
        if(matches)
            ++count;
    }
    return count;
}

int main() 
{
    //const std::string setName = "A-test";
    //const std::string setName = "A-small-attempt0";
    const std::string setName = "A-large";
    const std::string inputFileName  = setName + ".in";
    const std::string outputFileName = setName + ".out";

    std::ifstream ifs( inputFileName.c_str() );
    std::ofstream ofs( outputFileName.c_str() );

    if(!ifs || ! ofs) 
    {
        std::cerr << "Openeing the files went wrong" << std::endl;
        return 1;
    }

    ifs >> std::skipws >>  L >> D >> N;

    for(int i=0; i<D; ++i)
    {
        std::string word;
        ifs >> word;
        dict.push_back(word);
    }

    for(int i=0; i<N; ++i)
    {
        std::string code;
        ifs >> code;
        int matchCount = findMatchCount(code);
        std::cout << "Case #" << (i+1) << ": " << matchCount << "\n";
        ofs       << "Case #" << (i+1) << ": " << matchCount << "\n";
    }

    ifs.close();
    ofs.close();
    std::cout << "Done." << std::endl;

    return 0;
}
