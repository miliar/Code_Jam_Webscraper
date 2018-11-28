
#include<string>
#include<iostream>
#include<cstdlib>
#include<fstream>
#include<cmath>
#include<vector>
using namespace std;

int vectorC = 0;
int main() {

     ifstream in("A-small-attempt4.in");
     if( !in ) {
         cout << "Error Opening File";
         return 1;
         }
     vector<string> vec;
     char line[100];
     int i = 0;
     while( in ) {
          in.getline( line, 100 );
          string str = line;
          vec.push_back(str);
          i++;
          }
     in.close();
     // Input is in vec 
     int cases,
         engines,
         queries;
     int times = 1;
     
     ofstream out("Result.txt");
     
     cases = atoi( vec[vectorC].c_str());
     vectorC++;
     while( cases > 0 ) {          
          //out << cases << "\n";    
          engines = atoi( vec[vectorC].c_str());
          vectorC++;
         // out << engines << "\n";
          vector<string> engine(engines);
          for( int i = 0; i<engines; i++ ) {
             engine[i] = vec[vectorC];
             vectorC++;
            // out << engine[i] << "\n";
             }
         queries = atoi( vec[vectorC].c_str());
         vectorC++;
         vector<string> query(queries);
        // out << queries << "\n";
         for( int i = 0; i<queries; i++ ) {
             query[i] = vec[vectorC];
             vectorC++;
        //   out << query[i] << "\n";
             }
        // out << "engines" << engines << "\t" << "queries" << queries << "\n";
         int switches = -1;    
         int i = 0;
         while( i<queries ) {
               int max_cycleLength = 0;
               for( int j = 0; j<engines; j++ ) {
                   int k = i;
                   while( k<queries && (engine[j] != query[k]) )
                        k++;
                   if( (k-i) > max_cycleLength )
                      max_cycleLength = (k-i);  
                   }   
                 switches++;
                 i = i + max_cycleLength;
              } 
         if( queries == 0 )
            switches = 0;                          
         out << "Case #" << times << ": " << switches << "\n";
         times++;
         cases--;
         }
         out.close();
         return 0; 
         }  
         
