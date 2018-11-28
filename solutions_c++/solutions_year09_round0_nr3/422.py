
#include <vector>
#include <map>
#include <string>
#include <iostream>

using namespace std;


string jam = "welcome to code jam";
int ns[19] = {0};
vector<int> idx[27];

void init()
{
    int s=jam.size();
    for(int i=0; i<s; i++) {
        char ch = jam[i];
        if(ch==' '){
            idx[26].push_back(i);
        } else {
            idx[ch-'a'].push_back(i);
        }
    }
}

vector<int>* get(char ch)
{
    if(ch==' ') {
        return &idx[26];
    } else if(ch>='a' && ch<='z') {
        return &idx[ch-'a'];
    } else {
        return NULL;
    }
}

int main()
{
    init();

    int N;
    freopen("..\\in.txt", "r", stdin);
    freopen("..\\out.txt", "w", stdout);

    scanf("%d", &N);
    string str;
    getline(cin, str);

    for(int ncase=0; ncase<N; ncase++) {
        int count=0;
        for(int i=0; i<19; i++) ns[i]=0;

        getline(cin, str);
        int s = str.size();
        for(int i=0; i<s; i++) {
            char ch = str[i];
            vector<int>* pvec = get(ch);
            if(NULL != pvec) {
                int num = pvec->size();
                if(num>0) {
                    for(int j=0; j<num; j++) {
                        int id = (*pvec)[j];
                        if(id==0) {
                            ns[0]++;
                        } else if(ns[id-1] > 0){
                            ns[id] += ns[id-1];
                            ns[id] %= 10000;
                        } else {
                            break;
                        }
                    }
                }
            }
        }

        printf("Case #%d: %04d\n", ncase+1, ns[18]);
    }
    return 0;
}

