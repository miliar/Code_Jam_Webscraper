#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>

/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
 */

bool wordMatchesTest( const std::string &word, const std::vector<std::string> &test );

void printVector( const std::vector<std::string> &vec )
{
    for( int x = 0; x < vec.size(); ++x )
        std::cout << vec[x] << std::endl;
    std::cout << std::endl;
}

int main( int argc, char *argv[] )
{
    for( int i = 1; i < argc; ++i )
    {
        std::ifstream ifs( argv[i] );
        if( ifs.good() )
        {
            int wordLength;
            int wordCount;
            int testCaseCount;
            if( (ifs >> wordLength) && (ifs >> wordCount) && (ifs >> testCaseCount) )
            {
                std::vector<std::string> dict;
                std::string line;
                std::getline( ifs, line ); // throw away the rest of the header line
                for( int ln=0; ln < wordCount; ++ln )
                {
                    std::getline( ifs, line );
                    dict.push_back( line );
                }
//                printVector( dict );

                std::vector< std::vector<std::string> > testwords;
                for( int ln=0; ln < testCaseCount; ++ln )
                {
                    std::getline( ifs, line );
                    std::vector<std::string> onetest(wordLength);
                    int lineind = 0;
                    for( int chind = 0; chind < wordLength; ++chind )
                    {
                        // if the next char in the line is a (, then start  a new string,
                        // otherwise just add that char to onetest.
                        if( '(' == line[lineind] )
                        {
                            ++lineind;
                            while( ')' != line[lineind] )
                            {
                                onetest[chind].push_back( line[lineind] );
                                ++lineind;
                            }
                            ++lineind;
                        }
                        else
                        {
                            onetest[chind] = line[lineind];
                            ++lineind;
                        }
                    }
//                    printVector( onetest );
                    testwords.push_back( onetest );
                }

                for( int ln=0; ln < testCaseCount; ++ln )
                {
                    std::vector<std::string> onetest(testwords[ln]);
                    int count = 0;
                    for( int dictind = 0; dictind < wordCount; ++dictind )
                    {
                        if( wordMatchesTest( dict[dictind], onetest ) )
                            ++count;
                    }
                    std::cout << "Case #" << (ln+1) << ": " << count << std::endl;
                }
            }
            else
            {
                std::cerr << "Error reading in header line." << std::endl;
            }
        }
        else
        {
            std::cerr << "Unable to open file: " << argv[i] << std::endl;
        }
    }
    return 0;
}

bool wordMatchesTest( const std::string &word, const std::vector<std::string> &test )
{
    for( int ind = 0; ind < word.size(); ++ind )
    {
        bool match = false;
        for( int ch = 0; !match && (ch < test[ind].size()); ++ch )
        {
            if( word[ind] == test[ind][ch] )
            {
                match = true;
            }
        }
        if( !match ) return false;
    }
    return true;
}
