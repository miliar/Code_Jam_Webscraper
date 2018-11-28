
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <set>

using namespace std;

int rotate_integer( int target, int biggest_power_of_ten )
{
    int low_digit = target%10;
    return (target/10) + low_digit*biggest_power_of_ten;
    
}

int main( int argc, char ** argv )
{
    fstream input_file;
    input_file.open( argv[1] );
    int num_lines;
    input_file >> num_lines;

   
    //string current_string;
    // Eat the line that had the number of lines
    //getline( input_file, current_string );

    for (int i=0; i<num_lines; i++)
    {
        int num_members;
        input_file >> num_members;
        int members[num_members];
        for (int j=0; j<num_members; j++)
        {
            input_file >> members[j];
        }
        map<int, int> sums;
        int sums_by_members[(1<<num_members)];
        int winner_1, winner_2;
        winner_1 = winner_2 = -1;
        for (int j=1; j<((1 << num_members)-1); j++)
        {
//cout << "j = " << j << endl;
            // get top bit
            int mask;
            int top_bit;
            for (top_bit = num_members; top_bit >= 0; top_bit--)
            {
                mask = (1 << top_bit);
                if (mask & j)
                {
                    break;
                }
            }
            int current_sum;
            if (mask == j)
            {
                current_sum = members[top_bit];
            }
            else
            {
                current_sum = members[top_bit] + sums_by_members[j-mask];
            }
            if (sums.count( current_sum ) == 0)
            {
                sums_by_members[j] = current_sum;
                sums[current_sum] = j;
            }
            else
            {
                winner_1 = j;
                winner_2 = sums[current_sum];
                break;
            }
        } 
            
        cout << "Case #" << i+1 << ":" << endl;
        // We have a match
        if (winner_1 > 0)
        {
            for (int bit_pos = 0; bit_pos < num_members; bit_pos++)
            {
                if ((1 << bit_pos) & winner_1)
                {
                    cout << members[bit_pos] << " ";
                }
            }
            cout << endl;
            for (int bit_pos = 0; bit_pos < num_members; bit_pos++)
            {
                if ((1 << bit_pos) & winner_2)
                {
                    cout << members[bit_pos] << " ";
                }
            }
            cout << endl;
        }
        else
        {
            cout << "Impossible";
        }
                
    }

    input_file.close();

    return 0;

}
