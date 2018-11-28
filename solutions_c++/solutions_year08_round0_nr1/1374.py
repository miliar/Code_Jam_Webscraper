#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <string>

int SearchInNameList ( std::vector<std::string> &s, std::string &name, int i, int j );

int main()
{
    unsigned int N, S, Q;
    int search_engine_number;
    int i,j,k;
    std::vector<std::string> searchEngine;  
    std::string queryName;
    int count, searchEngineUsedCount;
    bool searchEngineUsed[100];
    char buf[101];
    
    std::cin >> N;
    for( j=0; j<N; ++j )
    {
        std::vector<std::string>().swap(searchEngine);
        //read in those names of search engines
        std::cin >> S;
        std::cin.getline(buf, 101);
        for( i=0; i<S; ++i)
        {
            std::cin.getline(buf, 101);
            queryName = buf;
            searchEngine.push_back(queryName);
        }
        sort ( searchEngine.begin(), searchEngine.end() );
//        for( i=0; i<S; ++i)
//        {
//            std::cout << searchEngine.at(i) << std::endl; 
//        }
        //read in queries and count for switches
        searchEngineUsedCount = count = 0;
        for( i=0; i<S; ++i ) searchEngineUsed[i] = false;
        std::cin >> Q;
        std::cin.getline(buf, 101);
        for( i=0; i<Q; ++i)
        {
            std::cin.getline(buf, 101);
            queryName = buf;
            search_engine_number = SearchInNameList( searchEngine, queryName, 0, searchEngine.size()-1);
            assert(search_engine_number>=0);
//            std::cout << "query search engine name number #" << search_engine_number << std::endl;
            if( !searchEngineUsed[search_engine_number] )
            {
                searchEngineUsed[search_engine_number] = true;
                searchEngineUsedCount++;
            }
            if( searchEngineUsedCount == S )
            {
//                std::cout << "all engine meet! choose #" << searchEngine.at(search_engine_number) << " for before" << std::endl;
                count++;
                searchEngineUsedCount = 1;
                for( k=0; k<S; ++k ) searchEngineUsed[k] = false;
                searchEngineUsed[search_engine_number] = true;
            }
            
        }
        //output result
        std::cout << "Case #" << j+1 << ": " << count << std::endl;
    }
    
    return 0;
}
int SearchInNameList ( std::vector<std::string> &se, std::string &name, int i, int j )
{
    int k;
    if ( i>j ) return -1;
    
    k=(i+j)/2;
    
    if ( name.compare(se.at(k)) < 0)
    {
        return SearchInNameList( se, name, i, k-1);
    }else if ( name.compare(se.at(k)) > 0)
    {
        return SearchInNameList( se, name, k+1, j);
    }else
    {
        return k;
    }
    
    return 0;
}

