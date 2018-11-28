#include <fstream>
#include <iostream>

using namespace std;
class status{
public:
	enum { X,O,Draw,Undefined,Unfinished};
};

int main()
{
	fstream in;
	fstream out;
	in.open("A-large.in", ios::in);
	out.open("output.out", ios::trunc|ios::out);

	int n;
	char board[4][4];

	in>>n;
	//cout<<n<<endl;
	for (int i = 0; i < n; ++i)
	{	
		//cout<<endl<<i;
		int status=status::Undefined;
		for (int j = 0; j < 4; ++j)
		{
			in.get(); // '/n'
			in.get(board[j][0]);
			in.get(board[j][1]);
			in.get(board[j][2]);
			in.get(board[j][3]);
			
			//cout<<endl;
			//cout<<j;
			//cout<<board[j][0];
			//cout<<board[j][1];
			//cout<<board[j][2];
			//cout<<board[j][3];
		}
		unsigned short DOT; // '.'
		DOT=0;
		// row
		//cout<<"examine row\n";
		for (int j = 0; j < 4; ++j)
		{
			unsigned short T,X,O;
			T=0; X=0, O=0;
			for (int k = 0; k < 4; ++k)
			{
				if (board[j][k]=='.') {DOT++; break;};
				if (board[j][k]=='T') T++;
				if (board[j][k]=='X') X++;
				if (board[j][k]=='O') O++;
			}
			if ((T+O)==4) {status=status::O; break;};
			if ((T+X)==4) {status=status::X; break;};
		}
		// column
		//cout<<"examine column\n";
		if (status==status::Undefined)
		{
			for (int j = 0; j < 4; ++j)
			{
				unsigned short T,X,O;
				T=0; X=0, O=0;
				for (int k = 0; k < 4; ++k)
				{
					if (board[k][j]=='.') {DOT++; break;};
					if (board[k][j]=='T') T++;
					if (board[k][j]=='X') X++;
					if (board[k][j]=='O') O++;
				}
				if ((T+O)==4) {status=status::O; break;};
				if ((T+X)==4) {status=status::X; break;};
			}
		}
		// cross
		//cout<<"examine \\ cross\n";
		if (status==status::Undefined)
		{
			unsigned short T,X,O;
			T=0; X=0, O=0;
			for (int j = 0; j < 4; ++j)
			{
				if (board[j][j]=='.') {DOT++; break;};
				if (board[j][j]=='T') T++;
				if (board[j][j]=='X') X++;
				if (board[j][j]=='O') O++;
			}
			if ((T+O)==4) {status=status::O; };
			if ((T+X)==4) {status=status::X; };
		}
		//cout<<"examine / cross\n";
		if (status==status::Undefined)
		{
			unsigned short T,X,O;
			T=0; X=0, O=0;
			for (int j = 0; j < 4; ++j)
			{
				if (board[j][3-j]=='.') {DOT++; break;};
				if (board[j][3-j]=='T') T++;
				if (board[j][3-j]=='X') X++;
				if (board[j][3-j]=='O') O++;
			}
			if ((T+O)==4) {status=status::O; };
			if ((T+X)==4) {status=status::X; };	
		}
		//cout<<"Case #"<<i+1<<endl;
		// Answer Section
		out<<"Case #"<<i+1<<": ";
		if (status==status::O)	{out<<"O won";};
		if (status==status::X)	{out<<"X won";};
		if (status==status::Undefined && DOT>0) {out<<"Game has not completed";};
		if (status==status::Undefined && DOT==0) {out<<"Draw";};
		out<<endl;
		// end of line;
		in.get();
	}
}