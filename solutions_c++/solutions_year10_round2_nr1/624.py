
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <utility>
using namespace std;
/*
 *
 */

bool isin(vector<string> f, string d){
    vector<string>::iterator it = f.begin();
    for(; it != f.end(); ++it){
        if(!it->compare(d)) return true;
    }
    return false;
}

string br(string* str){
    int x = str->find_last_of('/');
    if(!x) return "/";
    string res = str->substr(0, x);
    return res;
}


int main(int argc, char** argv) {
    FILE* in = fopen("A-large.in", "r");
    FILE* out = fopen("A-large.out", "w");
    int Cases = 0;
    int N,M;
    int count = 0;
    vector< string > field;
    vector< string > cf;
    fscanf(in, "%d", &Cases);
    for(int i=0; i<Cases;++i){
        count = 0;
        fscanf(in, "%d %d", &N, &M);
        char tmp[101];
        for(int j=0; j<N; ++j){
            fscanf(in, "%s", tmp);
            field.push_back(tmp);
        }
        for(int j=0; j<M; j++){
            fscanf(in, "%s", tmp);
            cf.push_back(tmp);
        }

        for(int j=0; j<cf.size(); ++j){
            while(cf[j].compare("/")){
                if(!isin(field, cf[j])){
                    field.push_back(cf[j]);
                    cf.push_back(br(&cf[j]));
                    ++count;
                }
                else break;
            }
        }
        fprintf(out, "Case #%d: %d\n", i+1, count);
        field.clear();
        cf.clear();
    }
    fclose(out);
    fclose(in);
    return (EXIT_SUCCESS);
}

