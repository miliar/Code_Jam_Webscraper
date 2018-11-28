#include <iostream>
#include <vector>
#include <queue>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <fstream>
using namespace std;


struct pt
{
	int W;
	int H;
};

pt noplace={-1,-1};

pt Npoint(pt M)
{
	pt up;
	up.H = M.H-1;
	if (up.H==-1)
	{
		return noplace;
	}
	up.W = M.W;
	return up;
}

pt Wpoint(pt M)
{
	pt W;
	W.H = M.H;
	W.W = M.W-1;
	if (W.W == -1)
	{
		return noplace;
	}
	return W;
}

pt Epoint(pt M,int W)
{
	pt E;
	E.H = M.H;
	E.W = M.W+1;
	if (E.W == W)
	{
		return noplace;
	}
	return E;
}

pt Spoint(pt M,int H)
{
	pt Sou;
	Sou.H = M.H+1;
	if (Sou.H == H)
	{
		return noplace;
	}
	Sou.W = M.W;
	return Sou;
}

pt check(pt M,pt N,pt W,pt E,pt Sou,int** mymap)
{
	pt A,B,C;
	int smallesta,smallestb,smallest;
	int NH,WH,EH,SouH;
	if (N.H == -1)
	{
		NH = 999999;
	}
	else
	{
		NH = mymap[N.H][N.W];
	}
	if (W.H == -1)
	{
		WH = 999999;
	}
	else
	{
		WH = mymap[W.H][W.W];
	}
	if (E.H == -1)
	{
		EH = 999999;
	}
	else
	{
		EH = mymap[E.H][E.W];
	}
	if (Sou.H == -1)
	{
		SouH = 999999;
	}
	else
	{
		SouH = mymap[Sou.H][Sou.W];
	}
	if (NH>WH)
	{
		smallesta = WH;
		A = W;
	}
	else
	{
		smallesta = NH;
		A = N;
	}
	if (EH>SouH)
	{
		smallestb = SouH;
		B = Sou;
	}
	else
	{
		smallestb = EH;
		B = E;
	}
	if (smallesta>smallestb)
	{
		smallest = smallestb;
		C = B;
	}
	else
	{
		smallest = smallesta;
		C = A;
	}
	if (smallest<mymap[M.H][M.W])
	{
		return C;
	}
	else
	{
		return M;
	}
}


int main()
{
	fstream f1("B-large.in");
	int T;
	f1>>T;
	vector<pt> road;
	vector<pt>sink;
	pt nextpoint;
	pt nowpoint;
	bool exisit = false;
	for (int m=0;m!=T;m++)
	{
		road.clear();
		sink.clear();
		int H,W;
		f1>>H>>W;
		int** m_pointer;
		char** mc_pointer;
		m_pointer =(int**) malloc(H*sizeof(int*));
		mc_pointer = (char**)malloc(H*sizeof(char*));
		for (int i=0;i!=H;i++)
		{
			m_pointer[i] = (int*)malloc(W*sizeof(int));
			mc_pointer[i] = (char*)malloc(W*sizeof(char));
		}
		for (int i=0;i!=H;i++)
		{
			for (int j=0;j!=W;j++)
			{
				f1>>m_pointer[i][j];
			}
		}
		for (int i=0;i!=H;i++)
		{
			for (int j=0;j!=W;j++)
			{
				nowpoint.H = i;
				nowpoint.W = j;
				road.clear();
				road.push_back(nowpoint);
				nextpoint = check(nowpoint,Npoint(nowpoint),
					Wpoint(nowpoint),Epoint(nowpoint,W),Spoint(nowpoint,H),m_pointer);
				while(nowpoint.H!=nextpoint.H||nextpoint.W!=nowpoint.W)
				{
					nowpoint = nextpoint;
					road.push_back(nowpoint);
					nextpoint = check(nowpoint,Npoint(nowpoint),
						Wpoint(nowpoint),Epoint(nowpoint,W),Spoint(nowpoint,H),m_pointer);
				}
				for (int q=0;q!=sink.size();q++)
				{
					if (road.back().H==sink[q].H&&road.back().W==sink[q].W)
					{
						exisit = true;
						break;
					}
				}
				if (exisit)
				{
					for (int q=0;q!=road.size();q++)
					{
						mc_pointer[road[q].H][road[q].W]=mc_pointer[road.back().H][road.back().W];
					}
					exisit = false;
				}
				else
				{
					sink.push_back(road.back());
					int num = sink.size();
					char flag = 'a'+num-1;
					mc_pointer[road.back().H][road.back().W] = flag;
					for (int q=0;q!=road.size();q++)
					{
						mc_pointer[road[q].H][road[q].W]=mc_pointer[road.back().H][road.back().W];
					}
					exisit = false;
				}
			}
		}
		ofstream f2("data.txt",ios::app);
		f2<<"Case #"<<m+1<<":"<<endl;
		for (int z=0;z!=H;z++)
		{
			for(int y=0;y!=W;y++)
			{
				f2<<mc_pointer[z][y]<<" ";
			}
			f2<<endl;
		}
		f2.close();

	}
	f1.close();
	return 0;
}