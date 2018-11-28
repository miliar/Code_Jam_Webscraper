#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

bool _debug = false;

struct s2Int{
    unsigned int a,b;
};

class cCase{
    vector<string> dEngines;
    vector<string> dQueries;
public:
    void fAddEngine(string &pEngine){
        dEngines.push_back(pEngine);
    }
    void fAddQuery(string &pQuery){
        dQueries.push_back(pQuery);
    }
    s2Int fGetMaxQueriesEngine(int pOffset = 0){
        unsigned int lIndexEngine, lIndexQuery, lQueries, lIndex;
        vector<s2Int> lResults;
        s2Int lCurResult, lMax;
        lMax.b = 0;
        for(lIndexEngine = 0; lIndexEngine < dEngines.size(); lIndexEngine++){
            lQueries = 0;
            for(lIndexQuery = pOffset; lIndexQuery < dQueries.size(); lIndexQuery++){
                if(dEngines[lIndexEngine].compare(dQueries[lIndexQuery]) == 0){
                    break;
                }
                lQueries++;
            }
            lCurResult.a = lIndexEngine;
            lCurResult.b = lQueries;
            lResults.push_back(lCurResult);
            if(_debug) cout << "Starting at index " << pOffset << " " << dEngines[lIndexEngine] <<
                        " can do " << lQueries << " queries" << endl;
        }
        for(lIndex = 0; lIndex < lResults.size(); lIndex++){
            if(lResults[lIndex].b > lMax.b){
                lMax = lResults[lIndex];
            }
        }
        return lMax;
    }
    int fGetSwitchs(){
        unsigned int lIndexEngine, lIndexQuery, lSwitchs, lOffset;
        s2Int lMax;

        // Special case : A engine is not researched
        for(lIndexEngine = 0; lIndexEngine < dEngines.size(); lIndexEngine++){
            lSwitchs = 0;
            for(lIndexQuery = 0; lIndexQuery < dQueries.size(); lIndexQuery++){
                if(dEngines[lIndexEngine].compare(dQueries[lIndexQuery]) == 0){
                    lSwitchs++;
                }
            }
            if(lSwitchs == 0){
                if(_debug) cout << "Special case, engine " << dEngines[lIndexEngine] << " is not queried" << endl;
                goto end;
            }
        }

        lSwitchs = 0;
        lOffset = 0;

        // Every engine is queried one time
        while(lOffset < dQueries.size()){
            lMax = fGetMaxQueriesEngine(lOffset);
            if(_debug) cout << "We use " << dEngines[lMax.a] << " to go to " << lOffset+lMax.b << endl;
            lOffset += lMax.b;
            lSwitchs++;
        }
        lSwitchs--; // -1 because i count the first :p

end:
        return (lSwitchs);
    }
};

class cInputFile{
    vector<cCase> dCases;
public:
    cInputFile(){
        int N;
        cin >> N;
        if(_debug) cout << "N : " << N << endl;

        for(; N > 0; N--){
            cCase lCurCase;
            string lBuff;

            int S;
            cin >> S;
            if(_debug) cout << "S : " << S << endl;

            // Hack, to prevent bug with cin&getline
            std::getline(std::cin, lBuff);

            for(; S > 0; S--){
                std::getline(std::cin, lBuff);
                lCurCase.fAddEngine(lBuff);
                if(_debug) cout << "Engine : " << lBuff << endl;
            }

            int Q;
            cin >> Q;
            if(_debug) cout << "Q : " << Q << endl;

            // Hack, to prevent bug with cin&getline
            std::getline(std::cin, lBuff);

            for(; Q > 0; Q--){
                std::getline(std::cin, lBuff);
                lCurCase.fAddQuery(lBuff);
                if(_debug) cout << "Query : " << lBuff << endl;
            }

            dCases.push_back(lCurCase);
        }
    }
    void fOutputResults(){
        unsigned int lIndex;
        for(lIndex = 1; lIndex <= dCases.size(); lIndex++){
            cout << "Case #" << lIndex << ": " << dCases[lIndex-1].fGetSwitchs() << endl;
        }
    }
};

int main(){
    cInputFile lInput;
    lInput.fOutputResults();
}
