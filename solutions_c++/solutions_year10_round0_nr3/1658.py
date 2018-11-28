#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int T;
int R, k, N;
int g[1024];
int visited[1024];
int next[1024];
int guadagno[1024];


int main(){
    //freopen("C.in", "r", stdin);
    
    cin >> T;
    for (int t = 1; t <= T; t++){
      unsigned long long money = 0;
      cin >> R >> k >> N;
      for (int i = 0; i < N; i++)
	cin >> g[i];

      //Per ogni gruppo
      for (int i = 0; i < N; i++){
	int sum = g[i];
	//Per ogni numero di gruppi
        for (int j = 1; j <= N; j++){
	  //Se g[i]+...+g[j] <= k, somma, altrimenti memorizza il guadagno e il successore e finisci il ciclo
	  if (j < N && sum + g[(i + j)%N] <= k){
	    sum += g[(i + j)%N];
	  } else {
	    next[i] = (i + j)%N;
	    guadagno[i] = sum;
	    break;
	  }
	}
      }

      //for (int i = 0; i < N; i++)
	//cout << next[i] << " " << guadagno[i] << endl;

      int pos = 0;

      //Cerca il primo nodo del ciclo
      int cyc = -1;
      
      for (int i = 0; i < N; i++)
	visited[i] = 0;
      
      do {
	visited[pos] = 1;
	pos = next[pos];
      } while (!visited[pos]);
      
      cyc = pos;
      
      //Calcola il guadagno fino a cyc, decrementando R opportunamente.
      pos = 0;
      while (pos != cyc) {
	money += guadagno[pos];
	R--;
	pos = next[pos];
      }

      
      unsigned long int guadagnogiro = 0;
      int partenzegiro = 0;
      //Calcola il guadagno e il numero di partenze per fare un giro completo e tornare a posizione cyc.
      
      do {
	guadagnogiro += guadagno[pos];
	partenzegiro++;
	pos = next[pos];
      } while (pos != cyc);
      
      
      //Numero di giri completi possibili
      int girimax = R / partenzegiro;
      
      //Quanto guadagno dai giri completi?
      money += guadagnogiro * girimax;
      R -= partenzegiro * girimax;
      
      
      //Rimangono da fare R partenze
      for (int r = 0; r < R; r++){
	money += guadagno[pos];
	pos = next[pos];
      }
      
      cout << "Case #" << t << ": " << money << endl;
    }

    return 0;
}
