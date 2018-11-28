#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<string> str;
    str.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    str.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    str.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");

    str.push_back("our language is impossible to understand");
    str.push_back("there are twenty six factorial possibilities");
    str.push_back("so it is okay if you want to just give up");

    vector<char> letras('z'-'a'+1,' ');
    for(int i = 0;i<3;++i){
        for(int j = 0;j<str[i].size();++j){
            if(str[i][j] != ' '){
                letras[str[i][j]-'a'] = str[i+3][j];
            }
        }
    }
    letras['q'-'a'] = 'z';
    letras['z'-'a'] = 'q';
    int cases;
    cin>>cases;
    string line;
    cin.ignore();
    for(int i = 0;i<cases;++i){
        cout<<"Case #"<<i+1<<": ";
        getline(cin,line);
        for(int j = 0;j<line.size();++j){
            if(line[j] == ' '){
                cout<<" ";
            }
            else{
                cout<<letras[line[j]-'a'];
            }
        }
        cout<<endl;
    }
    return 0;
}
