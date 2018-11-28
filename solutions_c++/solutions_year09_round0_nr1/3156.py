#include <string>
#include <iostream>
#include <vector>
using namespace std;

bool isSub (char a, string& subPat) {
     bool test = false;
     for (int i=0; i<subPat.size(); i++)
         test = test || (a==subPat[i]);
     return test;
}

string getSubPattern(int i, string& pattern) {
       string tmp;
       for (int j=0; j<pattern.size(); j++) {
           if (pattern[j]=='(')
              if (i==0) return pattern.substr(j+1,pattern.find_first_of(')',j)-j-1);
              else {i--; j=pattern.find_first_of(')',j); continue;}
           else if (i==0) {tmp.push_back(pattern[j]); return tmp;}
                else i--;
           }
}

bool isSuitable(string& word, string& pattern) {
     bool test = true;
     for (int i=0; i<word.size(); i++) {
         string tmp = getSubPattern(i,pattern);
         test = test && isSub(word[i],tmp);
         }
     return test;
}

int main() {
    int L,D,N; //L letters, D words, N test cases
    vector<string> words;
    vector<string> patterns;
    vector<int> caseNum;
    scanf("%d %d %d", &L, &D, &N);
    for (int i=0; i<D; i++)  {
        string word;
        cin>>word;
        words.push_back(word);
        }
    for (int i=0; i<N; i++) {
        string pattern;
        cin>>pattern;
        patterns.push_back(pattern);
        }
    for (int i=0; i<N; i++) {
        int caseno=0;
        for (int j=0; j<D; j++)
            if (isSuitable(words[j],patterns[i])) caseno++;
        caseNum.push_back(caseno);
        }
    for (int i=0; i<N; i++) 
        cout<<"Case #"<<i+1<<": "<<caseNum[i]<<endl;
}
