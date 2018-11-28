#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

class SavingTheUniverse {
private: 
    vector <string> search_engines;
    vector <string> queries;
public: 
    vector <string> SearchEngineThatWorks (string q) {
        vector <string> toReturn = search_engines;
        int i;
        for(i = 0;i<toReturn.size();i++) {
            if(q==toReturn[i]) {
                toReturn.erase(toReturn.begin()+i);
                i--;
            };
        }
        return toReturn;
    };
    void doit() {
        ifstream fin("A-small-attempt6.in");
        ofstream fout("A.out.txt");
        int N;
        int S, Q;
        fin>>N;
        fin.ignore(1,'\n');
        int i, j;
        char temp[111];
        for(i = 0; i<N; i++) {
            cout<<"Case #"<<i+1<<": ";
            cout<<endl;
            fin>>S;
            fin.ignore(1,'\n');
            //cout<<"--";
            for(j = 0; j<S; j++) {
                fin.get(temp,110,'\n');
                fin.ignore(1,'\n');
                search_engines.push_back(temp);
                //cout<<"["<<temp<<"]";
            }
            //cout<<endl;
            fin>>Q;
            fin.ignore(1,'\n');
            //cout<<"++";
            for(j = 0; j<Q; j++) {
                fin.get(temp,110,'\n');
                fin.ignore(1,'\n');
                queries.push_back(temp);
                //cout<<"["<<temp<<"]";
            }
            //cout<<endl;
            int Y = 0;
            vector <string> se_that_works;
            for(j = 0; j<(Q); j++) {
                if(j==0) se_that_works = SearchEngineThatWorks(queries[j]);
                int k;
                for(k = 0;k<se_that_works.size();k++) {
                    if(queries[j]==se_that_works[k]) {
                        se_that_works.erase(se_that_works.begin()+k);
                    };
                }
                if(se_that_works.empty()) {
                    se_that_works = SearchEngineThatWorks(queries[j]);
                    Y += 1;
                    //cout<<Y<<endl;
                };
                //cout<<queries[j]<<": ";
                for(k = 0;k<se_that_works.size();k++) {
                    //cout<<"["<<se_that_works[k]<<"]";
                }
                //cout<<endl;
            }
            fout<<"Case #"<<i+1<<": ";
            fout<<Y;
            fout<<endl;
            cout<<Y;
            cout<<endl;
            search_engines.clear();
            queries.clear();
            //system("PAUSE");
            //system("CLS");
        }
        fin.close();
        fout.close();
    };
};

int main() {
    SavingTheUniverse S;
    S.doit();
    system("PAUSE");
    return 0;
};
