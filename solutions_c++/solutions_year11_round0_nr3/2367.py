#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_N = 1000;
const int L = 20 + 1; // massima lunghezza in bit di un qualsiasi numero che può arrivare in ingresso

int table[MAX_N][L];  // ogni riga contiene la rappresentazione in base 2 di un numero in ingresso
int numOnes[L]; // numero di bit a 1 nelle colonne della matrice "table"

#define DEBUG 0


#define  MAX_LEVELS  1000
int beg[MAX_LEVELS], end[MAX_LEVELS];
bool quickSort(int *arr, int elements) {
  int  piv, i=0, L, R ;

  beg[0]=0; end[0]=elements;
  while (i>=0) {
    L=beg[i]; R=end[i]-1;
    if (L<R) {
      piv=arr[L]; if (i==MAX_LEVELS-1) return false;
      while (L<R) {
        while (arr[R]>=piv && L<R) R--; if (L<R) arr[L++]=arr[R];
        while (arr[L]<=piv && L<R) L++; if (L<R) arr[R--]=arr[L]; }
      arr[L]=piv; beg[i+1]=L+1; end[i+1]=end[i]; end[i++]=L; }
    else {
      i--; }}
  return true;
}



//vector<int> numbers(MAX_N);

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
        
        vector<int> numbers(N);
        
        for ( int i=0; i<N; i++ )
          fin >> numbers[i];
        
        for ( int i=0; i<N; i++ )
          for ( int j=0; j<L; j++ )
            table[i][j] = 0;
        for ( int j=0; j<L; j++ )
          numOnes[j] = 0;
        
        sort( numbers.begin(), numbers.end() );
        // ordina i numeri
        //quickSort(numbers,N);
        
        int minbit = 1; // numero minimo di bit necessari a rappresentare i numeri in "numbers"
        
        // converte in binario e riempie la tabella
        for ( int i=0; i<N; i++ )
          {
            int num = numbers[i];
            int bitPos = 0, bit;
            do
              {
                table[i][bitPos++] = num % 2;
                num >>= 1;
                if ( bitPos > minbit )
                  minbit = bitPos;
              }
            while ( num );
          }
        
        bool impossible = false;
        // calcola il numero di bit a 1 in ogni colonna e verifica la condizione necessaria e sufficiente
        for ( int j=0; j<minbit; j++ )
          {
            for ( int i=0; i<N; i++ )
              numOnes[j] += table[i][j];
            // verifica subito la condizione necessaria e sufficiente per la fattibilità
            if ( numOnes[j] % 2 == 1 )
              {
                impossible = true;
                //break; // a causa di questo break ovviamente l'array numOnes non è consistente! (ma chissene)
              }
          }        
        
        
        if ( DEBUG )
          {
            cout << "Posizione del bit più significativo = " << minbit << "\n";
            for ( int i=0; i<N; i++ )
              {
                for ( int j=L-1; j>=0; j-- )
                  cout << table[i][j] << " ";
                cout << "\n";
              }
            cout << "Somme:\n";
            for ( int j=L-1; j>=0; j-- )
              cout << numOnes[j] << " ";
            cout << "\n";
            for ( int i=0; i<N; i++ )
              {
                cout << numbers[i] << ", ";
              } cout << "\n";
            
            cout << "\n";
            
          }
        
        
        if ( impossible )  // se la condizione necessaria e sufficeinte non è verificata, non c'è nulla da fare
          {
                        if ( DEBUG ) { cout << "Impossibile\n"; system("PAUSE"); }
            fout << "Case #" << t+1 << ": NO\n";
            continue;
          }
        
        // se la condizione necessaria e sufficiente è soddisfatta Sean può prendersi tutte le caramelle tranne la più piccola
        int seanSum = 0;
        for ( int i=1; i<N; i++ )
          seanSum += numbers[i];
        
        if (DEBUG)
        {  
        cout << "Possibile: seanSum = " << seanSum << "\n";
        system( "PAUSE" ); }
        fout << "Case #" << t+1 << ": " << seanSum << "\n";    
      } 
  
  fin.close();
  fout.close();
  if ( DEBUG ) system( "PAUSE" );
}
