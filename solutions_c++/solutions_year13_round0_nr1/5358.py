#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//��ʼ�� 
int n;
string row;
char a[4][4]; 
//��־λ 
int nX = 0,nO = 0,nT = 0,nDot = 0; 
bool Xwon = false,Owon = false;

//�ж��Ƿ�Ӯ
bool isWon()
{
	//�ж�
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
//��
void searchRow()
{
	for(int i = 0;i<4;i++)
	{
		//��ʼ����־λ 
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
		//�ж�
		if(isWon()){
			break;
		}
	}	
}

//�� 
void searchCol()
{
	for(int j = 0;j<4;j++)
	{
		//��ʼ����־λ 
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
		//�ж�
		if(isWon()){
			break;
		}
	}	
}
//��б
void searchLeftDiagonal()
{
	//��ʼ����־λ 
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
	//�ж�
	isWon(); 

}
//��б
void searchRightDiagonal()
{
	//��ʼ����־λ 
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
	//�ж�
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
	//��
	searchRow();
	if(Xwon==true || Owon==true)
	{
		outfile<<outputRes()<<endl;
	}else{
		//�� 
		searchCol();
		if(Xwon==true || Owon==true)
		{
			outfile<<outputRes()<<endl;
		}else{
			//��б
			searchLeftDiagonal();
			if(Xwon==true || Owon==true)
			{
				outfile<<outputRes()<<endl;
			}else{
				//��б
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
	//����
 	ifstream infile;
	infile.open("A-small-attempt0.in");   
	infile>>n;               
	for(int k = 0;k<n;k++)
	{
		//��ʼ����־λ 
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