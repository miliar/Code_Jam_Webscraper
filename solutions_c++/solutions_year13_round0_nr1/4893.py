#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int anlyse(int num[], int i, int flag)
{
	int j,k,hor,vert, diag;
	for(j=0; j<4; j++)
	{
		hor = num[4*j] + num[4*j + 1] + num[4*j + 2] + num[4*j + 3];
		vert = num[j] + num[j+4] + num[j+8] + num[j+12];
		if(hor % 100 == 0)
			return 1;
		else if((hor%10==0) && hor < 100)
			return 2;
		if(vert % 100 == 0)
			return 1;
		else if((vert%10==0) && vert < 100)
			return 2;
	}
	diag = num[0] + num[5] + num[10] + num[15];
	if(diag % 100 == 0)
			return 1;
    else if((diag%10==0) && diag < 100)
			return 2;

	diag = num[3] + num[6] + num[9] + num[12];
	if(diag % 100 == 0)
			return 1;
    else if((diag%10==0) && diag < 100)
			return 2;

	if(flag>0)
		return 3;
	else
	    return 4;
}

void main()
{
	int i,j,k,res,flag,num[16];
	char tmp,game[16];
	ifstream ifile("A-large.in");
	ofstream ofile("output.txt");
	if (ifile.is_open())
	{
		ifile>>i;
		//ifile>>tmp;
		//i=i-48;
		cout<<i<<endl;
		//getline(ifile,line[0]);
		for(j=0;j<i;j++)
		{
			flag = 0;
			for(k=0; k<16; k++)
			{
			    ifile>>game[k];
				if(game[k] == 'X')
					num[k] = 100;
				else if(game[k] == 'O')
					num[k] = 10;
				else if(game[k] == 'T')
					num[k] = 0;
				else if(game[k] == '.') {
					num[k] = 3;
					flag++;
				}
				else
					cout<<"ERROR"<<endl<<endl;

				cout<<game[k];
				if((k+1)%4 == 0)
					cout<<endl;
			}
			cout<<endl;
			res =anlyse(num,16,flag);
			//ifile>>tmp;
			//cout<<tmp;
			if(res == 1)
				ofile<<"Case #"<<j+1<<": X won"<<endl;
			else if(res == 2)
				ofile<<"Case #"<<j+1<<": O won"<<endl;
			else if(res == 3)
				ofile<<"Case #"<<j+1<<": Game has not completed"<<endl;
			else if(res == 4)
				ofile<<"Case #"<<j+1<<": Draw"<<endl;
			else
				cout<<"Unknown Output"<<endl;
			//cout<<endl;
		}
	}
	cin>>tmp;
}