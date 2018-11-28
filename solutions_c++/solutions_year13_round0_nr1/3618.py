#include <iostream>
#include <vector>

using namespace std;

typedef vector<char> Row;
typedef vector<Row> Field;


class LineChecker
{
public:
    LineChecker() :
        state(' '),
        empty_square_present(false)
    {
    }

    void add_square(char c)
    {
        switch (c) {
            case '.':
                state = 'D';
                empty_square_present = true;
                break;

            case 'X':
                if (state != 'O' && state != 'D')
                    state = 'X';
                else
                    state = 'D';
                break;

            case 'O':
                if (state != 'X' && state != 'D')
                    state = 'O';
                else
                    state = 'D';
                break;

            case 'T':
                break;
        }
    }

    char state;
    bool empty_square_present;
};

class TicTacToeTomek
{
public:
    void add_row(const Row &row)
    {
        field.push_back(row);
    }

    string status() const
    {
        bool empty_square_present = false;

        // Check rows
        for (int i = 0; i < 4; i++) {
            LineChecker line;
            for (int j = 0; j < 4; j++)
                line.add_square(field[i][j]);

            empty_square_present |= line.empty_square_present;
            if (line.state == 'X')
                return "X won";
            if (line.state == 'O')
                return "O won";
    }

        // Check cols
        for (int j = 0; j < 4; j++) {
            LineChecker line;
            for (int i = 0; i < 4; i++)
                line.add_square(field[i][j]);

            empty_square_present |= line.empty_square_present;
            if (line.state == 'X')
                return "X won";
            if (line.state == 'O')
                return "O won";
    }

        // Check diags
        LineChecker diag1, diag2;
        for (int i = 0; i < 4; i++) {
            diag1.add_square(field[i][i]);
            diag2.add_square(field[i][4 - i - 1]);

            empty_square_present |= diag1.empty_square_present;
            empty_square_present |= diag2.empty_square_present;
        }

        if (diag1.state == 'X' || diag2.state == 'X')
            return "X won";
        if (diag1.state == 'O' || diag2.state == 'O')
            return "O won";

        // If we get here, either draw or game has not completed
        if (empty_square_present)
            return "Game has not completed";
        else
            return "Draw";
    }


private:
    Field field;

};

int main()
{
    int T;      // number of cases
    cin >> T;
    for (int case_number = 1; case_number <= T; case_number++) {
        TicTacToeTomek game;

        // Load field
        for (int i = 0; i < 4; i++) {
            string s;
            cin >> s;
            Row row;
            for (int j = 0; j < 4; j++)
                row.push_back(s[j]);
            game.add_row(row);
        }

        // Solve test case
        string status = game.status();

        // Print results
        cout << "Case #" << case_number << ": " << status << "\n";
    }
}
