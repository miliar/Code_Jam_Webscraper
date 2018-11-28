#include <iostream>
#include<vector>
//#define entrada cin
#include<fstream>
//#include<string>
//#define salida cout

using namespace std;


ifstream entrada("A-small-attempt0.in");
//ofstream fout("salida.txt");
ofstream salida("A-small.out");


//void print(bool m[], int circuit, int l);

main(){

int cases, N, i, j;
long int K;
bool states[1000000] = {false};
int circuit, newcircuit;
//bool updated;

    entrada>>cases;
    //salida<<cases<<endl;


    for(i=0;i<cases;i++){

        circuit=1;
        newcircuit=1;

        entrada>>N;
//        fout<<"N:"<<N;

        entrada>>K;
//        fout<<" K:"<<K<<endl;

        for(j=0; j<N; j++){
            states[j] = false;
        }


        while(K>0){

            //updated = false;
            //newcircuit=N;

            for(j=0; j<circuit; j++){
                states[j] = !states[j];
            }

            j=0;
            circuit=1;
            while(j<N && states[j]){
                circuit=j+2;
                j++;
            }

            /*if( !updated ){

                    if( !states[j] ){
                        updated = true;
                        newcircuit = j+1;
                    }else{
                        newcircuit = j+2;
                    }

                }*/

            //if ( updated )
            //circuit = newcircuit;

            K--;
            //print(states, circuit, N);

        }

        if( (circuit) == (N+1) )
            salida<<"Case #"<<(i+1)<<": ON"<<endl;
        else
            salida<<"Case #"<<(i+1)<<": OFF"<<endl;

    }



}



/*void print(bool m[], int circuit, int l){
int i;

    //fout<<"(";
    for(i=0; i<l; i++){
        fout<<m[i]<<", ";

        if( circuit == (i+1) )
            fout<<"(), ";

    }


fout<<endl;
}*/
