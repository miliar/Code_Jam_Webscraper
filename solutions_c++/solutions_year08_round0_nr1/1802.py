#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector <string> StrName;
vector <string> StrQuery;
int IntQuery;
int IntEngines;

int FindSolution(){
    int * IntEFirUse = (int *) new int[IntEngines];
    for(int i = 0; i < IntEngines; ++i){
        IntEFirUse[i] = -1;
    }
    vector <string>::iterator ite;
    vector <string>::iterator ite2;
    int num = 0;
    for(ite = StrQuery.begin(); ite != StrQuery.end(); ++ite){
        for(ite2 = StrName.begin(); ite2 != StrName.end(); ++ite2){
            if((*ite) == (*ite2)){
                int tmp = ite2 - StrName.begin();
                if(IntEFirUse[tmp] == -1){
                    IntEFirUse[tmp] = ite - StrQuery.begin();
                    num++;
                    if(num == IntEngines){
                        ite = StrQuery.end() - 1;
                        break;
                    }
                }
                break;
            }
        }
    }
    num = 0;
    for(int i = 0; i < IntEngines; ++i){
        if(IntEFirUse[i] == -1){
            return 0;
        }
        if(IntEFirUse[i] > num){
            num = IntEFirUse[i];
        }
    }
    ite = StrQuery.begin();
    ite2 = StrQuery.begin() + num;
    IntQuery -= num;
    StrQuery.erase(ite,ite2);
    return (1 + FindSolution());
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int IntCases;
    cin >> IntCases;
    int n = 0;
    while(n < IntCases){
        n++;
        StrName.clear();
        StrQuery.clear();
        cin >> IntEngines;
        string TmpName;
        cin.ignore();
        for(int i = 0; i < IntEngines; ++i){
            getline(cin,TmpName);
            StrName.push_back(TmpName);
        }
        //sort(StrName.begin(),StrName.end());
        cin >> IntQuery;
        cin.ignore();
        for(int i = 0; i < IntQuery; ++i){
            getline(cin,TmpName);
            StrQuery.push_back(TmpName);
        }
        //for(int i = 1; ; ++i){
        //    if(FindSolution(i)){
        //        cout << "Case #" << n << ": " << i - 1 << endl;
        //        break;
        //    }
        //}
        cout << "Case #" << n << ": ";
        cout << FindSolution() << endl;
    }
    return 0;
}

