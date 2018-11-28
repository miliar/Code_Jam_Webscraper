#include <QVector>
#include <QTextStream>

const char CHAR_O = 'O';
const char CHAR_X = 'X';
const char CHAR_T = 'T';
const char CHAR_S = '.';
const int BSIZE = 4;
typedef char Board[BSIZE][BSIZE];

char checkLine(Board& board, int x, int y, int incrx, int incry)
{
    char ret = CHAR_T;
    for (int i = 0; i < BSIZE; ++i)
    {
        if (board[x][y] == CHAR_S || (ret != CHAR_T && board[x][y] != CHAR_T && ret != board[x][y]))
        {
            ret = CHAR_S;
            break;
        }
        if (board[x][y] != CHAR_T)
        {
            ret = board[x][y];
        }
        x += incrx;
        y += incry;
    }
    return ret;
}

bool hasSpace(Board& board)
{
    for (int i = 0; i < BSIZE; ++i)
    {
        for (int j = 0; j < BSIZE; ++j)
        {
            if (board[i][j] == CHAR_S)
            {
                return true;
            }
        }
    }
    return false;
}

char solve2(Board& board)
{
    char ch;
    for (int i = 0; i < BSIZE; ++i)
    {
        ch = checkLine(board, 0, i, 1, 0);
        if (ch != CHAR_S)
        {
            return ch;
        }
        ch = checkLine(board, i, 0, 0, 1);
        if (ch != CHAR_S)
        {
            return ch;
        }
    }
    ch = checkLine(board, 0, 0, 1, 1);
    if (ch != CHAR_S)
    {
        return ch;
    }
    ch = checkLine(board, 0, BSIZE - 1, 1, -1);
    if (ch != CHAR_S)
    {
        return ch;
    }
    return hasSpace(board) ? CHAR_S : CHAR_T;
}

QString solve(Board& board)
{
    switch (solve2(board))
    {
    case CHAR_O:
        return "O won";
    case CHAR_X:
        return "X won";
    case CHAR_T:
        return "Draw";
    case CHAR_S:
        return "Game has not completed";
    default:
        return "fail";
    }
}

int main(int argc, char *argv[])
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();
    for (int i = 0; i < T; ++i)
    {
        Board sample;
        for (int j = 0; j < BSIZE; ++j)
        {
            QString str = ins.readLine();
            for (int k = 0; k < BSIZE; ++k)
            {
                sample[j][k] = str[k].toAscii();
            }
        }
        ins.readLine();
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(sample) << endl;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
    }

    return 0;
}
