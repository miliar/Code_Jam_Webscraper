//#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <fstream>
#include <utility>
#include <queue>

using namespace std ;

#define vi vector<int>
#define vvi vector< vi >
#define vvvi vector < vvi >

class state {
    public:
        int o_place, b_place, moves_made ;
};

int bfs(vector<pair<int,int> > & moves ) ;
bool within_bound( int a , int b ) ; 
ifstream cin("code.in");
ofstream cout("code.out");

//}
int main() {

    int T ;

    cin >> T ;

    for ( int i = 0 ; i < T ; i ++ ) {
        int N ;

        cin >> N ;

        vector<pair<int,int> > moves ;


        for ( int j = 0 ; j < N ; j ++ ) {

            char robot ;
            int id , position ;
            cin >> robot >> position ;
            pair<int,int> p ;

            if ( robot == 'O') id = 0 ;
            else id = 1 ;
            p.first = id ;
            p.second = position ;

            moves.push_back( p ) ;
        }
        cout<<"Case #"<<i+1<<": "<<bfs(moves)<<endl;
    }


    return 0 ;
}

int bfs(vector<pair<int,int> > & moves ) {
    
    vvvi dist = vvvi(105,vvi(105,vi(105,1073741824))) ;

    queue<state> q ;
    state start ;
    start.o_place = 1 ;
    start.b_place = 1 ;
    start.moves_made = 0 ;

    dist[ 1 ][ 1 ][ 0 ] = 0 ;

    q.push(start) ;
    int C[] = { -1, 1, 0 } ; 

    while ( !q.empty() ) {

        state tmp = q.front() ;
        q.pop() ;

        for ( int i = 0 ; i < 4 ; i ++ ) {
            for ( int j = 0 ; j < 4 ; j ++ ) {
                int o_nplace = 0 ;
                int b_nplace = 0 ;
                int move = tmp.moves_made ;
                if ( i <= 2 ) {
                    o_nplace = tmp.o_place + C[ i ] ;
                }

                else {
                    o_nplace = tmp.o_place ;
                }

                if ( j <= 2 ) {
                    b_nplace = tmp.b_place + C[ j ] ;
                }
		
		 
                else {
                    b_nplace = tmp.b_place ;
                }

		if ( !within_bound(o_nplace,b_nplace) ) continue ;

                if ( i == 3 && j == 3 ) {
                    if ( moves[ move ].first == 0 && moves[move].second == o_nplace ) {
                        if ( dist[ o_nplace ][ b_nplace ][ move + 1 ] > dist[ tmp.o_place ][ tmp.b_place ][ move ] + 1) {
                            state n ;
                            n.o_place = o_nplace ;
                            n.b_place = b_nplace ;
                            n.moves_made = move + 1 ;
			    dist[ o_nplace ][ b_nplace ][ move + 1 ] = dist[ tmp.o_place ][ tmp.b_place ][ move ] + 1 ; 

                            if ( n.moves_made <= moves.size() ) q.push(n) ;
                        }
                    }

		    if ( moves[ move ].first == 1 && moves[ move ].second == b_nplace ) {
			if ( dist[ o_nplace ][ b_nplace ][ move + 1 ] > dist[ tmp.o_place ][ tmp.b_place ][ move ] + 1 ) {
			    state n ; 
			    n.o_place = o_nplace ; 
                            n.b_place = b_nplace ;
			    n.moves_made = move + 1 ;
			    dist[ o_nplace ][ b_nplace ][ move + 1 ] = dist[ tmp.o_place ][ tmp.b_place ][ move ] + 1 ;
			    if ( n.moves_made <= moves.size() ) q.push( n ) ; 
			}
		     }
		}

		else if ( i == 3 ) {
		    if ( moves[ move ].first == 0 && moves[move].second == o_nplace ) {
                        if ( dist[o_nplace][b_nplace][ move + 1] > dist[ tmp.o_place ][ tmp.b_place ][ move ] + 1) {
                            state n ;
                            n.o_place = o_nplace ;
                            n.b_place = b_nplace ;
                            n.moves_made = move + 1 ;
			    dist[o_nplace][b_nplace][ move+1 ] = dist[tmp.o_place][tmp.b_place][move] + 1 ; 
                            if ( n.moves_made <= moves.size() ) q.push(n) ;
                        }
                    }    
		}

		else if ( j == 3 ) {
		    if ( moves[ move ].first == 1 && moves[ move ].second == b_nplace ) {
			if ( dist[o_nplace][b_nplace][ move + 1 ] > dist[tmp.o_place][tmp.b_place][move] + 1 ) {
			    state n ; 
			    n.o_place = o_nplace ; 
                            n.b_place = b_nplace ;
			    n.moves_made = move + 1 ;
			    dist[o_nplace][b_nplace][move+1] = dist[tmp.o_place][tmp.b_place][move] + 1 ;
			    if ( n.moves_made <= moves.size() ) q.push( n ) ; 
			}
		     }
		}

		else {
		    if ( dist[o_nplace][b_nplace][move] > dist[tmp.o_place][tmp.b_place][move] + 1 ) {
			dist[o_nplace][b_nplace][move] = dist[tmp.o_place][tmp.b_place][move] + 1 ;
			state n ; 
			n.o_place = o_nplace ; 
			n.b_place = b_nplace ; 
			n.moves_made = move ; 
			q.push(n);			
		    }	
		}
                       //dist[ o_nplace ][ b_nplace ][ moves+1 ] = min(dist[tmp.o_place][tmp.b_place][moves]+1,dist[ o_nplace ][ b_nplace ][ moves+1 ]) ;

            }
	}
    }

    int mins = 1073741824 ; 

    int sz = (int)moves.size() ; 

    for ( int i = 1 ; i <=101 ; i ++ ) {
	for ( int j = 1 ; j <= 101 ; j ++ ) {
	    mins = min(dist[i][j][sz],mins);
	}
    }

    return mins ;  
}

bool within_bound( int a , int b ) {
    if ( a >= 1 && a <= 100 && b >= 1 && b <= 100 ) return true ; 
    
    return false; 
}
