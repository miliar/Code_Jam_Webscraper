
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <stdlib.h>

using namespace std;

void tokenize(const string& , vector<long>& ,
                      const string& );
class RollarCoaster
{
    string errorDesc;
    long iRound;
    long iCapacity;
    long iNoOfGroup;
    long iTotalMoney;
    vector<long> iNoOfPerson;
    public:
    RollarCoaster( long _iRound , long _iCapacity , 
      long _iNoOfGroup , vector<long> token )
    {
       iRound = _iRound;
       iCapacity = _iCapacity;
       iNoOfGroup = _iNoOfGroup;
       iNoOfPerson = token;
       errorDesc = "";
    }
    RollarCoaster()
    {
    }
    ~RollarCoaster()
    {
    }
    string getErrorCode() { return errorDesc; }
    long getTotalMoney() { return iTotalMoney; }
    bool process();
};

string tostring(long number )
{
   char buffer[1000];
   sprintf( buffer, "%ld" , number );
   return string( buffer );
}

bool readInput( string inputFileName , map< int , RollarCoaster> &inputMap)
{
    string line="" , del = " ";
    long iRound = 0 , iCapacity = 0 , iNoOfGroup = 0;
    int iCaseCount = 0;
    ifstream file( inputFileName.c_str() );
    getline( file , line , '\n' );    
    while( !file.eof() )
    {
       vector<long> token;
       line = "";
       getline( file , line , '\n');
       if( line.empty() )
          continue;
       tokenize( line , token , del );
       if( token.size() == 3 )
       {
          iRound = token[0];
          iCapacity = token[1];
          iNoOfGroup = token[2];
       }
       token.clear();
       line = "";
       getline( file , line , '\n');
       tokenize( line , token , del );
       RollarCoaster rollarCoasterObj( iRound , iCapacity , iNoOfGroup , token );
       inputMap[++iCaseCount] = rollarCoasterObj;
    }
    file.close();
    return true;
}

void tokenize(const string& str, vector<long>& tokens,
                      const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        string temp = str.substr(lastPos , pos - lastPos );
        //tokens.push_back( atoi(str.substr(lastPos, pos - lastPos)).c_str());
        tokens.push_back( long(atoi(temp.c_str())) );
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
    return;
}


bool RollarCoaster::process()
{ 
   iTotalMoney = 0;
   for( long icount = 0 ; icount < iRound ; icount++ )
   {
      long iNoOfPersonOnBoard = 0;
      long totalCapacity = 0;
      vector<long>::iterator itr = iNoOfPerson.begin();
      for( int size = 0 ; size < iNoOfPerson.size(); size++ )
      {
         long value = *itr;
         cout << totalCapacity << " " << value << endl;
         totalCapacity = totalCapacity + value;
         if( totalCapacity > iCapacity )
         {
            totalCapacity = totalCapacity - value;
            break;
         }
         else if( totalCapacity == iCapacity )
         {
            itr = iNoOfPerson.erase(itr);
            iNoOfPerson.push_back( value );
            break;
         }
         itr = iNoOfPerson.erase(itr);
         iNoOfPerson.push_back( value );
      }
      iTotalMoney = iTotalMoney + totalCapacity * 1;
   }
   return true;
}

int main(int argc,char *argv[])
{
   map< int , RollarCoaster > inputMap;
   ofstream outputfile("output.txt");
   if( argc != 2 )
   {
      cout<<"[ Line@" << __LINE__ << " ] Please Provide the input file as command line argument" << 
      endl;
      cout<<"[ Line@" << __LINE__ << " ] ./a.out InputFileName"<<endl;
      return false;
   }
   string filename = argv[1];
   readInput(filename , inputMap );

   for( map<int,RollarCoaster>::iterator itr = inputMap.begin();
        itr != inputMap.end(); itr++ )
   {
      if( !(itr->second).process() )
      {
         cout << "[ Line@" << __LINE__ << " ] An Error Occured and Error Value[" << 
         (itr->second).getErrorCode() << "]" << endl;
         return false;
      }
   } 
   for( map<int,RollarCoaster>::iterator itr = inputMap.begin();
        itr != inputMap.end(); itr++ )
   {
      string output = "Case #";
      output = output + tostring(itr->first) +": " +
       tostring((itr->second).getTotalMoney()) + "\n";
      outputfile << output;
   }
   return true; 
}
