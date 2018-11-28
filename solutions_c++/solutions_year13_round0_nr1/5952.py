#include<iostream>
#include<string>
#include<fstream>


using namespace std;



char Equal(string line)
{
	char c, pc;
	pc = line[0];
	if(pc=='.')
		return 'N';
	if(pc=='T')
		pc = line[1];
	for(int i=1; i<4; i++)
	{
		c = line[i];
		if(c=='T')
			c = pc;
		if(c==pc && c!='.')
			continue;
		else
			return 'N';
	}
	if(c!='T')
		return c;
	return line[1];
}

int main()
{
	ifstream inpFile;
	inpFile.open("input.txt");
	ofstream outFile;
	outFile.open("output.txt");
	int T;
	inpFile>>T;
	for(int i=0; i<T; i++)
	{
		string line[4];
		bool won = false;
		for(int j=0; j<4; j++)
		{
			inpFile>>line[j];
		}
		
		for(int j=0; j<4; j++)
		{
			//horizontal
			char temp = Equal(line[j]);
			if(temp!='N')
			{
				outFile<<"Case #"<<i+1<<": "<<temp<<" won"<<endl;
				won = true;
				break;
			}
			//vertical
			string ts = "";
			ts += line[0][j];
			ts += line[1][j];
			ts += line[2][j];
			ts += line[3][j];

			temp = Equal(ts);
			if(temp!='N')
			{
				outFile<<"Case #"<<i+1<<": "<<temp<<" won"<<endl;
				won = true;
				break;
			}
		}
		if(!won)
		{
			//cross
			string ts = "";
			ts += line[0][0];
			ts += line[1][1];
			ts += line[2][2];
			ts += line[3][3];
			char temp = Equal(ts);
			if(temp!='N')
			{
				outFile<<"Case #"<<i+1<<": "<<temp<<" won"<<endl;
				won = true;
				continue;
			}

			ts = "";
			ts += line[0][3];
			ts += line[1][2];
			ts += line[2][1];
			ts += line[3][0];
			temp = Equal(ts);
			if(temp!='N')
			{
				outFile<<"Case #"<<i+1<<": "<<temp<<" won"<<endl;
				won = true;
				continue;
			}
		}

		if(!won)
		{
			bool flag = false;
			for(int ii=0; ii<4; ii++)
			{
				for(int j=0; j<4; j++)
				{
					if(line[ii][j]=='.')
					{
						outFile<<"Case #"<<i+1<<": Game has not completed"<<endl;
						flag = true;
						break;
					}
				}
				if(flag)
					break;
			}
			if(!flag)
				outFile<<"Case #"<<i+1<<": Draw"<<endl;
		}
	}

}