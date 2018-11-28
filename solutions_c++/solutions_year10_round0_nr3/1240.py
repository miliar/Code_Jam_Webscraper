#include <iostream>
#include <string.h>

int main ( ) {

    int last_seen[1000];
    int earned_last_seen[1000];
    int number_in_group[1000];

    int number_of_cases, R, k, N, coins, round, index, prev_index, sum;

    std::cin >> number_of_cases;

    for ( int cse = 1; cse <= number_of_cases; cse++ ) {
        std::cin >> R >> k >> N;

        for ( int i = 0; i < N; i++ ) {
            std::cin >> number_in_group[i];
        }

        memset ( last_seen, -1, 1000 );
        memset ( earned_last_seen, 0, 1000 );

        coins = 0;
        round = 0;
        index = 0;

        last_seen[index] = round;
        earned_last_seen[index] = coins;

        bool try_shortcut = true;

        while ( round < R ) {
            round++;

            sum = 0;
            prev_index = index;

            while ( sum + number_in_group[index] <= k ) {
                sum += number_in_group[index++];

                if ( index == N)
                    index = 0;

                if ( index == prev_index )
                    break;
            }

            coins += sum;
            if (try_shortcut ) {
                if ( last_seen[index] == -1 ) {
                    last_seen[index] = round;
                    earned_last_seen[index] = coins;
                } else {
                    int rounds = round - last_seen[index];
                    int earnings = coins - earned_last_seen[index];

                    int shortcuts = (R - round) / rounds;

                    round += shortcuts * rounds;
                    coins += shortcuts * earnings; 

                    try_shortcut = false;
                }
            }
        }

        std::cout << "Case #" << cse << ": " << coins << std::endl;
    }

    return 0;
}
