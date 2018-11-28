#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	char B[4][4];
	const int MAX = 100;
	char Buf[MAX];
	int T;
	cin >> T;
	cin.getline(Buf,MAX);
	int idx = 0;
	while(T--)
	{
		++idx;
		for(int i=0;i<4;++i)
		{
			scanf("%c%c%c%c\n",&B[i][0],&B[i][1],&B[i][2],&B[i][3]);
		/*	for(int j=0;j<4;++j)
				cin >> B[i][j];
			cin.getline(Buf,MAX);*/
		}
	//	cin.getline(Buf,MAX);
		/////////////////////////////
/*		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;++j)
				cout << B[i][j];
			cout << endl;
		}*/
		//////////////////////////////
		bool isO=false,isX=false,notF=false;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
			{
				switch(B[i][j])
				{
					case 'O':B[i][j]=0;break;
					case 'X':B[i][j]=1;break;
					case 'T':B[i][j]=2;break;
					case '.':B[i][j]=3;notF=true;break;
				}
			}
		int R[4];
		for(int i=0;i<4;++i)
		{
			R[0]=R[1]=R[2]=R[3]=0;
			for(int j=0;j<4;++j)
				++R[B[i][j]];
			if(R[2]==1)
			{
				if(R[0]==3)isO=true;
				else if(R[1]==3)isX=true;
			}
			else if(R[0]==4) isO=true;
			else if(R[1]==4) isX=true;
		}
		for(int j=0;j<4;++j)
		{
			R[0]=R[1]=R[2]=R[3]=0;
			for(int i=0;i<4;++i)
				++R[B[i][j]];
			if(R[2]==1)
			{
				if(R[0]==3)isO=true;
				else if(R[1]==3)isX=true;
			}
			else if(R[0]==4) isO=true;
			else if(R[1]==4) isX=true;
		}
		{
			R[0]=R[1]=R[2]=R[3]=0;
			for(int j=0;j<4;++j)
				++R[B[j][j]];
			if(R[2]==1)
			{
				if(R[0]==3)isO=true;
				else if(R[1]==3)isX=true;
			}
			else if(R[0]==4) isO=true;
			else if(R[1]==4) isX=true;
		}
		{
			R[0]=R[1]=R[2]=R[3]=0;
			for(int j=0;j<4;++j)
				++R[B[j][3-j]];
			if(R[2]==1)
			{
				if(R[0]==3)isO=true;
				else if(R[1]==3)isX=true;
			}
			else if(R[0]==4) isO=true;
			else if(R[1]==4) isX=true;
		}
		cout << "Case #"<<idx<<": ";
		if(isO)cout << "O won" << endl;
		else if(isX)cout << "X won" << endl;
		else if(notF)cout << "Game has not completed"<<endl;
		else cout << "Draw" << endl;
	}
	return 0;
}
