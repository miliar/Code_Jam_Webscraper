#include<iostream>
#include<string>
#include<fstream>
#include<sstream>

using namespace std;

int main() 
{

    
    const char *ifile_name = "C-small-attempt0.in";
    const char *ofile_name = "C-small-attempt0.out";
    
    ifstream in;
    ofstream out;
    in.open(ifile_name);
    out.open(ofile_name);
    
    if( in.is_open() && out.is_open() )
    {
        int nb_cases;
        int case_nb = 1;
        int A, B ;
        int n,m;
        string str;
        int result=0;
        
        in >> nb_cases;
        for ( ; case_nb <= nb_cases ; case_nb++)
        {
             in >> A >> B;
            for( n=A; n<=B ; n++)
            {
                 stringstream strm;         
                 strm << n;
                 strm >> str;
                 int size = str.size();         
                 for(int i=0 ; i<size ; i++ )
                 {
                         str = str.substr(size-1,1) + str.substr(0,size-1);
                         
                         istringstream iss(str);
                         iss >> m; 
                         
                         if( m >=A && m<=B  && m!=n)
                         {
                              result++;   
                          }            
                         
                 }
             }
             out << "Case #" << case_nb << ": " << result/2 << endl;   
             result = 0;            
        }
        
    }
    else
    {
        cerr << "Could not open input and output file" << endl;
    }
    
    return 0;
}
