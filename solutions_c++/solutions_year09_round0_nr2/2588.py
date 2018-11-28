/*
Language:C++
*/

#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<iostream>

using namespace std;

typedef struct _point{
	int x;   
	int y;
}point;


char flow(int a,int b, vector<point>& trace,vector<vector<int> >& matrix,vector<vector<char> >& matrixL,int rowNum,int colNum)
{
	point pt;
	pt.x=a;
	pt.y=b;
	
	trace.push_back(pt);
	
	int up=10000,left=10000,right=10000,down=10000;
	
	if(a-1>=0) up=matrix[a-1][b];
	if(b-1>=0) left=matrix[a][b-1];
	if(b+1<colNum) right=matrix[a][b+1];
	if(a+1<rowNum) down=matrix[a+1][b];

//cout<<up<<","<<left<<","<<right<<","<<down<<endl;	

	if(up<matrix[a][b])
	{
		pt.x=a-1;
		pt.y=b;
	}
	
	if(left<matrix[a][b]&&left<up)
	{
		pt.x=a;
		pt.y=b-1;
	}
	
	if(right<matrix[a][b]&&right<up&&right<left)
	{
		pt.x=a;
		pt.y=b+1;
	}
	
	if(down<matrix[a][b]&&down<right&&down<left&&down<up)
	{
		pt.x=a+1;
		pt.y=b;
	}
//cout<<"tracking: "<<pt.x<<" ,"<<pt.y<<","<<matrixL[pt.x][pt.y]<<endl;
//cout<<(matrixL[pt.x][pt.y]!='`')<<endl;
	
	if((pt.x==a&&pt.y==b))
	{
		return matrixL[a][b];
	}else if(matrixL[pt.x][pt.y]!='`')
	{
		trace.push_back(pt);
		return matrixL[pt.x][pt.y];
	}else
	{
		return flow(pt.x,pt.y,trace,matrix,matrixL,rowNum,colNum);
	}
}


int main()
{
	ofstream fout("B-large.out");
	ifstream fin("B-large.in");

	int t;
	fin>>t;
	
	for(int i=0;i!=t;i++)
	{
	
		int h,w;
		fin>>h>>w;

		vector<int> row(w,10000);
		vector<char> l(w,'`');
		vector<vector<int> > matrix;
		vector<vector<char> > matrixL;
		

		for(int j=0;j!=h;j++)
		{
			for(int k=0;k!=w;k++)
			{
				fin>>row[k];
			}
			matrix.push_back(row);
			matrixL.push_back(l);
		}
		
		char now='`';
		vector<point> trace;
		
		for(int j=0;j!=h;j++)
		{
			for(int k=0;k!=w;k++)
			{
//cout<<j<<","<<k<<endl;
				if(matrixL[j][k]=='`')
				{

					char label=flow(j,k,trace,matrix,matrixL,h,w);
//cout<<"Source:  "<<j<<","<<k<<","<<label;
					if(label=='`')
					{

						now++;
						for(int m=0;m!=trace.size();m++)
						{
							matrixL[trace[m].x][trace[m].y]=now;
//cout<<trace[m].x<<","<<trace[m].y<<","<<now<<endl;
						}
					}else{
						for(int m=0;m!=trace.size();m++)
						{
							matrixL[trace[m].x][trace[m].y]=label;
//cout<<trace[m].x<<","<<trace[m].y<<","<<now<<endl;
						}
					}
					trace.clear();
				}

			}
		}

		fout<<"Case #"<<i+1<<":"<<endl;
		for(int j=0;j!=h;j++)
		{
			fout<<matrixL[j][0];
			for(int k=1;k!=w;k++)
			{
				//cout<<k<<","<<
				fout<<" "<<matrixL[j][k];
			}
			fout<<endl;
		}
	}
	return 0;
}