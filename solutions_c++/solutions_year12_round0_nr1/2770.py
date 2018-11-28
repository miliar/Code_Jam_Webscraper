#include <iostream>
#include <string>
using namespace std;

//-----------Start Fri Apr 13 18:58:33 EDT 2012------------------

int main() {
    int nTestCases;
    char mapto[256]={'\0'},mapfrom[256]={'\0'};
    string line;
    //case 1
    string shouldbe1="our language is impossible to understand";
    string input1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    for (unsigned int i = 0; i < shouldbe1.length(); i ++)
    {
        mapto[shouldbe1[i]]=input1[i];
        mapfrom[input1[i]]=shouldbe1[i];
    }
    //case 2 
    string shouldbe2="there are twenty six factorial possibilities";
    string input2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    for (unsigned int i = 0; i < input2.length(); i ++)
    {
        mapto[shouldbe2[i]]=input2[i];
        mapfrom[input2[i]]=shouldbe2[i];
    }
    //case 3
    string shouldbe3="so it is okay if you want to just give up";
    string input3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    for (unsigned int i = 0; i < input1.length(); i ++)
    {
        mapto[shouldbe3[i]]=input3[i];
        mapfrom[input3[i]]=shouldbe3[i];
    }
    mapto['a']='y';mapto['o']='e';mapto['z']='q';
    mapfrom['y']='a';mapfrom['e']='o';mapfrom['q']='z';
    mapto['q']='z';mapfrom['z']='q';
    cin>>nTestCases;
    getline(cin,line);
    for(int iCase=0;iCase< nTestCases;iCase++) {
        getline(cin,line);
        //implement
        for (unsigned int i = 0; i < line.length(); i ++)
        {
            line[i]=mapfrom[line[i]];
        }
        cout<<"Case #"<<iCase+1<<": "<<line<<endl;;
    }
}
