#include <string>
#include <cstdio>
#include <iostream.h>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    int n,na,nb,ca,cb,s1i,s2i,s3i,s4i,rest_time;
    vector <pair <int,int> > ta, tb;

    vector<int> atemb,temppp;
    string str,str1,str2,str3,str4;
    char stra[10];
    char strb[10];
    ifstream file("C:\\B-large.in");
    getline( file, str );
    n=atoi(str.c_str());
    for (int i=0;i<n;i++){
        ca=0;
        cb=0;
        getline( file, str );
                 rest_time=atoi(str.c_str());
        getline( file, str );
                 sscanf(str.c_str(), "%s%s", stra, strb );
                 na= atoi(stra);
                 nb= atoi(strb);
        for (int k=0;k<na;k++)
        {
            getline( file, str );
            str1 = str.substr (0,2);
            str2 = str.substr (3,2);
            str3 = str.substr (6,2);
            str4 = str.substr (9,2);
            s1i = atoi(str1.c_str())*60+ atoi(str2.c_str());
            ta.push_back(make_pair( s1i, 1 ));
            s2i = atoi(str3.c_str())*60+ atoi(str4.c_str())+rest_time;
            tb.push_back(make_pair( s2i, -1 ));
        }
        for (int k=0;k<nb;k++)
        {
            getline( file, str );
            str1 = str.substr (0,2);
            str2 = str.substr (3,2);
            str3 = str.substr (6,2);
            str4 = str.substr (9,2);
            s1i = atoi(str1.c_str())*60+ atoi(str2.c_str());
            tb.push_back(make_pair( s1i, 1 ));
            s2i = atoi(str3.c_str())*60+ atoi(str4.c_str())+rest_time;
            ta.push_back(make_pair( s2i, -1 ));
        }
         sort (ta.rbegin(), ta.rend());
         sort (tb.rbegin(), tb.rend());
        for (int j=0;j<nb+na;j++){
            ca=ta[j].second + ca;
            cb=tb[j].second+cb;
            if(ca<0)
            ca=ca+1;
            if(cb<0)
            cb=cb+1;
        }

        ta.clear();
        tb.clear();

        cout<< "Case #"<<(i+1)<<": "<<ca<<" "<<cb<<endl;
    }
    file.close();
    return 0;
}
