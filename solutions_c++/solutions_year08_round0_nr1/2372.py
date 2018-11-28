//
//
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){

    ifstream ifile( "input.txt" );
    ofstream ofile( "output.txt");

    int num_of_testcase = 0;

    ifile >> num_of_testcase;

    for ( int i = 0 ; i < num_of_testcase ; i++ ) {
    
        int num_of_searchengine = 0;
        vector<string> search;
        int result = 0;

        ifile >> num_of_searchengine;

        for ( int  j = 0 ; j < num_of_searchengine ; j++ ) {
            char buf[1024];
            ifile.getline(buf, sizeof(buf) );
            string tmp(buf);
            if (tmp.length() ==0 ) {
               j--;
               continue;
            }
            search.push_back(tmp);
        }

        int num_of_query = 0;
        ifile >> num_of_query;
        vector<string> chk = search;

        for ( int  j = 0 ; j < num_of_query ; j++ ) {
            char buf[1024];
            ifile.getline(buf, sizeof(buf));
            string query(buf);
            if (query.length() ==0 ) {
                j--;
                continue;
            }

            for(vector<string>::iterator it=chk.begin();it!=chk.end();it++){
                if ( *it == query ) {
                    chk.erase(it);
                    break;
                }
            }
            if ( chk.size()==0 ) {
                result++;
                chk = search;
                for(vector<string>::iterator it=chk.begin();it!=chk.end();it++){
                    if ( *it == query ) {
                        chk.erase(it);
                        break;
                    }
                }
            }
        }

       ofile << "Case #" << i+1 << ": " << result << endl; 

    }
    return true;
}
