#include<iostream.h>
#include <vector>
#include <cstdio>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    int n,s,q,count;
    string str="";
    vector<string> srch, query, scpy;
    vector<string>::iterator positit;
    ifstream file("C:\\A-large.in");
getline( file, str );
n=atoi(str.c_str());
for (int i=0;i<n;i++){
    getline( file, str );
    count=0;
    s=atoi(str.c_str());
      for (int j=0;j<s;j++){
                      getline( file, str );
                      srch.push_back(str);
                            }
                            getline( file, str );
                             q=atoi(str.c_str());
                             for (int j=0;j<q;j++){
                      getline( file, str );
                      query.push_back(str); }
                           scpy.assign( srch.begin(), srch.end() );
            for(int j=0;j<query.size(); j++){


                            for(positit=scpy.begin(); positit != scpy.end(); ){
                                   if (*positit== query[j])
                                   scpy.erase(positit);
                                   else
                                   positit++;
                            }




                    if(scpy.size()==0){
                            scpy.clear();
                            count++;
                            j= j-1;
                            scpy.assign( srch.begin(), srch.end() );
                    }
            }
    cout<< "Case #"<<(i+1)<<": "<<count<<endl;

     srch.clear();
     query.clear();
     scpy.clear();

    }

    file.close();



  return 0;
}
