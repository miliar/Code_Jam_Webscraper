#include <iostream>
#include <map>
#include <string>
#include <fstream>


using namespace std;

int main(){
    map<string, string> chars;
    string s0 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string s1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string s2 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string s3 = "y qee";

    string s00 = "our language is impossible to understand";
    string s11 = "there are twenty six factorial possibilities";
    string s22 = "so it is okay if you want to just give up";
    string s33 = "a zoo";

    for(int i=0; i<s0.size();i++) chars[s0.substr(i,1)] = s00.substr(i,1);
    for(int i=0; i<s1.size();i++) chars[s1.substr(i,1)] = s11.substr(i,1);
    for(int i=0; i<s2.size();i++) chars[s2.substr(i,1)] = s22.substr(i,1);
    for(int i=0; i<s3.size();i++) chars[s3.substr(i,1)] = s33.substr(i,1);

    chars["z"] = "q";

    /*
    for( map<string, string>::iterator ii=chars.begin(); ii!=chars.end(); ++ii)
    {

       cout << (*ii).first << ": " << (*ii).second << endl;

    }*/

    ifstream ifs( "rtr.in" );
    ofstream myfile;
    myfile.open ("output.txt");
    string s;
    int k=0;
    while(getline( ifs, s )){
        string s2="";
        if(k){for(int i=0; i < s.size(); i++) s2 += chars[s.substr(i,1)];
        myfile << "Case #"<< k <<": " << s2 << endl;}
        k++;
    }

     myfile.close();

    return 0;
}
