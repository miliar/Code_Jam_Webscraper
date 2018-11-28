#include<fstream>
using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("input.txt");
	out.open("output.txt");
	int num_of_case;
	in >> num_of_case;
	for(int i=0; i<num_of_case; i++)
	{
		char a[17];
		bool flag = false;
		for(int j=0; j<16; j++)
			in >> a[j];
		for(int j=0; j<4; j++)
		{
			if(a[j*4] == a[j*4+1] && a[j*4+1] == a[j*4+2] && a[j*4+2] == a[j*4+3] && a[j*4] == 'X')//in row
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j*4] == a[j*4+1] && a[j*4+1] == a[j*4+2] && a[j*4+3] == 'T' && a[j*4] == 'X')//in row
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j*4] == a[j*4+1] && a[j*4+2] =='T' && a[j*4+1] == a[j*4+3] && a[j*4] == 'X')//in row
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j*4] == a[j*4+2] && a[j*4+1] == 'T' && a[j*4+2] == a[j*4+3] && a[j*4] == 'X')//in row
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j*4] == 'T' && a[j*4+1] == a[j*4+2] && a[j*4+2] == a[j*4+3] && a[j*4+1] == 'X')//in row
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j] == a[j+4] && a[j+4] == a[j+8] && a[j+8] == a[j+12] && a[j] == 'X')//in column
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j] == a[j+4] && a[j+4] == a[j+8] && a[j+12] == 'T' && a[j] == 'X')//in column
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j] == a[j+4] && a[j+4] == a[j+12] && a[j+8] == 'T' && a[j] == 'X')//in column
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j] == a[j+8] && a[j+4] == 'T' && a[j+8] == a[j+12] && a[j] == 'X')//in column
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j] == 'T' && a[j+4] == a[j+8] && a[j+8] == a[j+12] && a[j+4] == 'X')//in column
			{
				out << "Case #" << i+1 << ": X won" << endl;
				flag = true;
				break;
			}
			if(a[j*4] == a[j*4+1] && a[j*4+1] == a[j*4+2] && a[j*4+2] == a[j*4+3] && a[j*4] == 'O')//in row
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
			if(a[j*4] == a[j*4+1] && a[j*4+1] == a[j*4+2] && a[j*4+3] == 'T' && a[j*4] == 'O')//in row
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
			if(a[j*4] == a[j*4+1] && a[j*4+2] =='T' && a[j*4+1] == a[j*4+3] && a[j*4] == 'O')//in row
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
			if(a[j*4] == a[j*4+2] && a[j*4+1] == 'T' && a[j*4+2] == a[j*4+3] && a[j*4] == 'O')//in row
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
			if(a[j*4] == 'T' && a[j*4+1] == a[j*4+2] && a[j*4+2] == a[j*4+3] && a[j*4+1] == 'O')//in row
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
			if(a[j] == a[j+4] && a[j+4] == a[j+8] && a[j+8] == a[j+12] && a[j] == 'O')//in column
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
			if(a[j] == a[j+4] && a[j+4] == a[j+8] && a[j+12] == 'T' && a[j] == 'O')//in column
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
			if(a[j] == a[j+4] && a[j+4] == a[j+12] && a[j+8] == 'T' && a[j] == 'O')//in column
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
			if(a[j] == a[j+8] && a[j+4] == 'T' && a[j+8] == a[j+12] && a[j] == 'O')//in column
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
			if(a[j] == 'T' && a[j+4] == a[j+8] && a[j+8] == a[j+12] && a[j+4] == 'O')//in column
			{
				out << "Case #" << i+1 << ": O won" << endl;
				flag = true;
				break;
			}
		}
		if(flag)continue;
		if(a[0] == a[5] && a[5] == a[10] && a[10] == a[15] && a[0] == 'X')//in diagonal
		{
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[0] == a[5] && a[5] == a[10] && a[15] == 'T' && a[0] == 'X')//in diagonal
		{	
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[0] == a[5] && a[5] == a[15] && a[10] == 'T' && a[0] == 'X')//in diagonal
		{	
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[0] == a[10] && a[5] == 'T' && a[10] == a[15] && a[0] == 'X')//in diagonal
		{	
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[0] == 'T' && a[5] == a[10] && a[10] == a[15] && a[5] == 'X')//in diagonal
		{	
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[0] == a[5] && a[5] == a[10] && a[10] == a[15] && a[0] == 'O')//in diagonal
		{
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if(a[0] == a[5] && a[5] == a[10] && a[15] == 'T' && a[0] == 'O')//in diagonal
		{	
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if(a[0] == a[5] && a[5] == a[15] && a[10] == 'T' && a[0] == 'O')//in diagonal
		{	
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if(a[0] == a[10] && a[5] == 'T' && a[10] == a[15] && a[0] == 'O')//in diagonal
		{	
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if(a[0] == 'T' && a[5] == a[10] && a[10] == a[15] && a[5] == 'O')//in diagonal
		{	
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if(a[3] == a[6] && a[6] == a[9] && a[9] == a[12] && a[3] == 'X')//in diagonal
		{
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[3] == a[6] && a[6] == a[9] && a[12] == 'T' && a[3] == 'X')//in diagonal
		{	
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[3] == a[6] && a[6] == a[12] && a[9] == 'T' && a[3] == 'X')//in diagonal
		{	
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[3] == a[9] && a[6] == 'T' && a[9] == a[12] && a[3] == 'X')//in diagonal
		{	
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[3] == 'T' && a[6] == a[9] && a[9] == a[12] && a[6] == 'X')//in diagonal
		{	
			out << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(a[3] == a[6] && a[6] == a[9] && a[9] == a[12] && a[3] == 'O')//in diagonal
		{
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if(a[3] == a[6] && a[6] == a[9] && a[12] == 'T' && a[3] == 'O')//in diagonal
		{	
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if(a[3] == a[6] && a[6] == a[12] && a[9] == 'T' && a[3] == 'O')//in diagonal
		{	
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if(a[3] == a[9] && a[6] == 'T' && a[9] == a[12] && a[3] == 'O')//in diagonal
		{	
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if(a[3] == 'T' && a[6] == a[9] && a[9] == a[12] && a[6] == 'O')//in diagonal
		{	
			out << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		bool flag2 = false;
		for(int j=0; j<16; j++)
		{
			if(a[j] == '.')
			{
				flag2 = true;
				break;
			}
		}
		if(flag2)
			out << "Case #" << i+1 << ": Game has not completed" << endl;
		else
			out << "Case #" << i+1 << ": Draw" << endl;
	}
	return 0;
}