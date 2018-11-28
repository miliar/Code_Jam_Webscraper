#include <iostream.h>
#include <vector>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int n,na,nb;
    int ca,cb;
    int s1i,s2i,s3i,s4i,tot;
    vector <pair <int,int> > tta;
    vector <pair <int,int> > ttb;

    vector <string> dataeq;

    string str,str1,str2,str3,str4;
    char stra[10],strb[10];
    ifstream file( "C:\\B-large.in" );
    getline( file, str );
    n=atoi(str.c_str());
    for (int i=0;i<n;){
        ca=0;
        cb=0;
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
            s1i = atoi(str1.c_str())*60+atoi(str2.c_str());
            tta.push_back(make_pair( s1i, 1 ));
            s2i = atoi(str3.c_str())*60+atoi(str4.c_str())+tot;
            ttb.push_back(make_pair( s2i, -1 ));
        }
        for (int k=0;k<nb;k++){
            getline( file, str );
            str1 = str.substr (0,2);
            str2 = str.substr (3,2);
            str3 = str.substr (6,2);
            str4 = str.substr (9,2);
            s1i = atoi(str1.c_str())*60+atoi(str2.c_str());
            ttb.push_back(make_pair( s1i, 1 ));
            s2i = atoi(str3.c_str())*60+atoi(str4.c_str())+tot;
            tta.push_back(make_pair( s2i, -1 ));
        }

        sort (tta.rbegin(), tta.rend());

        sort (ttb.rbegin(), ttb.rend());

        for (int j=0;j<nb+na;j++){
            ca=tta[j].second + ca;
            cb=ttb[j].second+cb;
            if(ca<0)
                        ca=ca+1;
            if(cb<0)
                        cb=cb+1;
        }
        tta.clear();
        ttb.clear();

        i++;
        cout<< "Case #"<<i<<": "<<ca<<" "<<cb<<endl;
    }

    file.close();
    return 0;
}
