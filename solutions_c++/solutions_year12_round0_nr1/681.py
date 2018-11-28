// Problem A. Speaking in Tongues.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
*/
int main()
{
    ifstream input("In_Data.in");
    ofstream output("Out_Data.txt");
    map<char,char> transl;
	//map<char,char>::iterator itm;
    vector<string> inp(3);
    string op;
    for(int i=0;i<3;++i)
    {
        getline(cin,inp[i]);
    }
    for(int i=0;i<3;++i)
    {
        getline(cin,op);
        for(int j=0;j<op.size();++j)
        {
            transl[inp[i][j]]=op[j];
        }
    }
	/*for(itm=transl.begin();itm!=transl.end();itm++)
	{
		cout<<(*itm).first<<": "<<(*itm).second<<endl;
	}*/
	transl['z']='q';
	transl['q']='z';
    int T;
    input>>T;
    input.ignore();
    for(int t=1;t<=T;++t)
    {
        getline(input,op);
		output<<"Case #"<<t<<": ";
        for(int i=0;i<op.size();++i)
        {
            output<<transl[op[i]];
        }
        output<<endl;
    }
    return 0;
}
