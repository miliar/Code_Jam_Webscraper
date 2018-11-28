#include <iostream>
#include <fstream>
using namespace std;

const int DROW[4] = {-1, 0, 0, 1};
const int DCOL[4] = {0, -1, 1, 0};
const int ROW = 20;
const int COL = 20;
const int QSIZE = 100000;

ifstream fin("b_small.in");
ofstream fout("b_small.out");

int Row, Col;
int Board[ROW][COL];
int Visited[ROW][COL];
char sBoard[ROW][COL];
char SinkChar = 'a';

void do_bfs(int, int);

void bfs()
{
	memset(Visited, 0, sizeof Visited);
    memset(sBoard, 0, sizeof sBoard);
    //cout << "inited" << endl; 
    int r, c;
    for (r=0; r<Row; ++r) for (c=0; c<Col; ++c) {
        if (!Visited[r][c]) {
            //cout << "row: " << r << " col: " << c << endl; 
            do_bfs(r, c);
        }
    }
    //cout << "Visited: " << endl;
    //for (r=0; r<Row; ++r) {
        //for (c=0; c<Col; ++c) cout << Visited[r][c];
        //cout << endl;
    //}
}

inline bool inBoard(int row, int col) 
{
    return row >= 0 && row < Row && col >= 0 && col < Col;
}

int Queue[QSIZE][2], head, tail;

void fill_board(char ch)
{
    int i;
    for (i=0; i<tail; ++i) {
        int r = Queue[i][0];
        int c = Queue[i][1];
        Visited[r][c] = true;
        sBoard[r][c] = ch;
    }
}


void do_bfs(int sRow, int sCol)
{
    head = 0; tail = 0;
    int d, fhead = 0, ftail = 0;
    Queue[tail][0] = sRow;
    Queue[tail][1] = sCol;
    ++tail;
    char sink;
    bool ok = false;
    Visited[sRow][sCol] = true;
    //cout << "in do_bfs() " << endl;
    do {
        int row = Queue[head][0];
        int col = Queue[head][1];
        ++head;
        //cout << "row: " << row << " col: " << col << endl;
        int curAtt = Board[row][col];
        int mRow = row;
        int mCol = col;
        int lowest = curAtt;
        for (d=0; d<4; ++d) {
            int rr = row + DROW[d];
            int cc = col + DCOL[d];
            if (inBoard(rr, cc)) {
                if (Board[rr][cc] < lowest) {    
                    mRow = rr;
                    mCol = cc;
                    lowest = Board[rr][cc];
                }
            }
        }
        if (lowest < curAtt) {
            if (sBoard[mRow][mCol] > 0) {
                ok = true;
                sink = sBoard[mRow][mCol];
                //cout << "find sink: " << sink 
                //    << " row: " << mRow << " col: " << mCol << endl;
                //break;
            } else {
                Queue[tail][0] = mRow;
                Queue[tail][1] = mCol;
                ++tail;
            }
        }
    } while (head < tail);

    if (!ok) {
        //cout << "no sink, use SinkChar:" << SinkChar << endl; 
        sink = SinkChar;
        ++SinkChar;
    }
    fill_board(sink);
}

void output_board()
{
    int r, c;
    for (r=0; r<Row; ++r) {
        fout << sBoard[r][0];
        //printf("%c", sBoard[r][c]);
        for (c=1; c<Col; ++c) {
            fout << " " << sBoard[r][c];
            //printf(" %c", sBoard[r][c]);
        }
        fout << endl;
    }
}


int main()
{
	//freopen("b_small.in", "r", stdin);
    //freopen("b_small.out", "w", stdout);
	int testCases;
	fin >> testCases;
    //scanf("%d", &testCases);
	for (int tcase=1; tcase<=testCases; ++tcase) {
        SinkChar = 'a';
		//scanf("%d%d", &Row, &Col);
        fin >> Row >> Col;
        //cout << "row: " << Row << " col: " << Col << endl;
		int r, c;
		for (r=0; r<Row; ++r) {
            for (c=0; c<Col; ++c) {
			    //scanf("%d", &Board[r][c]);
                fin >> Board[r][c];
                //cout << "board: " << Board[r][c] << endl;
            }
		}
        
		bfs();
        //printf("Case #%d:\n", tcase);
        fout << "Case #" << tcase << ":" << endl;
        output_board();
	}

	return 0;
}
