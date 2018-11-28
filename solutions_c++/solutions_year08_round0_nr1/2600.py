#include <string>
#include <fstream>
#include<iostream.h>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
    int n,s,q,cnt;
    string str_tmp;
    vector<string> srch, query, scpy;
    vector<string>::iterator pit;
    ifstream file("C:\\A-large.in");
    getline( file, str_tmp );
    n=atoi(str_tmp.c_str());
for (int i=0;i<n;i++){
    getline( file, str_tmp );
    cnt=0;
    s=atoi(str_tmp.c_str());
      for (int j=0;j<s;j++){
                      getline( file, str_tmp );
                      srch.push_back(str_tmp);
                            }
                            getline( file, str_tmp );
                             q=atoi(str_tmp.c_str());
                             for (int j=0;j<q;j++){
                      getline( file, str_tmp );
                      query.push_back(str_tmp); }
                           scpy.assign( srch.begin(), srch.end() );
            for(int j=0;j<query.size(); j++){


                            for(pit=scpy.begin(); pit != scpy.end(); ){
                                   if (*pit== query[j])
                                   scpy.erase(pit);
                                   else
                                   pit++;
                            }




                    if(scpy.size()==0){
                            scpy.clear();
                            cnt++;
                            j= j-1;
                            scpy.assign( srch.begin(), srch.end() );
                    }
            }
    cout<< "Case #"<<(i+1)<<": "<<cnt<<endl;

     srch.clear();
     query.clear();
     scpy.clear();

    }

    file.close();



  return 0;
}
