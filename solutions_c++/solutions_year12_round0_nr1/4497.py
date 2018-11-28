#include <fstream>
#include <iostream>
#include <map>

#include <vector>

using namespace std;
int main(){
    vector <char> orden;
    //vector <char> vector1;
    //vector <char> vector2;
    int t,i,j;
    map <char,char> decode;
    decode ['q'] = 'z';
    decode ['z'] = 'q';
    decode [' '] = ' ';
    string s;
    string ejemplo1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
    string ejemplo2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
    char c;
    ifstream in ("Googlerese.in");
    ofstream out ("Googlerese.out");   
    for (int i = 0;i<=ejemplo1.size()-1;i++){
          decode[ejemplo1[i]] = ejemplo2[i];
    }
    //for (map<char, char>::const_iterator i = decode.begin();i != decode.end(); ++i){
    //    char k = i->first;
    //    cout<<k;
    //}
    
    //for (map<char, char>::const_iterator i = decode.begin();i != decode.end(); ++i){
    //    char k = i->second;
    //    orden.push_back(k);
    //}
    //cout<<endl;
    //sort (orden.begin(),orden.end());
    //for ( int i = 0; i<=orden.size()-1;i++){
        //cout<<orden[i];    
    //} 
    in>>t;
    getline(in,s);
    for (i = 1;i<=t;i++){
        out<<"Case #"<<i<<": ";
        getline(in,s);
        for (j = 0;j<=s.size()-1;j++){
            out<<decode [s[j]];
        }
        out<<"\n";            
    }
}
