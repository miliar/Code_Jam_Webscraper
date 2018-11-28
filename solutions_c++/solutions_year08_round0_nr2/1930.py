#include <string>
#include <fstream>
#include<iostream.h>
#include <vector>
#include <cstdio>
#include<algorithm>
using namespace std;

int main()
{

    int n=0,na,nb,counta,countb,str1int,str2int,str3int,str4int,tot;
    vector <pair <int,int> > qa,qb;
       vector <pair <int,int> >::iterator pos;
    string str,str1,str2,str3,str4;
    char stra[10],strb[10];
ifstream file( "C:\\B-large.in" );
// Do error checking here

getline( file, str );

n=atoi(str.c_str());
for (int i=0;i<n;i++){
    counta=0;
    countb=0;

    getline( file, str );
     tot=atoi(str.c_str());
    getline( file, str );

    sscanf(str.c_str(), "%s%s", stra,strb );
     na= atoi(stra);
      nb= atoi(strb);
       for (int j=0;j<na;j++){
          getline( file, str );

                  str1 = str.substr (0,2);
                  str2 = str.substr (3,2);
                  str3 = str.substr (6,2);
                  str4 = str.substr (9,2);

                  str1int = atoi(str1.c_str())*60+atoi(str2.c_str());

                  //qa[j].first=str1int;
                  //qa[j].second=1;
                  qa.push_back(make_pair( str1int, 1 ));

                  str2int = atoi(str3.c_str())*60+atoi(str4.c_str())+tot;
                 qb.push_back(make_pair( str2int, -1 ));

                }
                for (int j=0;j<nb;j++){
                           getline( file, str );

              str1 = str.substr (0,2);
                  str2 = str.substr (3,2);
                  str3 = str.substr (6,2);
                  str4 = str.substr (9,2);
                  str1int = atoi(str1.c_str())*60+atoi(str2.c_str());
                  qb.push_back(make_pair( str1int, 1 ));
                  str2int = atoi(str3.c_str())*60+atoi(str4.c_str())+tot;
                  qa.push_back(make_pair( str2int, -1 ));
                }

             sort (qa.rbegin(), qa.rend());
              sort (qb.rbegin(), qb.rend());

               for (int j=0;j<nb+na;j++){
                counta=qa[j].second + counta;
                countb=qb[j].second+countb;
                if(counta<0)
                counta=counta+1;
                if(countb<0)
                countb=countb+1;
                         }

                                     while( !qa.empty() ) {
     qa.pop_back();
 }
     while( !qb.empty() ) {
     qb.pop_back();
 }

    cout<< "Case #"<<(i+1)<<": "<<counta<<" "<<countb<<endl;
                 }

    file.close();



  return 0;
}
