#include<iostream>
#include<vector>
#include<string>
#include<fstream>

using namespace std;

void print(vector<string> vec){
    for(int i = 0; i < vec.size(); ++i){
        cout<<vec[i]<<endl;
    }
}

vector< vector<bool> > ok(16, vector<bool>(30,false));

//sets ok
void setOk(const string& s){
    for(int i = 0; i < ok.size(); ++i){
        for(int k = 0; k < ok[i].size(); ++k) ok[i][k]= false;
    }
    
    int pos = 0, i = 0;
    while(i < s.size()){
        if(s[i] == '('){
            ++i;
            while(s[i] != ')'){
                ok[pos][(int)(s[i]-'a')] = true;
                ++i;
            }
            ++i;
        }
        else{
            ok[pos][(int)(s[i]-'a')] = true;
            ++i;
        }
        ++pos;
    }
}

//checks
bool check(const string& word){
    for(int i = 0; i < word.size(); ++i){
        if(!ok[i][(int)(word[i]-'a')]) return false;
    }
    return true;
}

int main()
{

    ofstream fout("alien.out");

    int L,D,N;
    cin>>L>>D>>N;
    
    //reads input
    vector<string> words(D,"");

    for(int i = 0; i < D; ++i) cin>>words[i];

    //starts computing
    for(int i = 0; i < N; ++i){
        string pos;
        cin>>pos;

        setOk(pos);
        
        int ret = 0;

        for(int k = 0; k < words.size(); ++k){
            if(check(words[k])) ++ret;
        }
    
        cout<<"Case #"<<i+1<<": "<<ret<<endl;
        fout<<"Case #"<<i+1<<": "<<ret<<endl;
    }

    return 0;
}
