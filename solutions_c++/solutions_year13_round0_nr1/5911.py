#include<iostream>
#include<string>
#include<cmath>
#include<fstream>
using namespace std;

char whoWin(string line)
{
	if(line=="XXXX"||line=="TXXX"||line=="XTXX"||line=="XXTX"||line=="XXXT")return 'X';
	else if(line=="OOOO"||line=="TOOO"||line=="OTOO"||line=="OOTO"||line=="OOOT")return 'O';
	else return 'n';


}
int main()
{
	ifstream in("D://inl.in");
	ofstream out("D://outs.out");
	int t,z;
	in>>t;
	for(z=1;z<=t;z++)
	{
		string text;
		string rows[4];
		string cols[4];
		string ob[2];
		int j;
		for(j=0;j<4;j++)
		{
			in>>rows[j];
		}
		for(j=0;j<4;j++)
		{
			if(whoWin(rows[j])=='O'){text="O won";goto done;}
			else if(whoWin(rows[j])=='X'){text="X won";goto done;}
			cols[0]=cols[0]+rows[j][0];cols[1]=cols[1]+rows[j][1];cols[2]=cols[2]+rows[j][2];cols[3]=cols[3]+rows[j][3];
			ob[0]=ob[0]+rows[j][j];
			ob[1]=ob[1]+rows[j][3-j];
		}
	
		for(j=0;j<4;j++)
		{
			if(whoWin(cols[j])=='O'){text="O won";goto done;}
			else if(whoWin(cols[j])=='X'){text="X won";goto done;}
		}

		for(j=0;j<2;j++)
		{
			if(whoWin(ob[j])=='O'){text="O won";goto done;}
			else if(whoWin(ob[j])=='X'){text="X won";goto done;}
		}
		if(rows[0].find('.')>10 && rows[1].find('.')>10 && rows[2].find('.')>10 && rows[3].find('.')>10)text="Draw";
		else text="Game has not completed";



done:out<<"Case #"<<z<<": "<<text<<endl;

	}




	in.close();out.close();
	system("pause");return 0;
}