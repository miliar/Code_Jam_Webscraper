#include <iostream>
#include <map>
#include <vector>

using namespace std;

/*
    QWERASDF - single half byte value. each char correspondes value [0 - 8]
*/

unsigned char encodeCombination( char val1, char val2 = '\0' ) {
    unsigned char ret = 0;

    switch ( val1 ) {
    case 'Q':
        ret = 0x01;
        break;
    case 'W':
        ret = 0x02;
        break;
    case 'E':
        ret = 0x03;
        break;
    case 'R':
        ret = 0x04;
        break;
    case 'A':
        ret = 0x05;
        break;
    case 'S':
        ret = 0x06;
        break;
    case 'D':
        ret = 0x07;
        break;
    case 'F':
        ret = 0x08;
        break;
    }

    switch ( val2 ) {
    case 'Q':
        ret |= 0x10;
        break;
    case 'W':
        ret |= 0x20;
        break;
    case 'E':
        ret |= 0x30;
        break;
    case 'R':
        ret |= 0x40;
        break;
    case 'A':
        ret |= 0x50;
        break;
    case 'S':
        ret |= 0x60;
        break;
    case 'D':
        ret |= 0x70;
        break;
    case 'F':
        ret |= 0x80;
        break;
    default:
        break;
    }

    return ret;
}

void clearCounts( int* counts, int count_size ) {
    for ( int i = 0; i < count_size; ++i ) {
        counts[i] = 0;
    }
}

int main( int argc, char** argv ) {
    int T, C, D, N;
    unsigned char combine_key;
    char combine_val;

    char base_elem, base_elem2, comb_elem;

    map<unsigned char, char> combinations;
    map<char, char> opposed;
    vector<char> elem_list;

    map<unsigned char, char>::iterator f_it;
    map<char, char>::iterator opp_it;
    vector<char>::iterator elem_it;

    unsigned char is_present;

    int base_elem_count = 8;
    int* elem_counts = new int[base_elem_count];

    cin >> T;

    for ( int i = 0; i < T; ++i ) {
        cin >> C;
        combinations.clear();
        for ( int j = 0; j < C; ++j ) {
            cin >> base_elem >> base_elem2 >> comb_elem;
            combine_key = encodeCombination( base_elem, base_elem2 );
            combinations.insert( pair<unsigned char, char>( combine_key, comb_elem ) );
            combine_key = encodeCombination( base_elem2, base_elem );
            combinations.insert( pair<unsigned char, char>( combine_key, comb_elem ) );
        }

        cin >> D;
        opposed.clear();
        for ( int j = 0; j < D; ++j ) {
            cin >> base_elem >> base_elem2;
            opposed.insert( pair<char, char>( base_elem, base_elem2 ) );
            opposed.insert( pair<char, char>( base_elem2, base_elem ) );
        }

        cin >> N;
        elem_list.clear();
        clearCounts( elem_counts, base_elem_count );

        for ( int j = 0; j < N; ++j ) {
            cin >> base_elem;
            if ( elem_list.size() > 0 ) {
                combine_key = encodeCombination( elem_list.back(), base_elem );
                f_it = combinations.find( combine_key );
                if ( f_it != combinations.end() ) {
                    combine_key = encodeCombination( elem_list.back() );
                    elem_counts[combine_key - 1]--;
                    elem_list.pop_back();
                    elem_list.push_back( f_it->second );
                    continue;
                }
                opp_it = opposed.find( base_elem );
                if ( opp_it != opposed.end() ) {
                    combine_key = encodeCombination( opp_it->second );
                    if ( elem_counts[combine_key - 1] > 0 ) {
                        elem_list.clear();
                        clearCounts( elem_counts, base_elem_count );
                        continue;
                    }
                }
            }

            combine_key = encodeCombination( base_elem );
            ++elem_counts[combine_key - 1];
            elem_list.push_back( base_elem );
        }



        cout << "Case #" << ( i + 1 ) << ": [";
        for ( elem_it = elem_list.begin(); elem_it != elem_list.end(); ) {
            cout << *elem_it;
            if ( ++elem_it != elem_list.end() ) {
                cout << ", ";
            } else {
                break;
            }
        }
        cout << "]\n";
    }
    return 0;
}
