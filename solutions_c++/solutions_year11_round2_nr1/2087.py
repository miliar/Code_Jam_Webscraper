#include<cstdio>
#include<string>
#include<iostream>

using namespace std;

int main(){
	int N,T;
	string p[110];
	double WP[110],OWP[110],OOWP[110],RPI[110];

	cin>>N;
	double sum;
    int numJogos,numVitorias;

	for(int t = 1; t <= N; t++){
		cin>>T;
		for(int i = 0; i < T; i++){
            cin>>p[i];
		}

        for(int i = 0; i < T; i++){	//	Calcula WP para os times
            numJogos = 0;
            numVitorias = 0;

            for(int j = 0; j < p[i].size(); j++){
                if(p[i][j] != '.')  numJogos++;
                if(p[i][j] == '1')  numVitorias++;
            }
            WP[i] = numVitorias / (double)numJogos;
        }

        for(int i = 0; i < T; i++){	//	Calcula OWP para os times
            double avg;
            int numTimes;

            avg = 0.0;
            numTimes = 0;

            for(int j = 0; j < p[i].size(); j++){
                if( i == j )    continue;
                if(p[i][j] != '.'){
                    numTimes++;
                    numJogos = 0;
                    numVitorias = 0;
                    for(int k = 0; k < p[j].size(); k++){
                        if(k == i) continue;
                        if(p[j][k] != '.')  numJogos++;
                        if(p[j][k] == '1')  numVitorias++;
                    }
                }else   continue;
                avg += numVitorias / (double)numJogos;
            }
            OWP[i] = avg / (double)numTimes;
        }

        for(int i = 0; i < T; i++){	//	Calcula OOWP para os times
            sum = 0.0;
            numJogos = 0;

            for(int j = 0; j < p[i].size(); j++){
                if( i == j )    continue;
                if(p[i][j] != '.')	numJogos++, sum += OWP[j];
            }
            OOWP[i] = sum / (double)numJogos;
        }

        for(int i = 0; i < T; i++){
            RPI[i] = 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i];
        }

        cout<<"Case #"<<t<<":"<<endl;
        for(int i = 0; i < T; i++){
            //cout<<WP[i]<<" "<<OWP[i]<<" "<<OOWP[i]<<endl;
            printf("%0.8lf\n",RPI[i]);
        }
	}
	return 0;
}
