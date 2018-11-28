
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <map>

using namespace std;

class Snapper
{
    string inputFileName;
    string errorDesc;
    int iNoOfSnapper;
    int iNoOfTimeToggle;
    bool isLightOn;
    public:
    Snapper( string _inputFileName )
    {
       inputFileName = _inputFileName;
       errorDesc = "";
    }
    Snapper()
    {
    }
    ~Snapper()
    {
    }
    string getErrorCode() { return errorDesc; }
    bool readInput( map<int,Snapper> &);
    void tokenize( const string& , vector<string> &,
                   const string& );
    void setNoOfSnapper(int _iNoOfSnapper) { iNoOfSnapper = _iNoOfSnapper; }
    void setNoOfTimeToggle( int _iNoOfTimeToggle ) { iNoOfTimeToggle = _iNoOfTimeToggle; }
    int getNoOfSnapper() { return iNoOfSnapper; }
    int getNoOfTimeToggle() { return iNoOfTimeToggle; }
    bool getIsLightOn() { return isLightOn; }
    bool process();
};

bool Snapper::readInput( map< int , Snapper > &inputMap )
{
    int iCaseCount = 0;
    string line="";
    string del = " ";
    ifstream file( inputFileName.c_str() );
    getline( file , line ,'\n' );
    while( !file.eof() )
    {
       line = "";
       vector<string> token;
       Snapper sObj;
       int _iNoOfSnapper =0 , _iNoOfTimeToggle = 0;
       getline( file , line , '\n');
       if( line.empty() )
         continue;
       tokenize( line , token , del );
       if( token.size() == 2 )
       {
          _iNoOfSnapper = atoi(token[0].c_str());
          _iNoOfTimeToggle = atoi(token[1].c_str());
          sObj.setNoOfSnapper( _iNoOfSnapper );
          sObj.setNoOfTimeToggle( _iNoOfTimeToggle );
          inputMap[++iCaseCount] = sObj;
       }
       cout << "Case #"<< iCaseCount << ": " << line << endl;
    }
    file.close();
    return true;
}

void Snapper::tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
    return;
}


bool Snapper::process()
{
    isLightOn = false; 
    vector<int> vToggleSnapper;
    for( int icount =0; icount < iNoOfSnapper ; icount++ ) 
      vToggleSnapper.push_back(0);
    for( int icount =0; icount < iNoOfTimeToggle ; icount++ )
    {
       if( !vToggleSnapper[0] )
         vToggleSnapper[0] = 1;
       else
       {
          bool bToggleBit = true;
          for( vector<int>::iterator vToggleSnapperItr = vToggleSnapper.begin();
          vToggleSnapperItr != vToggleSnapper.end(); vToggleSnapperItr++ )
          {
             bToggleBit = bToggleBit & *vToggleSnapperItr;
             *vToggleSnapperItr = 0;
             if( !bToggleBit )
             {
               *vToggleSnapperItr = 1;
                break;
             }
          }
       }
       /*for( vector<int>::iterator vToggleSnapperItr = vToggleSnapper.begin();
       vToggleSnapperItr != vToggleSnapper.end(); vToggleSnapperItr++ )
       {
          cout << *vToggleSnapperItr << " " ;
       }
       cout << endl;*/
       
    }
    if( vToggleSnapper.size() > 0 )
       isLightOn = vToggleSnapper[0];
    for( int icount =1; icount < iNoOfSnapper ; icount++ ) 
       isLightOn = isLightOn & vToggleSnapper[icount] ;

    return true;
}

string tostring(int number )
{
   char buffer[100];
   sprintf( buffer, "%d", number );
   return string(buffer);
}


int main(int argc,char *argv[])
{
   map< int , Snapper > inputMap;
   ofstream outputFile("output.txt");
   if( argc != 2 )
   {
      cout<<"[ Line@" << __LINE__ << " ] Please Provide the input file as command line argument" << 
      endl;
      cout<<"[ Line@" << __LINE__ << " ] ./a.out InputFileName"<<endl;
      return false;
   }
   string filename = argv[1];
   Snapper SnapperObj(filename);
   if( !SnapperObj.readInput( inputMap ) )
   {
      cout<<"[ Line@" << __LINE__ <<" ] Error in reading the input function" <<
      endl;
      return false;
   }

   for( map<int,Snapper>::iterator inputMapItr = inputMap.begin();
        inputMapItr != inputMap.end(); inputMapItr++ )
   {
      if( !(inputMapItr->second).process() )
      {
         cout << "[ Line@" << __LINE__ << " ] An Error Occured and Error Value[" << 
         (inputMapItr->second).getErrorCode() << "]" << endl;
         return false;
      } 
   }
   for( map<int,Snapper>::iterator inputMapItr = inputMap.begin();
        inputMapItr != inputMap.end(); inputMapItr++ )
   {
      string output = "Case #";
      output = output + tostring(inputMapItr->first);
      if( (inputMapItr->second).getIsLightOn() )
          output = output + ": ON\n";
      else
          output = output + ": OFF\n";
      outputFile << output;
   }
   return true; 
}
