#include<iostream>
#include<fstream>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

int main(){

	ifstream entrada("B-large.in");
	ofstream salida("B-large.out");

	int Casos;
	entrada >> Casos;
	for(int caso=1;caso<=Casos;++caso){
		vector<char> res;
		int C, D, N;
		entrada >> C;
        vector<string> comb;
        for(int i=0;i<C;++i){
            string aux;
            entrada >> aux;
            comb.push_back(aux);
        }
        entrada >> D;
        vector<string> opp;
        for(int i=0;i<D;++i){
            string aux;
            entrada >> aux;
            opp.push_back(aux);
        }
        entrada >> N;
        string orig;
        entrada >> orig;
        for(int i=0;i<N;++i){
            char act = orig[i];
            //si se combina, combino
            bool combina = false;
            char combi;
            if(res.size()>0){
                char ant = res[res.size()-1];
                for(int j=0;j<C;++j){
                    if((comb[j][0] == ant && comb[j][1] == act) || (comb[j][0] == act && comb[j][1] == ant)){
                        combi = comb[j][2];
                        combina = true;
                        break;
                    }
                }
                if(combina){
                    res[res.size()-1] = combi;
                }
            }
            //si se opone, borro
            bool opone = false;
            if(!combina){
                for(int j=0;j<res.size()&&!opone;++j){
                    char ant = res[j];
                    for(int k=0;k<D;++k){
                        if((opp[k][0] == act && opp[k][1] == ant) || (opp[k][0] == ant && opp[k][1] == act)){
                            opone = true;
                            break;
                        }
                    }
                }
                if(opone){
                    res.clear();
                }
            }
            //sino lo pongo
            if(!opone && !combina){
                res.push_back(act);
            }
        }

		salida << "Case #" << caso << ": ";
		salida << "[";
		for(int i=0;i<res.size();++i){
		    if(i!=res.size()-1){
                salida << res[i] << ", ";
		    } else{
                salida << res[i];
		    }
		}
		salida << "]" << endl;
	}
	return 0;
}
