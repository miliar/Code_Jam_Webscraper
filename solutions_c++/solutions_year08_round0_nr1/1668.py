#include <string>
#include<fstream>
#include<iostream.h>
#include <vector>
#include <cstdio>
using namespace std;

int main()
{
    int n=0;
    string str="",temp="";
    vector<string> search;
    vector<string> query;
    vector<string> search_copy;
    vector<string>::iterator pos;
    ifstream file( "C:\\A-large.in");


getline( file, str );
n=atoi(str.c_str());
for (int i=0;i<n;i++){
    getline( file, str );
    int s=0,q=0,count=0;
    s=atoi(str.c_str());
    count=0;
    for (int j=0;j<s;j++){
                      getline( file, str );
                      search.push_back(str);
    }
                      getline( file, str );
                      q=atoi(str.c_str());
                      for (int j=0;j<q;j++){
                          getline( file, str );
                          query.push_back(str);
                      }
                          search_copy.assign( search.begin(), search.end() );
                      for(int j=0;j<query.size(); j++){
                              for(pos=search_copy.begin(); pos != search_copy.end(); ){
                                                           if (*pos== query[j])
                                                           search_copy.erase(pos);
                                                           else
                                                               pos++;
                              }

                              if(search_copy.size()==0){
                                                        count++;
                                                        j--;
                                                        search_copy.assign( search.begin(), search.end() );
                              }
                      }
                      cout<< "Case #"<<(i+1)<<": "<<count<<endl;
                      search.clear();
                      query.clear();
                      search_copy.clear();
}
file.close();
return 0;
}
