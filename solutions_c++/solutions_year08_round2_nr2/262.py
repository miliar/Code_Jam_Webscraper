#include <map>
#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const int END = 1001;
int tab [ END + 1];
char buf1 [ 1024];
bool fact [ 1002][1002];
char buf [ 1024];
bool marked [ 1002];

int main(int argc, char *argv[])
{

    // GENERATES PRIMES UP TO END
    
    vector < int > primes;
    
    memset ( tab, 0, sizeof(tab));
    int current = 2;
    
    //cout << "tab[3] " << tab[3] << endl;
    while (current <= END) {
	int z = 2;
	for ( ; z*current <= END; z++)
		tab[z*current] = 1;
		
	current ++;	
	while (current <= END && tab[current] == 1)
		current ++;
	if (current > END)
		break;
	//cout << current << "=" << tab[current]<<" ";
    }
    
    for ( int i= 1; i <= END; i++)
    	if ( tab[i] == 0) {
    		primes.push_back ( i);
    	//	if ( i < 100)
    	//		cout << i << endl;
    	}	   
    // DONE
    //cout << primes.size() << endl;
    int testCases;
    cin >> testCases;

    for ( int testCase = 1; testCase <= testCases; testCase ++ ) {
       memset ( fact, 0, sizeof ( fact));
              memset ( marked, 0, sizeof ( marked));
       long long A, B, P;
       cin >> A >> B >> P;
       for ( long long x = A; x <= B; x++)
           for (int y = 0; y < primes.size() ; y++)
               if ( (x % primes[y]) == 0 && primes[y] >= P  ) {
                  fact [x-A][primes[y]] = true;
             //     cout << x << " | " << primes[y] << endl;
                  }
                  
        // go for it          
        //cout << fact [ 5] [3] << " " << fact[2][3] << " XXX " << endl;;
        long long count = 0;
        for ( int i = 0; i <= B - A; i++ ) {
            if ( ! marked [ i] ) {    
                marked [i] = true;; count ++;
                queue < long long > q;
                q.push ( i );
              //  cout << " leader: " << i + A;
                while ( ! q.empty () ) {
                      int cur = q.front();
                      q.pop();
                      for ( int j = 0; j <= B - A; j ++)
                          for ( int k = 0; k < 1001; k ++)    {
                             // if ( cur = 5 && j == 2 && k == 3)
                             //    cout << "sprawdz " << (! marked [j]) << (fact[i][k]) << (fact[j][k])   << endl; 
                              if ( (! marked [j]) && (fact[cur][k]) && (fact[j][k]) ) {
      //                           cout << " " << j +A;
                                 marked [j] = true;
                                 q.push ( j );
                              }
                              }    
                }
        //        cout << endl;
            } 
        }
        cout << "Case #" << testCase << ": "<<  count   << endl;
    }
    //cout << "done";

    
    
    return 0;
}
