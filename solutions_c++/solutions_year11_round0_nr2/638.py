#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;

namespace
{
    enum{
        NUMBER_OF_ALPHABETS=26,
        NO_NUMBER=0
    };
    void DeleteRange(vector<char> *v, int start, int end){
        vector<char>::iterator it1=v->begin(), it2=v->begin();
        it1+=start;
        it2+=(end+1); // 
        v->erase(it1, it2);
    }
}

template <class T>
class RuleTemplate{
    T Map[NUMBER_OF_ALPHABETS][NUMBER_OF_ALPHABETS];

    int ToIndex(char c){
        return c-'A';
    }
public:
    RuleTemplate(){
        Clear();
    }
    void Clear(){
        for(int i=0; i<NUMBER_OF_ALPHABETS; i++){
            for(int j=0; j<NUMBER_OF_ALPHABETS; j++){
                Map[i][j]=NO_NUMBER;
            }
        }
    }
    bool RuleExists(char a, char b){
        return Map[ToIndex(a)][ToIndex(b)]!=NO_NUMBER;
    }
    char GetRule(char a, char b){
        return Map[ToIndex(a)][ToIndex(b)];
    }
    void AppendRule(char a, char b, T c){
        Map[ToIndex(a)][ToIndex(b)]=c;
        Map[ToIndex(b)][ToIndex(a)]=c;
    }
};


int main()
{
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        //cerr << "--------------------------------" << endl;
        RuleTemplate<char> combine;
        RuleTemplate<char> oppose;
        // combine rule
        int C;
        cin >> C;

        for(int j=0; j<C; j++){
            char a, b, c;
            cin >> a >> b >> c;
            combine.AppendRule(a, b, c);
        }

        // oppose rule
        int D;
        cin >> D;
        for(int j=0; j<D; j++){
            char a, b;
            cin >> a >> b;
            oppose.AppendRule(a, b, true);
        }

        // elements
        int N;
        cin >> N;
        vector<char> v(N);
        for(int j=0; j<N; j++){
            char a;
            cin >> a;
            v[j]=a;
        }

        // invoke
        for(unsigned int j=0; j<v.size();){
/*
            for(int k=0; k<v.size(); k++){
                cerr << v[k] << ", ";
            }
            cerr << endl;
*/
            if(j==0){
                j++;
                continue;
            }
            // combine rule
            if(combine.RuleExists(v[j], v[j-1])){
                //cerr << "Combine Rule exists" << endl;
                v[j-1]=combine.GetRule(v[j], v[j-1]);
                DeleteRange(&v, j, j);
                continue;
            }
            // oppose rule
            for(int k=j-1; k>=0; k--){
                if(oppose.RuleExists(v[j], v[k])){
                    //cerr << "Oppose Rule exists (" << 0 << ", " << j << ")" << endl;
                    DeleteRange(&v, 0, j);
                    j=0;
                    break;
                }
            }
            j++;
        }
        cout << "Case #" << (i+1) << ": [";
        for(unsigned int j=0; j<v.size(); j++){
            if(j==0){
                cout << v[j];
            }else{
                cout << ", " << v[j];
            }
        }
        cout << "]" << endl;
    }
    return 0;
}
