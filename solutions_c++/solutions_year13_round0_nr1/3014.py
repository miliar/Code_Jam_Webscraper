#include <iostream>

int main ( void ) {

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(static_cast<std::ostream*>(nullptr));

    int c, i, j;
    int n_cases;
    char player;
    char map[4][4];
    bool o_won, x_won;
    bool game_completed;

    std::cin >> n_cases;

    for ( c = 1 ; c <= n_cases ; ++ c ) {

        o_won = x_won = false;
        game_completed = true;

        for ( i = 0 ; i < 4 ; ++ i ) {
            for ( j = 0 ; j < 4 ; ++ j ) {
                std::cin >> map[i][j];
                if ( map[i][j] == '.' ) {
                    game_completed = false;
                }
            }
        }

        // Horizontal
        for ( i = 0 ; i < 4 ; ++ i ) {
            if ( map[i][0] != '.' ) {
                player = map[i][0];
                for ( j = 0 ; j < 4 ; ++ j ) {
                    if ( player == 'T' ) {
                        player = map[i][j];
                    }
                    if ( map[i][j] != 'T' && player != map[i][j] ) {
                        player = '.';
                        break;
                    }
                }
                if( player != '.' ) {
                    if ( player == 'O' ) {
                        o_won = true;
                    }
                    else {
                        x_won = true;
                    }
                }
            }
        }

        // Vertical
        for ( j = 0 ; j < 4 ; ++ j ) {
            if ( map[0][j] != '.' ) {
                player = map[0][j];
                for ( i = 0 ; i < 4 ; ++ i ) {
                    if ( player == 'T' ) {
                        player = map[i][j];
                    }
                    if ( map[i][j] != 'T' && player != map[i][j] ) {
                        player = '.';
                        break;
                    }
                }
                if( player != '.' ) {
                    if ( player == 'O' ) {
                        o_won = true;
                    }
                    else {
                        x_won = true;
                    }
                }
            }
        }

        // Main diagonal
        if ( map[0][0] != '.' ) {
            player = map[0][0];
            for ( i = 0 ; i < 4 ; ++ i ) {
                if ( player == 'T' ) {
                    player = map[i][i];
                }
                if ( map[i][i] != 'T' && player != map[i][i] ) {
                    player = '.';
                    break;
                }
            }
            if ( player != '.' ) {
                if ( player == 'O' ) {
                    o_won = true;
                }
                else {
                    x_won = true;
                }
            }
        }

        // Anti diagonal
        if ( map[0][3] != '.' ) {
            player = map[0][3];
            for ( i = 0 ; i < 4 ; ++ i ) {
                if ( player == 'T' ) {
                    player = map[i][3 - i];
                }
                if ( map[i][3 - i] != 'T' && player != map[i][3 - i] ) {
                    player = '.';
                    break;
                }
            }
            if ( player != '.' ) {
                if ( player == 'O' ) {
                    o_won = true;
                }
                else {
                    x_won = true;
                }
            }
        }

        std::cout << "Case #" << c << ": ";
        if ( o_won ) {
            std::cout << "O won" << std::endl;
        }
        else if ( x_won ) {
            std::cout << "X won" << std::endl;
        }
        else if ( game_completed ) {
            std::cout << "Draw" << std::endl;
        }
        else {
            std::cout << "Game has not completed" << std::endl;
        }
    }

    return 0;
}
