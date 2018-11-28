#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <string>
using namespace std;

#define MAX 10010
#define NUM_LETTERS 26

int pos[26];
vector<char> letters[MAX];
char words[MAX][12];
int len[MAX];
int N,M;
char qry[27];
//map< int > remain;
map< string,int > cSet[2];
int state[MAX];
string str[MAX];
int score[MAX];
char nxt[MAX];
int charSet[2][ 1025 ][11];

inline bool cmp(const char &a, const char &b){
    return pos[ (int)(a-'a') ] < pos[ (int)(b-'a') ];
}

int T;

int main(){
    scanf("%d",&T);
    for (int caseID = 1; caseID <= T; caseID++){
        //remain.clear();
        scanf("%d%d",&N,&M);
        printf("Case #%d:",caseID);
        for (int i = 0; i < N; i++){
            scanf("%s",words[i]);
            letters[i].clear();
            len[i] = strlen(words[i]);
            for (int j = 0; j < len[i]; j++) letters[i].push_back(words[i][j]);
            sort(letters[i].begin(),letters[i].end());
            vector<char>::iterator it = unique(letters[i].begin(),letters[i].end());
            letters[i].resize(it-letters[i].begin());
        }
        while (M--){
            scanf("%s",qry);
            for (int i = 0; i < NUM_LETTERS; i++)
                pos[ (int)(qry[i]-'a') ] = i;
            //memset(charSet, 0, sizeof charSet);

            int cur = 0, nxt = 1;
            cSet[cur].clear();
            for (int i = 0; i < N; i++){ 
                //sort(letters[i].begin(),letters[i].end(), cmp);
                //state[i] = 0;
                //map[state[i]]++;
                //nxt[i] = letters[i][0];
                str[i] = "";
                for (int k = 0; k < len[i]; k++) str[i] += "_";//string('_',len[i]);
//                cout<<str[i]<<endl;
                int a = cSet[cur][ str[i] ];
                //cout<<"a of "<<words[i]<<" is "<<a<<endl;
                for (unsigned k = 0; k < letters[i].size(); k++)
                    a |= (1<<(int)(letters[i][k]-'a'));
                    //charSet[cur][ state[i] ][ len[i] ] |= (1<<(int)(letters[i][k]-'a'));
                cSet[cur][str[i]] = a;
            }
            memset(score, 0, sizeof score);
            for (int i = 0; i < NUM_LETTERS; i++){
                int lID = (int)(qry[i]-'a');
                //printf("letter %c\n",qry[i]);
                //memset(charSet[nxt], 0, sizeof charSet[nxt]);
                cSet[nxt].clear();
                for (int k = 0; k < N; k++){
                    //printf("state of word %d = %s score =%d\n",k,str[k].c_str(),score[k]);
                    //decide that for this word, will Sean guess?
                    if ((cSet[cur][ str[k] ] >> lID)&1){
                        string prev = str[k];//state[k];
                        for (int j = 0; j < len[k]; j++)
                            if (words[k][j] == qry[i]) str[k][j] = qry[i];
                        if (str[k] == prev) score[k]++;
                        //printf("new satte of word %d = %s\n",k,str[k].c_str());
                        
                    }
                    int a = cSet[nxt][str[k]];
                    for (unsigned j = 0; j < letters[k].size(); j++)
                            a |=(1<<(int)(letters[k][j]-'a'));
                            //charSet[nxt][state[k]][ len[k] ] |= (1<<(int)(letters[k][j]-'a'));
                    cSet[nxt][str[k]] = a;
                }
                int tmp = cur;
                cur = nxt;  
                nxt = tmp;
            }
            int best = -1, idx = -1;
            for (int i = 0; i < N; i++)
                if (score[i] > best){
                    best = score[i];
                    idx = i;
                }
            printf(" %s", words[idx]);
        }
        printf("\n");
    }
    return 0;
}
