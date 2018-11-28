#include <vector>
#include <deque>
#include <cstdio>
#include <iostream>

using namespace std;

int main ()
{
    int N, T;
    int next_orange, next_blue, cur_orange, cur_blue;
    int moved_orange, moved_blue;
    int move_to, ans;
    deque<int> orange_moves, blue_moves;
    deque<pair<int, int> > both_moves;
    pair<int, int> move_pair;
    string color;

    cin >> T;

    for (int t = 0; t < T; ++t) {
        cin >> N;

        for (int i = 0; i < N; ++i) {
            cin >> color >> move_to;

            if (color == "B") {
                blue_moves.push_back (move_to);
                both_moves.push_back (make_pair (1, move_to));
            } else {
                orange_moves.push_back (move_to);
                both_moves.push_back (make_pair (0, move_to));
            }


        }


        ans = 0;
        next_orange = next_blue = -1;
        cur_orange = cur_blue = 1;

        if (!blue_moves.empty ()) {
            next_blue = blue_moves.front ();
            blue_moves.pop_front ();
        } else {
            next_blue = 0;
        }

        if (!orange_moves.empty ()) {
            next_orange = orange_moves.front ();
            orange_moves.pop_front ();
        } else {
            next_orange = 0;
        }


        while (!both_moves.empty ()) {
            ++ans;
            move_pair = both_moves.front ();
            moved_blue = moved_orange = 0;


            if (move_pair.first) {
                if (cur_blue == move_pair.second) {
                    both_moves.pop_front ();

                    if (!blue_moves.empty ()) {
                        next_blue = blue_moves.front ();
                        blue_moves.pop_front ();
                        moved_blue = 1;
                    } else {
                        next_blue = 0;
                    }
                }
            } else {
                if (cur_orange == move_pair.second) {
                    both_moves.pop_front ();

                    if (!orange_moves.empty ()) {
                        next_orange = orange_moves.front ();
                        orange_moves.pop_front ();
                        moved_orange = 1;
                    } else {
                        next_orange = 0;
                    }

                }
            }


            if (next_blue && !moved_blue) {
                if (next_blue > cur_blue) {
                    ++cur_blue;
                } else if (next_blue < cur_blue) {
                    --cur_blue;
                }
            }

            if (next_orange && !moved_orange) {
                if (next_orange > cur_orange) {
                    ++cur_orange;
                } else if (next_orange < cur_orange) {
                    --cur_orange;
                }
            }
        }

        cout << "Case #" << (t + 1)  << ": " << ans << endl;
    }

    return 0;
}
