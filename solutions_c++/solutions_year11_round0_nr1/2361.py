#include <iostream>
#include <fstream>

using namespace std;

const int MAX_N = 100;

#define DEBUG 0


int BlueTarget[MAX_N];
int OrangeTarget[MAX_N];
int TargetButton[MAX_N];
char TargetName[MAX_N];

int main()
{
    ifstream fin( "input.txt" );
    ofstream fout( "output.txt" );
    int T;
    fin >> T;
    for ( int t=0; t<T; t++ )
      {
        int N;
        fin >> N;
        int NOT = 0, NBT = 0;
        for ( int i=0; i<N; i++ )
          {
            fin >> TargetName[i] >> TargetButton[i];
            if ( TargetName[i] == 'O' )
              OrangeTarget[NOT++] = TargetButton[i];
            else if ( TargetName[i] == 'B' )
              BlueTarget[NBT++] = TargetButton[i];
            else
              {
                cout << "Input error\n";
                system( "PAUSE" );
              }    
          }
        
        if ( DEBUG )
          {
            for ( int i=0; i<N; i++ )
              {
                cout << TargetName[i] << " " << TargetButton[i] << ", ";
              } cout << "\n";
            cout << "Orange:\n";
            for ( int i=0; i<NOT; i++ )
              cout << OrangeTarget[i] << ", ";
            cout << "\n";
            cout << "Blue:\n";
            for ( int i=0; i<NBT; i++ )
              cout << BlueTarget[i] << ", ";
            cout << "\n";
            cout << "\n";
          }
        
        int time = 0;
        int OCPos = 1, BCPos = 1;
        int OCTar = 0, BCTar = 0;
        
        //cout << "time = " << time << ", OCPos = " << OCPos << ", BCPos = " << BCPos << "\n";
        for ( int i=0; i<N; i++ ) // per ogni bottone da premere, in ordine
          {
            int s, sa;
            if ( TargetName[i] == 'O' ) // se lo deve premere Orange...
              {
                // Orange si sposta sul suo target
                s = abs( OrangeTarget[OCTar] - OCPos ); // valore assoluto dello spostamento
                time += s+1; // aggiorna il tempo trascorso al momento in cui ha premuto il bottone dell'i-esimo obiettivo
                //cout << "Orange: target " << i << " ok at button " << OrangeTarget[OCTar] << ", time = " << time << "\n";
                OCPos = OrangeTarget[OCTar++];
                if ( BCTar < NBT )  // se Blue ha un prossimo obiettivo
                  {
                    // Blue si avvicina quanto può al suo prossimo obiettivo
                    sa = abs( BlueTarget[BCTar] - BCPos ); // spostamento desiderato da Blue!
                    if ( s+1 < sa )  // se il target di Blue è ancora troppo lontano si avvicina quanto puù
                      {
                        if ( BCPos < BlueTarget[BCTar] )
                          BCPos += s+1;
                        else
                          BCPos -= s+1;
                      }
                    else  // altrimenti ci va sopra (e aspetta)
                      BCPos = BlueTarget[BCTar];
                  } 
              }
            else // ( TargetName[i] == 'B' )
              {
                s = abs( BlueTarget[BCTar] - BCPos ); 
                time += s+1; // aggiorna il tempo trascorso al momento in cui ha premuto il bottone dell'i-esimo obiettivo
                //cout << "Blue: target " << i << " ok at button " << BlueTarget[BCTar] << ", time = " << time << "\n";
                BCPos = BlueTarget[BCTar++];
                sa = abs( OrangeTarget[OCTar] - OCPos );
                if ( OCTar < NOT )
                  {
                    if ( s+1 < sa ) 
                      {
                        if ( OCPos < OrangeTarget[OCTar] )
                          OCPos += s+1;
                        else
                          OCPos -= s+1;
                      }
                    else 
                      OCPos = OrangeTarget[OCTar];
                  }
              }
            //cout << "time = " << time << ", OCPos = " << OCPos << ", BCPos = " << BCPos << ", OCTar = " << OCTar << ", BCTar = " << BCTar << "\n";
            //system("PAUSE");
          }

        fout << "Case #" << t+1 << ": " << time << "\n";        
        
      } 
  
  fin.close();
  fout.close();
  if ( DEBUG ) system( "PAUSE" );
}
