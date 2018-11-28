#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
int check(string str[]) {
//	for(int i = 0; i < 4; i++)
//	{
//		cout<<str[i]<<endl;
//	}
//	cout<<endl;
	for(int i = 0; i < 4; i++)
	{
//		cout<<str[i]<<endl;
		char refer = str[i][0];
		for(int k = 0;k < 4 && refer == 'T'; k++)
		{
			refer = str[i][k];
		}
		for(int j = 0; j < 4;j++)
		{
			if(j == 3 &&(refer == str[i][j] || str[i][j] == 'T'))
			{
				return refer == 'X';
			}
			if (str[i][j] == 'T') continue;
			if(refer != str[i][j] || str[i][j] == '.' ) break;
		}
	}
	for(int i = 0; i < 4; i++)
	{
		char refer = str[0][i];
		for(int k = 0;k < 4 && refer == 'T'; k++)
		{
			refer = str[k][i];
		}
		for(int j = 0; j < 4;j++)
		{
			if(j == 3 &&(refer == str[j][i] || str[j][i] == 'T'))
			{
				return refer== 'X';
			}
			if (str[j][i] == 'T') continue;
			if(refer != str[j][i]||str[j][i] == '.') break;
		}
	}
	char refer = str[0][0];
	for(int k = 0;k < 4 && refer == 'T'; k++)
	{
		refer = str[k][k];
	}
	for(int i = 0; i < 4; i++)
	{
		if (i == 3 && (refer == str[i][i] || str[i][i] == 'T'))
			return refer == 'X';
		if (str[i][i] == 'T') continue;
		if (refer != str[i][i] || str[i][i] == '.') break;
	}
	refer = str[3][0];
	for(int k = 0;k < 4 && refer == 'T'; k++)
	{
		refer = str[3-k][k];
	}
	for(int i = 0; i < 4; i++)
	{
//		cout<<i<<" "<<refer<<" ";
//		cout<<str[3-i][i]<<endl;
		if (i == 3 && (refer == str[3-i][i] || str[3-i][i] == 'T'))
			return refer == 'X';
		if (str[3-i][i] == 'T') continue;
		if(refer!= str[3-i][i] || str[3-i][i] == '.') break;
	}
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(str[i][j] == '.') return -1;
		}
	}
	return -2;
}
int main() {
    ifstream in("input.in");
    ofstream out("output.out");
    int T;
    in>>T;
    for (int x = 0; x < T; x++) {
		cout<<x<<endl;
        string str[4];
        for (int y = 0; y < 4; y++) {
            in>>str[y];
        }
        string tmp;
        //in>>tmp;
        int a = check(str);
        out<<"Case #"<<x+1<<": ";
        if (a>0) out<<"X won"<<endl;
        else if (a==-1)
            out<<"Game has not completed"<<endl;
        else if (a==-2)
            out<<"Draw"<<endl;
        else out<<"O won"<<endl;

    }
    return 0;
}
