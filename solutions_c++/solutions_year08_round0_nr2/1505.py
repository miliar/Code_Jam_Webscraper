#include <iostream.h>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    int n=0,na,nb,counta=0,countb=0;
    int str1i,str2i,str3i,str4i,tot;
    vector <pair <int,int> > qa,qb;
    string str,str1,str2,str3,str4;
    char stra[10],strb[10];
    ifstream file( "C:\\B-large.in" );
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
            str1i = atoi(str1.c_str())*60+atoi(str2.c_str());
            qa.push_back(make_pair( str1i, 1 ));
            str2i = atoi(str3.c_str())*60+atoi(str4.c_str())+tot;
            qb.push_back(make_pair( str2i, -1 ));
        }
        for (int j=0;j<nb;j++){
            getline( file, str );
            str1 = str.substr (0,2);
            str2 = str.substr (3,2);
            str3 = str.substr (6,2);
                  str4 = str.substr (9,2);
                  str1i = atoi(str1.c_str())*60+atoi(str2.c_str());
                  qb.push_back(make_pair( str1i, 1 ));
                  str2i = atoi(str3.c_str())*60+atoi(str4.c_str())+tot;
                  qa.push_back(make_pair( str2i, -1 ));
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
        qa.clear();
        qb.clear();


        cout<< "Case #"<<(i+1)<<": "<<counta<<" "<<countb<<endl;
    }

    file.close();



  return 0;
}
