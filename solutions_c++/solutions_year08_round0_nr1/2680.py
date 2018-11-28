#include <iostream>

#include <fstream>
#include <map>
#include <list>
#include <string>
#include <cassert>
#include <sstream>
#include <vector>
#include <boost/foreach.hpp>

#include <algorithm>
#include <boost/utility.hpp>
#include <limits>

//! 'Runtime' debug control      (also use NDEBUG)
int debug = false;


int longestProgress( const std::list< std::list<int> >& taskQueue )
{
    std::size_t lprog = std::numeric_limits<std::size_t>::min();
    
    BOOST_FOREACH( const std::list<int>& choiceSeq,  taskQueue )
    {
        lprog = std::max(lprog, choiceSeq.size() );
    }
    
    return lprog;
}


int shortestProgress( const std::list< std::list<int> >& taskQueue )
{
    std::size_t lprog = std::numeric_limits<std::size_t>::max();
    
    BOOST_FOREACH( const std::list<int>& choiceSeq,  taskQueue )
    {
        lprog = std::min(lprog, choiceSeq.size() );
    }
    
    return lprog;
}


int numSwitches( const std::list<int>& seq )
{
    int nswitch = 0;
    
    int icur = seq.front();
    BOOST_FOREACH(int seqCur, seq)
    {
        if( seqCur != icur )
        {
            icur = seqCur;
            ++nswitch;
        }
    }
    
    return nswitch;
}
/*
    std::list<int> seq;
    seq.push_back(0);
    seq.push_back(0);
    seq.push_back(0);
    seq.push_back(1);
    seq.push_back(1);
    seq.push_back(1);
    seq.push_back(0);
    seq.push_back(0);
    seq.push_back(0);
    std::cout << " numSwitches( const std::list<int>& seq ) = " << numSwitches( seq ) << std::endl;
*/

bool numSwitchesSort( const std::list<int>& seqA, const std::list<int>& seqB )
{
    return numSwitches( seqA ) < numSwitches( seqB );
}
/*
    std::list<int> A,B,C,D;
    A.push_back(0); A.push_back(0); A.push_back(0); A.push_back(0);     // 0 changes
    B.push_back(0); B.push_back(1); B.push_back(1); B.push_back(1);     // 1 changes
    C.push_back(0); C.push_back(1); C.push_back(1); C.push_back(0);     // 2 changes
    D.push_back(1); D.push_back(0); D.push_back(1); D.push_back(0);     // 3 changes
    
    taskQueue.push_back(D);
    taskQueue.push_back(A);
    taskQueue.push_back(C);
    taskQueue.push_back(B);
    taskQueue.sort( numSwitchesSort );
    
    
    BOOST_FOREACH( std::list<int>& choiceSeq,  taskQueue )
    {
        std::cout << "\n\nnext list:";
        BOOST_FOREACH( int i,  choiceSeq )
        {
            std::cout << " " << i;
        }
    }
*/



void print(const std::list< std::list<int> >& taskQueue)
{
    std::cout << "taskQueue:\n";
    
    BOOST_FOREACH( const std::list<int>& choiceSeq,  taskQueue )
    {
        std::cout << "next list:";
        BOOST_FOREACH( int i,  choiceSeq )
        {
            std::cout << " " << i;
        }
        std::cout << " numSwitches= " << numSwitches(choiceSeq) << std::endl;
    }
}





void show_seq_soln( const std::list<int>& choiceSeq,  const std::vector<int>& queries_sequence )
{
    std::list<int>::const_iterator choiceItor;
    std::vector<int>::const_iterator queryItor;
    
    choiceItor = choiceSeq.begin();
    queryItor  = queries_sequence.begin();
    
    assert( choiceSeq.size() == queries_sequence.size() );
    
    while(1)
    {
        if( choiceItor ==  choiceSeq.end() )
        {
            break;
        }
        
        std::cout << "query: " << *queryItor << " using engine:  " << *choiceItor << std::endl;
        
        ++choiceItor;
        ++queryItor;
    };
}


void prune( std::list< std::list<int> >& taskQueue )
{
    if(debug)   std::cout << "PRUNE!" << std::endl;
    if(debug)   print(taskQueue);
    
    //can prune them off by saying that if we have multiple ones which are the same length, same number of switches and same current  keep only one
    
    // of ones of a given length and final
    //  take only one of minimal num switches
    
    typedef int Length;
    typedef int Final;
    typedef std::list< std::list<int> >::iterator   SeqItor;
    std::map<  std::pair< Length, Final >,  SeqItor >   lengthsFinals;
    
    for( std::list< std::list<int> >::iterator itor = taskQueue.begin();  itor != taskQueue.end();   )
    {
        std::list<int>& choiceSeq = *itor;
        int length = choiceSeq.size();
        int final  = choiceSeq.back();
        
        if(debug)   std::cout << "looking for length,final = " << length << " " << final << std::endl;
        
        std::pair< Length, Final > lf = std::make_pair(length,final);
        
        std::map<  std::pair< Length, Final >,  SeqItor >::iterator  itorFound = lengthsFinals.find(lf);
        if( itorFound != lengthsFinals.end() )
        {
            SeqItor& sp = itorFound->second;
            std::list<int>& foundSeq = *sp;
            int numSwitchesExisting = numSwitches( foundSeq );
            
            
            if(debug)   
            {
                std::cout << "found ";
                BOOST_FOREACH( int i,  foundSeq )
                {
                    std::cout << " " << i;
                }
                std::cout << " numSwitches= " << numSwitchesExisting << std::endl;
            }
            
            
            
            int numSwitchesCurrent = numSwitches( choiceSeq );
            if(debug)   std::cout << "numSwitchesCurrent = " << numSwitchesCurrent << std::endl;
            
            if( numSwitchesCurrent < numSwitchesExisting )
            {
                SeqItor toErase = sp;
                
                //replace
                sp = itor;
                
                taskQueue.erase( toErase );
            }
            
            if( numSwitchesCurrent >= numSwitchesExisting )
            {
                std::list< std::list<int> >::iterator nextItor = boost::next(itor);
                
                if ( nextItor == taskQueue.end() )
                {
                    taskQueue.erase( itor );
                    if(debug)   std::cout << "erased ok, break" << std::endl;
                    break;
                }
                else
                {
                    //increment before erase
                    taskQueue.erase( itor );
                    if(debug)   std::cout << "erased ok, continue" << std::endl;
                    
                    itor = nextItor;
                    
                    continue;
                }
            }
        }
        else
        {
            if(debug)   std::cout << "not found" << std::endl;
            
            lengthsFinals.insert( std::make_pair(lf, itor) );
        }
        
        
        //increment before erase
        ++itor;
    }
    
    if(debug)   std::cout << "done prune!" << std::endl;
}





int process_case( int num_searchengines, const std::vector<int>& queries_sequence )
{
    //list of possible choice sequences
    std::list< std::list<int> > taskQueue;
    
    //populate with initial choices
    for(int se = 0; se < num_searchengines; ++se)
    {
        if( se == queries_sequence[0] )
        {
            continue;
        }
        
        std::list<int> choice_seq;
        choice_seq.push_back(se);
        
        taskQueue.push_back(choice_seq);
    }
    
    if(debug)   print(taskQueue);
    
    
    
    
    unsigned int shortestProg = 0;
    while( shortestProg < queries_sequence.size() )
    {
        //BOOST_FOREACH( std::list<int>& choiceSeq,  taskQueue )
        for( std::list< std::list<int> >::iterator taskQueueItorThis = taskQueue.begin(); taskQueueItorThis != taskQueue.end(); ++taskQueueItorThis)
        {
            std::list<int>& choiceSeq = *taskQueueItorThis;
            //std::list< std::list<int> >::iterator taskQueueItorThis = taskQueue.begin();
            
            unsigned int curProgress = choiceSeq.size();
            if(curProgress >= queries_sequence.size())
            {
                continue;
                //work on a different one,    this one's finished
            }
            
            int curChoice = choiceSeq.back();
            int curQueryIndex = curProgress;
            
            int curQuery = queries_sequence[curQueryIndex];
            if (curQuery == curChoice)
            {
                std::list< std::list<int> > taskQueue_additions;
                
                //needs a change     replace current by  all next possibilities
                for(int se = 0; se < num_searchengines; ++se)
                {
                    if( se == curQuery )
                    {
                        continue;
                    }
                    
                    std::list<int> choice_seq = choiceSeq;      //continuing from current choice sequence
                    choice_seq.push_back(se);
                    
                    taskQueue_additions.push_back(choice_seq);
                }
                
                taskQueue.erase(taskQueueItorThis);
                taskQueue.merge( taskQueue_additions, numSwitchesSort );
            }
            else
            {
                choiceSeq.push_back(curChoice);
            }
            
            break;
        }
        
        // re-sort taskQueue by num changes
        //taskQueue.sort( numSwitchesSort );
        
        prune( taskQueue );
        
        if(debug) print(taskQueue);
        
        shortestProg = shortestProgress(taskQueue);
        if(debug)   std::cout << "shortestProg = " << shortestProg << std::endl;
    }
    
    
    //print(taskQueue);
    
    
    int minNumSwitches = std::numeric_limits<int>::max();
    
    std::list<int>* chosenSeqPtr = NULL;
    
    //of the ones with longest progress,    find the minimum numswitches
    BOOST_FOREACH( std::list<int>& choiceSeq,  taskQueue )
    {
        unsigned int progress = choiceSeq.size();
        if( progress == queries_sequence.size() )
        {
            int numSw =     numSwitches(choiceSeq);
            
            //minNumSwitches = std::min( minNumSwitches, numSw );
            if( numSw < minNumSwitches )
            {
                minNumSwitches = numSw;
                chosenSeqPtr = &choiceSeq;
            }
        }
        else
        {
            assert(false);
        }
    }
    
    assert( chosenSeqPtr != NULL);
    
    //std::list<int>& choiceSeq = taskQueue.front();
    
    //std::cout << "old ans: " << numSwitches(choiceSeq);
    //std::cout << "new ans: " << minNumSwitches;
    
    //std::cout << "soln:\n";
    //show_seq_soln( *chosenSeqPtr,  queries_sequence );
    
    return minNumSwitches;
}






int main(int argc, char* argv[])
{
    const char delimiter = '\n';
    const char* infilename = argv[1];
    const char* outfilename = argv[2];
    
    
    std::ifstream infile(infilename);
    std::ofstream outfile(outfilename);
    
    
    int numcases=0;
    {
        std::string line;
        std::getline( infile, line, delimiter );
        std::istringstream iss(line);
        iss >> numcases;
    }
    std::cout << "numcases=" << numcases << std::endl;
    
    for(int ncase = 0; ncase < numcases; ++ncase)
    {
        std::cout << "\n\nncase=" << ncase << std::endl;
        
        int num_searchengines = 0;
        {
            std::string line;
            std::getline( infile, line, delimiter );
            std::istringstream iss(line);
            iss >> num_searchengines;
        }
        std::cout << "num_searchengines=" << num_searchengines << std::endl;
        
        //std::vector<std::string> searchengines;
        std::map<std::string, int> searchEnginesMap;
        
        for(int nSearchEngine = 0; nSearchEngine < num_searchengines; ++nSearchEngine)
        {
            std::string searchEngine;
            //infile >> searchEngine;            
            std::getline( infile, searchEngine, delimiter );
            
            std::cout << "got searchEngine = " << searchEngine << std::endl;
            
            //std::pair< std::set<std::string>, bool > result = searchengines.insert(searchEngine);
            
            //searchEnginesMap[searchEngine] = nSearchEngine;
            std::pair< std::map<std::string, int>::iterator, bool> result = 
                    searchEnginesMap.insert( std::make_pair(searchEngine, nSearchEngine) );
            assert(result.second == true );     // must have unique search engine names
        }
        
        //DEBUG:
        //{
        //    const char delimiter = '\n';
        //    std::string line;
        //    std::getline( infile, line, delimiter );
        //    std::cout << "DEBUG" << std::endl;
        //    std::cout << line << std::endl;
        //}
        
        int numQueries = -1;
        {
            std::string line;
            std::getline( infile, line, delimiter );
            std::istringstream iss(line);
            iss >> numQueries;
        }
        std::cout << "numQueries = " << numQueries << std::endl;
        
        assert( numQueries >= 0 );
        
        std::vector<int> queries_sequence;
        for(int nQ = 0; nQ < numQueries; ++nQ)
        {
            std::string searchEngine;
            std::getline( infile, searchEngine, delimiter );
            
            std::cout << "searchEngine Query = " << searchEngine << std::endl;
            
            std::map<std::string, int>::iterator itor_found = searchEnginesMap.find(searchEngine);
            
            assert(itor_found->first == searchEngine);
            
            int searchEngineIndex = itor_found->second;
            
            queries_sequence.push_back(searchEngineIndex);
        }
        
        BOOST_FOREACH(int i, queries_sequence)
        {
            std::cout << "got query for search engine i=" << i << std::endl;
        }
        
        if( queries_sequence.size() == 0 )
        {
            outfile << "Case #" << ncase+1 << ": " << 0 << std::endl;
        }
        else
        {
            outfile << "Case #" << ncase+1 << ": " << process_case( num_searchengines, queries_sequence ) << std::endl;
        }
    }
    
}