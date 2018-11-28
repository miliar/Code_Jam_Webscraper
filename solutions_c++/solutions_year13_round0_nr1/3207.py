#include <string>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int test_win(string str);

string filename("ProblemA_Data_Big.txt");
int main()
{
	ifstream infile(filename.c_str());
	if (infile)
    {
		ofstream outfile((string("Output_")+filename).c_str());
		if (outfile)
		{
			// read the input file
			int T;
			infile>>T;
			string temp;
			getline(infile,temp);
			for (int icase = 1; icase <= T; icase++)
			{
				vector<string> board;
				
				int res = 0,nfullflag = 0,resflag = 0;
				for (int iline = 1; iline <= 4; iline++)
				{
					getline(infile, temp);
					board.push_back(temp);
					//cout << temp<<endl;
					// test each line
					res = test_win(temp);
					if (res == 1) {
						outfile<<"Case #"<<icase<<": X won\n";
						resflag = res;
					}else if (res == 2) {
						outfile<<"Case #"<<icase<<": O won\n";
						resflag = res;
					}else if (res == 3) {nfullflag = 1;}
				}
				getline(infile,temp);
				if (resflag == 1 || resflag == 2) {continue;}
			
				// test each column
				
				for (int icol = 0; icol < 4; icol++){
					string temp1;
					temp1 = temp1 + board[0][icol] + board[1][icol] + board[2][icol]+board[3][icol];
					res = test_win(temp1);
					if (res == 1) {
						outfile<<"Case #"<<icase<<": X won\n";
						break;
					}else if (res == 2) {
						outfile<<"Case #"<<icase<<": O won\n";
						break;
					}
				}
				
				if (res == 1 || res == 2) {continue;}
				
				// test diagonal
				string temp1;
				temp1 = temp1 + board[0][0]+board[1][1]+board[2][2]+board[3][3];
				res = test_win(temp1);
				
				if (res == 1) {
					outfile<<"Case #"<<icase<<": X won\n";
					continue;
				}else if (res == 2) {
					outfile<<"Case #"<<icase<<": O won\n";
					continue;
				}
				temp1 = "";
				temp1 = temp1 + board[3][0]+board[2][1]+board[1][2]+board[0][3];
				res = test_win(temp1);
				if (res == 1) {
					outfile<<"Case #"<<icase<<": X won\n";
					continue;
				}else if (res == 2) {
					outfile<<"Case #"<<icase<<": O won\n";
					continue;
				}
				
				if (nfullflag == 1) {
					outfile<<"Case #"<<icase<<": Game has not completed\n";
				}else{
					outfile<<"Case #"<<icase<<": Draw\n";
				}
				
			}
			
		}else{cout<<"Cannot create output file.\n"; return -1;}
    }else{cout<<"Cannot read the input file.\n"; return -1;}
	return 0;
}
int test_win(string str){
	int res=0;
	int count[4] = {0,0,0,0};
	for (int i = 0; i < 4; i++){
		switch (str[i]){
			case 'X': 
				count[0]++;
				break;
			case 'O':
				count[1]++;
				break;
			case 'T': 
				count[2]++;
				break;
			case '.':
				count[3]++;
				break;
		}
	}
	if (count[0] == 4 || (count[0]==3 && count[2] == 1))
	{res = 1;
	}else if (count[1] == 4 ||(count[1]==3 && count[2] == 1)){
		res = 2;
	}else if (count[3] >=1){
		res = 3;
	}
	return res;
}