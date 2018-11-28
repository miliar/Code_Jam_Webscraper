#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//初始化 
int n;
string row;
char a[4][4]; 
//标志位 
int nX = 0,nO = 0,nT = 0,nDot = 0; 
bool Xwon = false,Owon = false;

//判断是否赢
bool isWon()
{
	//判断
	if((nX==3&&nT==1)||(nX==4))
	{
		Xwon = true;
	}
	if((nO==3&&nT==1)||(nO==4))
	{
		Owon = true;
	}
	return (Xwon || Owon);
} 
//横
void searchRow()
{
	for(int i = 0;i<4;i++)
	{
		//初始化标志位 
		nX = 0;nO = 0;nT = 0;nDot = 0;
		for(int j = 0;j<4;j++)
		{
			switch(a[i][j])
			{
				case 'O':nO++;break;
				case 'X':nX++;break;
				case 'T':nT++;break;
				case '.':nDot++;break;
			}
		}
		//判断
		if(isWon()){
			break;
		}
	}	
}

//竖 
void searchCol()
{
	for(int j = 0;j<4;j++)
	{
		//初始化标志位 
		nX = 0;nO = 0;nT = 0;nDot = 0;
		for(int i = 0;i<4;i++)
		{
			switch(a[i][j])
			{
				case 'O':nO++;break;
				case 'X':nX++;break;
				case 'T':nT++;break;
				case '.':nDot++;break;
			}
		}
		//判断
		if(isWon()){
			break;
		}
	}	
}
//左斜
void searchLeftDiagonal()
{
	//初始化标志位 
	nX = 0;nO = 0;nT = 0;
	for(int i = 0,j = 0;i<4,j<4;i++,j++)
	{
		switch(a[i][j])
		{
			case 'O':nO++;break;
			case 'X':nX++;break;
			case 'T':nT++;break;
		}
	}
	//判断
	isWon(); 

}
//右斜
void searchRightDiagonal()
{
	//初始化标志位 
	nX = 0;nO = 0;nT = 0;
	for(int i = 0,j = 3;i<4,j>=0;i++,j--)
	{
		switch(a[i][j])
		{
			case 'O':nO++;break;
			case 'X':nX++;break;
			case 'T':nT++;break;
		}
	}
	//判断
	isWon();
}

//output
string outputRes()
{
	if(Xwon==false && Owon==false && nDot != 0)
 	{
	 	return "Game has not completed";
 	}else if(Xwon==false && Owon==false && nDot == 0)
 	{
	 	return "Draw";
 	}
    if(Xwon==true)
 	{
	 	return "X won";
 	}
 	if(Owon==true)
 	{
	 	return "O won";
 	}else{
	 	return "";
 	}	
}
void handle(int index)
{
	ofstream outfile;
	outfile.open("A-small-attempt0.out",ofstream::out | ofstream::app);
	outfile<<"Case #"<<index<<": ";
	//横
	searchRow();
	if(Xwon==true || Owon==true)
	{
		outfile<<outputRes()<<endl;
	}else{
		//竖 
		searchCol();
		if(Xwon==true || Owon==true)
		{
			outfile<<outputRes()<<endl;
		}else{
			//左斜
			searchLeftDiagonal();
			if(Xwon==true || Owon==true)
			{
				outfile<<outputRes()<<endl;
			}else{
				//右斜
				searchRightDiagonal();
				if(Xwon==true || Owon==true)
				{
					outfile<<outputRes()<<endl;
				}else{
					outfile<<outputRes()<<endl;
				}	
			}
		}
	}
	outfile.close();
}

int main()
{
	//输入
 	ifstream infile;
	infile.open("A-small-attempt0.in");   
	infile>>n;               
	for(int k = 0;k<n;k++)
	{
		//初始化标志位 
		Xwon = false,Owon = false;
		for(int i = 0;i<4;i++)
		{
			infile>>row;
			if(row.size() == 0) break;
			for(int j = 0;j<4;j++)
			{
				a[i][j] = row[j];
			}	
		}
		//handle
		handle(k+1);	
	}
	infile.close();
	
	return 0;
}