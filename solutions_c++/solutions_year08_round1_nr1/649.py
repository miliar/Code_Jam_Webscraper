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
    Input(std::vector<int_64> x,std::vector<int_64> y,uint_64 noOfPairs);
    void process();

    int_64 leastDotProd()
    {
        return _leastDotProd;
    }

 private:        
     uint_64 noOfPairs;
     int_64 _leastDotProd;
     std::vector<int_64> x;
     std::vector<int_64> y;
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
                    uint_64 vectors =atoi(line.c_str());
                    //TRACE("no of vectors"<<vectors)
					            string line1;
								            string line2;
                    getline (myfile,line1);
					getline (myfile,line2);
					std::vector<int_64> x;
					std::vector<int_64> y;
					char* result; char* result1	;	
					result = strtok( const_cast<char*>(line1.c_str()), " " );

					int k=1;
					while( result != NULL ) {
						//printf( "  result is \"%s\"\n", result );
												x.push_back(atoi(result));
						result = strtok( 0, " " );
						//printf( "  result is \"%s\"\n", result );
					}
					TRACE("outside");
					result1 = strtok(const_cast<char*>( line2.c_str()), " " );
					while( result1 != NULL ) {
						//printf( "       result is \"%s\"\n", result1 );
						
						y.push_back(atoi(result1));
						result1 = strtok( 0, " " );
						
					}
                    //TRACE("no of queries"<<noOfQueries)

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
                    Input inputData(x,y,vectors);
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
                myfile<<"Case #"<<i<<": "<<itr->leastDotProd()<<"\n";
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





void Input::process()
{
	int_64 sum=0;
	int_64 newSum=0;_leastDotProd=0;
	int i=0;
	 std::sort(x.begin(), x.end());
	 std::sort(y.begin(), y.end());
	 std::reverse(y.begin(), y.end());
	for (int i=0;i<noOfPairs ; i++)
	{
		 _leastDotProd+=x[i]*y[i];
	}
   
}
Input::Input(std::vector<int_64> px,std::vector<int_64> py,uint_64 pnoOfPairs):x(px),y(py),noOfPairs(pnoOfPairs)
{
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
