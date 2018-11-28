#include <iostream>
#include <fstream>
using namespace std;

main()
{
	int i,j,k,m,n;
	int p,q;
	int T;
	int a;
	char KongGe[5];
	char temp1,temp2,temp3;
	char Square[4][4];
	ifstream infile("input");
	ofstream outfile("output",ios_base::app);
	infile>>T;
//cout<<N;
	for(i=0;i<T;i++)
	{
		outfile<<"Case #"<<i+1<<": ";
		for(j=0;j<4;j++)		
		{
			infile>>Square[j];
//cout<<Square[j]<<endl;
		}
//		infile>>KongGe;
/*		if((Square[0][0])==(Square[1][1])==(Square[2][2])==(Square[3][3])=='X')
		{
			outfile<<"X won"<<endl;
			break;
		}
		if((Square[0][0])==(Square[1][1])==(Square[2][2])==(Square[3][3])=='O')
		{
			outfile<<"O won"<<endl;
			break;
		}
*/
		for(j=0,k=0,p=0,q=0;j<4,k<4;j++,k++)			//判断【0】【0】子的斜线
		{
				if(Square[j][k]=='X')
				{
					p=p+1;
				}
				else if(Square[j][k]=='O')
				{
					q=q+1;
				}
				else if(Square[j][k]=='T')
				{
					p=p+1;
					q=q+1;
				}
				else
				{
					break;
				}
		}
		if((p==4)||(q==4))
		{
			if((Square[0][0]=='X')||(Square[1][1]=='X'))
			{
				outfile<<"X won"<<endl;
				goto p1;
			}
			else
			{
				outfile<<"O won"<<endl;
				goto p1;
			}
		}
		for(j=3,k=0,p=0,q=0;j>=0,k<4;j--,k++)			//判断【3】【0】子的斜线
		{
				if(Square[j][k]=='X')
				{
					p=p+1;
				}
				else if(Square[j][k]=='O')
				{
					q=q+1;
				}
				else if(Square[j][k]=='T')
				{
					p=p+1;
					q=q+1;
				}
				else
				{
					break;
				}
		}
		if((p==4)||(q==4))
		{
			if((Square[0][3]=='X')||(Square[1][2]=='X'))
			{
				outfile<<"X won"<<endl;
				goto p1;
			}
			else
			{
				outfile<<"O won"<<endl;
				goto p1;
			}
		}

		for(j=0;j<4;j++)		//判断第一行的子的列是不是4子
		{
			for(k=0,p=0,q=0;k<4;k++)
			{
				if(Square[k][j]=='X')
				{
					p=p+1;
				}
				else if(Square[k][j]=='O')
				{
					q=q+1;
				}
				else if(Square[k][j]=='T')
				{
					p=p+1;
					q=q+1;
				}
				else
				{
					break;
				}
			}
			if((p==4)||(q==4))
			{
				if((Square[0][j]=='X')||(Square[1][j]=='X'))
				{
					outfile<<"X won"<<endl;
					goto p1;
				}
				else
				{
					outfile<<"O won"<<endl;
					goto p1;
				}
			}
		}

		for(j=0;j<4;j++)		//判断第一列的子的各行是不是4子
		{
			for(k=0,p=0,q=0;k<4;k++)
			{
				if(Square[j][k]=='X')
				{
					p=p+1;
				}
				else if(Square[j][k]=='O')
				{
					q=q+1;
				}
				else if(Square[j][k]=='T')
				{
					p=p+1;
					q=q+1;
				}
				else
				{
					break;
				}
			}
			if((p==4)||(q==4))
			{
				if((Square[j][0]=='X')||(Square[j][1]=='X'))
				{
					outfile<<"X won"<<endl;
					goto p1;
				}
				else
				{
					outfile<<"O won"<<endl;
					goto p1;
				}
			}
		}

		for(j=0;j<4;j++)		//判断是否未完成
		{
			for(k=0;k<4;k++)
			{
				if(Square[j][k]=='.')
				{
					outfile<<"Game has not completed"<<endl;
					goto p1;
				}
			}
/*			if(Square[j][k]=='.')
			{
				break;
			}
*/
		}

		for(j=0,m=0;j<4;j++)		//判断是否是平局
		{
			for(k=0;k<4;k++)
			{
				if(Square[j][k]!='.')
				{
					m=m+1;
				}
			}
		}
		if(m==16)
		{
			outfile<<"Draw"<<endl;
		}
p1:
	continue;
	}

}
