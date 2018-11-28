// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
using namespace std;
ifstream in("A-large.in");
ofstream out("out.txt");

class Order
{
public:
	Order(int ord,int but):m_ord(ord),m_but(but){}
	int m_ord,m_but;
};

vector<Order> orders[2];

int Solve()
{
	int timepoLlegada[2];///hora a la que llega el robot a su proxima suborder
	int pos[2];///posicion fisica
	int subOrd[2];///proximo numero de suborden a ejecutar
	for(int i = 0;i < 2;++i)
	{
		pos[i] = 1;
		subOrd[i] = 0;
		timepoLlegada[i] = 0;
		if(!orders[i].empty())
		{
			timepoLlegada[i] = abs(pos[i]-orders[i][0].m_but);
			pos[i] = orders[i][0].m_but;
		}
	}
	int t = 0;///hora en la que el ultimo robot apreto boton
	while(subOrd[0] < orders[0].size() || subOrd[1] < orders[1].size())
	{
		///Cual sigue?
		int next;
		if(subOrd[0] < orders[0].size() && subOrd[1] < orders[1].size())
			next = orders[0][subOrd[0]].m_ord < orders[1][subOrd[1]].m_ord?0:1;
		else if(subOrd[0] < orders[0].size())
			next = 0;
		else
			next = 1;
		if(t < timepoLlegada[next])
			t = timepoLlegada[next]+1;///llego y apreto el boton
		else
			t++; 
		subOrd[next]++;
		if(subOrd[next] < orders[next].size())
		{
			timepoLlegada[next] = t+abs(pos[next]-orders[next][subOrd[next]].m_but);
			pos[next] = orders[next][subOrd[next]].m_but;
		}
	}
	return t;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	in >> T;
	for(int i = 0;i<T;++i)
	{
		int moves;
		in >> moves;
		orders[0].clear();
		orders[1].clear();
		for(int m = 0;m < moves;++m)
		{
			char r;
			int but;
			in >> r;
			in >> but;
			int robot = (r == 'O')?0:1;
			orders[robot].push_back(Order(m,but));
		}
		out << "Case #" << (i+1) << ": " << Solve() << endl;
	}
	return 0;
}

