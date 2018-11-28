#include <iostream>
#include <fstream>
#include <string>
#include <deque>
#include <map>
#include <list>
#include <vector>
#include <iterator>
#include <set>
#include <algorithm>
using namespace std;
typedef unsigned long long uint_64 ;
typedef long long int_64 ;
#define TRACE(X) std::cout<<X<<std::endl;

class Input
{
    public:
    Input(uint_64 noOfSE,std::deque<std::string> listSE,uint_64 noOfQueries,std::deque<std::string> listQuery);
    void process();

    uint_64 leastSwitch()
    {
        return _leastSwitch;
    }

 private:        
     uint_64 noOfSE;
     uint_64 noOfQueries;
     uint_64 _leastSwitch;
     std::deque<std::string> listSE;
     std::deque<std::string> listQuery;
};



class ReaderWriter
{
public:
    void readInputs(std::string filename)
    {
        ifstream myfile (filename.c_str(),ios::in);
        if(myfile.is_open())
        {
            string line;
                //TRACE("INPUTS READ START");
            while (! myfile.eof() )
            {
                getline (myfile,line);
                cout << line << endl;
                _numberOfInputs=atol(line.c_str());
                ////TRACE("number of inputs ="<<_numberOfInputs);
                for(uint_64 i=0 ; i<_numberOfInputs;i++)
                {
                    getline (myfile,line);
                    uint_64 noOfSearchEngine =atoi(line.c_str());
                    std::deque<std::string> listSE;
                    std::deque<std::string> listQuery;
                    //TRACE("no of search engines"<<noOfSearchEngine)
                    for (uint_64 j=0;j< noOfSearchEngine;j++ )
                    {
                         getline (myfile,line);
                         listSE.push_back(line);
                    }
                    getline (myfile,line);
                    uint_64 noOfQueries =atoi(line.c_str());
                    //TRACE("no of queries"<<noOfQueries)
                    for (uint_64 j=0;j< noOfQueries;j++ )
                    {
                         getline (myfile,line);
                         listQuery.push_back(line);
                    }
                    //TRACE( "The list of SE")
//                    for (std::deque<std::string> ::iterator itr=listSE.begin();itr!=listSE.end();itr++)
//                    {
//                        TRACE(*itr)
//                    }
//                    //TRACE( "The list of Queries")
//                    for (std::deque<std::string> ::iterator itr=listQuery.begin();itr!=listQuery.end();itr++)
//                    {
//                        TRACE(*itr)
//                    }
                    Input inputData(noOfSearchEngine,listSE,noOfQueries,listQuery);
                    _inputs.push_back(inputData);

                }
            }
                myfile.close();
                //TRACE("INPUTS READ END");
        }
        else TRACE("unable to open the file "<<filename);
    }
    void processInputs()
    {
        for (std::deque<Input> ::iterator itr=_inputs.begin();itr!=_inputs.end();itr++)
        {
            itr->process();
        }
    }
    void writeOutput(std::string filename)
    {
        //Case #1: 2 2
//Case #2: 2 0
        ofstream myfile (filename.c_str());
        if(myfile.is_open())
        {
            uint_64 i=1;
            for (std::deque<Input> ::iterator itr=_inputs.begin();itr!=_inputs.end();itr++)
            {
                myfile<<"Case #"<<i<<": "<<itr->leastSwitch()<<"\n";
                i++;
            }
            myfile.close();
        }
        else TRACE("unable to open the file "<<filename);
    }
private:
    uint_64 _numberOfInputs;
    std::deque<Input> _inputs;



};




    Input::Input(uint_64 p_noOfSE,std::deque<std::string> p_listSE,uint_64 p_noOfQueries,std::deque<std::string> p_listQuery)
    :noOfSE(p_noOfSE),listSE(p_listSE),noOfQueries(p_noOfQueries),
    listQuery(p_listQuery),_leastSwitch(noOfQueries)
{
}
void Input::process()
{
    std::map<std::string,bool> globalSEref;
    for (std::deque<std::string> ::iterator itr=listSE.begin(); itr!=listSE.end();itr++ )
    {
        globalSEref[*itr]=true;
    }
    //uint_64 leastSwitch=noOfQueries;
    for (std::deque<std::string> ::iterator itr=listSE.begin(); itr!=listSE.end();itr++ )
    {
        std::string currentSE=*itr;
        uint_64 tmpleastSwitch=0;
        //TRACE("RUN FOR SEARCH ENGINE >>>>"<<*itr);
        for (std::deque<std::string> ::iterator ITR=listQuery.begin(); ITR!=listQuery.end();ITR++ )
        {
            //TRACE("leastSwitch ="<<_leastSwitch);
                //TRACE("tmpleastSwitch ="<<tmpleastSwitch);
                //TRACE("CURRENT SEARCH ENGINE " <<currentSE);
                //sleep(1);
            if (*ITR==currentSE)
            {
                tmpleastSwitch++;
                std::map<std::string,bool> SEref=globalSEref;
                                    //SEref.erase(currentSE);ITR++;
                while( ITR!=listQuery.end())
                {
                //sleep(1);
                    SEref.erase(*ITR);
                //TRACE("SEref.size() ="<<SEref.size());
                    if (SEref.size()==0)
                    {
                        currentSE=*ITR;
                        //if (ITR!=listQuery.begin())
                        
                            ITR--;
                        break;
                    }
                    else
                    {
                        ITR++;
                    }
                }
            }
            if (ITR==listQuery.end())
            {
                break;
            }
        }
        if (tmpleastSwitch<_leastSwitch)
        {
            _leastSwitch=tmpleastSwitch;
        }
    }
    //TRACE("leastSwitch"<<_leastSwitch);

}


int main () {
  string line;
  //ifstream myfile ("inputfile",ios::in);
  ReaderWriter a;
  a.readInputs("A-large.in");
  a.processInputs();
  a.writeOutput("A-large.out");

  return 0;
}
