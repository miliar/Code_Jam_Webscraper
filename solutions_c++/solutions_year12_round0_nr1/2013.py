#include<iostream>
#include<map>
using namespace std;

map<char,char> result;
void analysis(string& C,string& c)
{
    for(int i = 0;i<C.length();++i)
        result[c[i]] = C[i];
}
string use(string& input){
    string ret;
    for(auto i :input){
        char tmp = result[i];
        ret.push_back(tmp);
    }
    return ret;
}
int main(int argc, char *argv[])
{
    string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string b = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string c = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string A = "our language is impossible to understand";
    string B = "there are twenty six factorial possibilities";
    string C = "so it is okay if you want to just give up";
    analysis(A,a);
    analysis(B,b);
    analysis(C,c);
    result['q'] = 'z';
    result['z'] = 'q';
    // for(auto i = result.begin();i!=result.end();++i)
    // {
    //     cout<<i->second<<"->"<<i->first<<endl;
    // }
    int n;
    cin>>n;
    string input;
    getchar();
    for (int i = 0; i < n; ++i)
    {
        getline(cin,input);
        cout<<"Case #"<<i+1<<": "<<use(input)<<endl;
    }
    
    return 0;
}

