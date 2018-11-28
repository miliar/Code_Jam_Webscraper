#include <iostream>
#include <fstream>

using namespace std;

int wordLen, nWords, nCase;
string dict[5005];
bool mat[20][26];

int main() {
    cin>>wordLen>>nWords>>nCase;
    for(int a=0; a<nWords; a++) cin>>dict[a];
    for(int a=1; a<=nCase; a++) {
        string in;
        cin>>in;
        int s = 0;
        for(int lt=0; lt<wordLen; lt++,s++) {
            for(int c=0; c<26; c++) mat[lt][c] = 0;
            if(in[s]!='(') {
                mat[lt][in[s]-'a'] = 1;
            } else {
                int e = in.find_first_of(')',s);
                for(int c=s+1; c<e; c++) {
                    mat[lt][in[c]-'a'] = 1;
                }
                s=e;
            }
        }
        
        int numFound=0;
        for(int c=0; c<nWords; c++) {
            int match = 1;
            for(int d=0; d<wordLen; d++) {
                if(!mat[d][dict[c][d]-'a']) {
                    match = 0;
                    break;
                }
            }
            if(match) numFound++;
        }
        cout<<"Case #"<<a<<": "<<numFound<<endl;
    }
    return 0;
}
