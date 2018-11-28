#include<iostream>
#include<fstream>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

int main(){

	ifstream entrada("A-large.in");
	ofstream salida("A-large.out");

	int Casos;
	entrada >> Casos;
	for(int caso=1;caso<=Casos;++caso){
		long long int res = 0;
		int N;
		entrada >> N;
		vector<pair <char, int> > boto;
		for(int i=0;i<N;++i){
            char aux;
            int aux2;
            entrada >> aux >> aux2;
            boto.push_back(pair<char,int>(aux,aux2));
		}
        int bPos = 1;
        int oPos = 1;
        for(int i=0;i<N;++i){
           // cout << oPos << " " << bPos << " " << res << endl;
            char act = boto[i].first;
            int actbot = boto[i].second;
            if(act == 'O'){
                int tiempo = abs(actbot-oPos) + 1;
                res += tiempo;
                oPos = actbot;
                int auxPos = -1;
                for(int j=i+1;j<N;++j){
                    if(boto[j].first == 'B'){
                        auxPos = j;
                        break;
                    }
                }
                if(auxPos != -1){
                    int pPos = boto[auxPos].second;
                    if(pPos >= bPos){
                        if(pPos <= bPos+tiempo){
                            bPos = pPos;
                        } else{
                            bPos = bPos+tiempo;
                        }
                    }else{
                        if(pPos >= bPos-tiempo){
                            bPos = pPos;
                        }else{
                            bPos = bPos-tiempo;
                        }
                    }
                }
            } else{
                int tiempo = abs(actbot-bPos) + 1;
                res += tiempo;
                bPos = actbot;
                int auxPos = -1;
                for(int j=i+1;j<N;++j){
                    if(boto[j].first == 'O'){
                        auxPos = j;
                        break;
                    }
                }
                //cout << oPos << " " << auxPos << " " << boto[auxPos].second << endl;
                if(auxPos != -1){
                    int pPos = boto[auxPos].second;
                    if(pPos >= oPos){
                        if(pPos <= oPos+tiempo){
                            oPos = pPos;
                        } else{
                            oPos = oPos+tiempo;
                        }
                    }else{
                        if(pPos >= oPos-tiempo){
                            oPos = pPos;
                        }else{
                            oPos = oPos-tiempo;
                        }
                    }
                }
            }
        }

		salida << "Case #" << caso << ": " << res << endl;
	}
	return 0;
}
