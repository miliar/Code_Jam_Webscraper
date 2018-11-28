#include <iostream>
using namespace std;

int n  , n_ , s , q , i , j , k , pos[100] , querie[1000] , troca;
string names[100] , aux;

int main( int argc , char** argv )
{
    cin >> n;
    for ( n_ = 1 ; n_ <= n ; n_++ )
    {
        cin >> s;
        getline ( cin, aux );
        for ( i = 0 ; i < s ; i++ )
            getline ( cin,  names[i] );
        
        cin >> q;
        getline ( cin,  aux );
        for ( i = 0 ; i < q ; i++ )
        {
            getline ( cin,  aux );
            j = 0;
            while ( names[j].compare(aux) )
                j++;
            querie[i] = j;
            
        }
        troca = -1;
        i = 0;
        do {
            //para cada name verifica qual é a posicao mais longe que ele chega apartir de i
            for ( j = 0 ; j < s ; j++ )
            {
                k = i;
                while (( querie[k] != j )&&( k < q ))
                    k++;
                pos[j] = k;
            }

            //verifica qual foi o ultimo valor, ou seja, maior distancia a partir do inicio
            k = 0;
            for ( j = 1 ; j < s ; j++ )
                if ( pos[j] > pos[k] )
                    k = j;
                    
            troca++;
            i = pos[k];
        } while ( i < q );
        
        cout << "Case #" << n_ << ": "<< troca << endl;
        //for ( i = 0 ; i < q ; i++ )
        //    cout << names[ querie[i] ] << endl;
    }
    return 0;
}
