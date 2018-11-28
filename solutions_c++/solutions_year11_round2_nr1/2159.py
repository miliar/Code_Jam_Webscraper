
#include<iostream>
#include<set>
#include<map>
#include<deque>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

int main(){

	int n;
	int t = 1;
    cin>>t;

    for(int tt = 0 ; tt < t; tt++){
		
        int teams;
        cin>>teams;
        map<int, map<int, char> > placar;
        vector<int> qt(teams);
        vector<double> wp(teams);
        vector<double> owp(teams);
        vector<double> oowp(teams);
        
        map<int , set< int > > jogou;

        for(int i = 0; i < teams; i++){
            for(int j = 0 ; j < teams; j++){
                cin>> placar[i][j];
                if(placar[i][j] != '.'){
                    wp[i] += (placar[i][j] - '0');
                    qt[i]++;
                    jogou[i].insert(j);
                }
            }
        }

        for(int i = 0; i < teams; i++){
            wp[i] /= qt[i];
            int bla = 0;
            //ut<< i << " " << owp[i] <<endl;
        }

        for(int i = 0; i < teams; i++){
            double soma = 0;
            int media = 0;

            for(int j = 0; j < teams; j++){
               if(placar[i][j] == '.') continue;
                media++;
                int jogos = 0;
                int soma2 = 0;

               for(int k = 0; k < teams; k++){
                    if(placar[j][k] != '.' && k!=i){
                        soma2 += (placar[j][k] - '0');
                        jogos++;
                    }     
                }
                if(jogos> 0){
                    double awp = (1.0*soma2)/jogos;
                    soma += awp;
                }
            }
            if(media > 0)
                owp[i] = soma / media;
            else
                owp[i] = 0.0;
        }
        

        for(int i = 0; i < teams; i++){
            double sum = 0.0;
            int conta = 0;
            for(int j = 0; j < teams; j++){
                if(placar[i][j] != '.'){
                    sum += owp[j];
                    conta++;
                }
            }
            oowp[i] = sum / conta;
        }

		printf("Case #%d:\n",tt+1);

        for(int i = 0 ; i < teams; i++){
            // 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
            cout<< 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
        }
	}

	return 0;

}



