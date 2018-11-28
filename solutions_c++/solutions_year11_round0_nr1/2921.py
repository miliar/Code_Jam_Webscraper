#include <cstdlib>
#include <iostream>
#include <fstream>
#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;

int listaBotones[200][2];

struct robot {
       int elapsedTime;
       int nextFromVec;
       int position;
};

int costeDespl(struct robot r, int max) {
    if (r.nextFromVec>=max)
       return 0;
    int bttn=listaBotones[r.nextFromVec][1];
    return (abs(bttn-r.position));
}

int calcularPasos(int max) {
    int boton=0, oTime=0, bTime=0, aux=0;
    struct robot oRobot, bRobot;
    // Cada uno conoce su posición y su boton iniciales; elapsedTime a 0
    oRobot.elapsedTime=bRobot.elapsedTime=0;
    oRobot.position=bRobot.position=1;
    for (aux=0; aux<max && listaBotones[aux][0]!=(int)'O'; aux++);
    oRobot.nextFromVec=aux;
    for (aux=0; aux<max && listaBotones[aux][0]!=(int)'B'; aux++);
    bRobot.nextFromVec=aux;
    // Main while
    while (boton<max) {
          oRobot.elapsedTime+=costeDespl(oRobot, max); // They have to arrive sooner or later...
          if (oRobot.nextFromVec<max)
             oRobot.position=listaBotones[oRobot.nextFromVec][1];
          bRobot.elapsedTime+=costeDespl(bRobot, max);
          if (bRobot.nextFromVec<max)
             bRobot.position=listaBotones[bRobot.nextFromVec][1];
          if (listaBotones[boton][0]==(int)'O') {
             oRobot.elapsedTime++; // Push the button
             if (bRobot.elapsedTime < oRobot.elapsedTime)
                bRobot.elapsedTime = oRobot.elapsedTime;
                
            for (aux=oRobot.nextFromVec+1; aux<max && listaBotones[aux][0]!=(int)'O'; aux++);
                oRobot.nextFromVec=aux;
          }
          else if (listaBotones[boton][0]==(int)'B') {
             bRobot.elapsedTime++; // Push the button
             if (oRobot.elapsedTime < bRobot.elapsedTime)
                oRobot.elapsedTime = bRobot.elapsedTime;
                
            for (aux=bRobot.nextFromVec+1; aux<max && listaBotones[aux][0]!=(int)'B'; aux++);
                bRobot.nextFromVec=aux;
          }
          boton++;
    }
    int time=oRobot.elapsedTime;
    if (bRobot.elapsedTime>time)
       return bRobot.elapsedTime;
    return time;
}

int main(int argc, char *argv[])
{
    if (argc<2) {
        printf("\n...input file needed...\r\n");
    system("PAUSE");
		exit(-1);
    }
    int T=-1, N=-1, P=100;
    FILE *outputF, *inputF;

    ifstream entrada(argv[1]); 
    ofstream salida("output.out");
    entrada >> T;
    cout << T << " casos de prueba." << endl;
    for (int j=1; j<=T; j++) {
          entrada >> N;
          cout << N << " botones." << endl;
          for (int i=0; i<N; i++) {
              char caracter=0;
              entrada >> caracter;
              listaBotones[i][0]=(int)caracter;
              entrada >> listaBotones[i][1];
              cout << (char) listaBotones[i][0] << " - " << listaBotones[i][1] << endl;
        }
        salida << "Case #" << j << ": " << calcularPasos(N) << endl;
    }
    
    
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
