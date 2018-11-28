#include <string>
#include <fstream>
#include<iostream.h>
#include <vector>
#include <cstdio>
using namespace std;

int main()
{          int n=0;

    string str,temp="";
    vector<string> srch;
    vector<string> query;
    vector<string> srch_copy;
    vector<string>::iterator positit;
ifstream file( "C:\\A-large.in" );
// Do error checking here

getline( file, str );
n=atoi(str.c_str());
for (int i=0;i<n;i++){
    getline( file, str );
    int s=0,q=0,count=0,k;;
    s=atoi(str.c_str());
     count=0;
      for (int j=0;j<s;j++){
                      getline( file, str );
                      srch.push_back(str);
                            }
                            getline( file, str );
                             q=atoi(str.c_str());
                             for (int j=0;j<q;j++){
                      getline( file, str );
                      query.push_back(str); }
                           srch_copy.assign( srch.begin(), srch.end() );
            for(int j=0;j<query.size(); j++){


                            for(positit=srch_copy.begin(); positit != srch_copy.end(); ){
                                   if (*positit== query[j])
                                   srch_copy.erase(positit);
                                   else
                                   positit++;
                            }




                    if(srch_copy.size()==0){
                            count++;
                            j--;
                            srch_copy.assign( srch.begin(), srch.end() );
                    }
            }
    cout<< "Case #"<<(i+1)<<": "<<count<<endl;
     while( !srch.empty() ) {
     srch.pop_back();
 }
     while( !query.empty() ) {
     query.pop_back();
 }
     while( !srch_copy.empty() ) {
     srch_copy.pop_back();
 }
		
    }

    file.close();



  return 0;
}
