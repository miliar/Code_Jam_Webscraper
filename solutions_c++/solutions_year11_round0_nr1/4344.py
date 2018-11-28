#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	int T, N, P, Time;
	char R;
	int Bpos, Opos, BLast, OLast, Secuence;
	bool Bturn, Oturn, Bfin, Ofin, Bpushed, Opushed;
	vector<char> Rs;
	vector<int> Ps, Os, Bs;
	ifstream inFile( "A-large.in" );
	ofstream outFile( "A-large.txt" );

	inFile >> T;

	for(int i = 0; i < T; i++)
	{
		inFile >> N;
		Rs.clear();
		Os.clear();
		Bs.clear();
		for(int j = 0; j < N; j++)
		{
			inFile >> R >> P;
			Rs.push_back(R);
			if(R == 'O') Os.push_back(P); else Bs.push_back(P);
		}
		bool finish = false;
		Bturn = Oturn = false;
		Bpushed = Opushed = false;
		Ofin = Bfin = false;
		Time = 1;
		Bpos = Opos = 1;
		BLast = OLast = -1;
		Secuence = 0;
		while(!finish)
		{
			if(!Bturn&&!Oturn)
				if(Rs[Secuence]=='O') Oturn = true; else Bturn = true;

			if(Bs.size()>0)
			{
				if(!Bfin)
				{
					if(Bpos == Bs[BLast+1])//estoy en un boton?
					{
						if(Bturn)//es mi turno de apretar el boton?
						{
							BLast++;
							Secuence++;
							Bturn = false;
							Bpushed = true;
							if((BLast+1) < Bs.size())
								if(Rs[Secuence]=='O') Oturn = true; else Bturn = true;
							else
								Bfin = true;
								if(Secuence<Rs.size())							
									if(Rs[Secuence]=='O') Oturn = true; else Bturn = true;
						}
					}
					else
					{
						if((BLast+1) < Bs.size())//quedan botones para apretar?
							if(Bs[BLast+1]>Bpos)
								Bpos++;
							else
								Bpos--;
						else
							Bfin = true;
					}
				}
			}
			else
				Bfin = true;

			if(Os.size()>0)
			{
				if(!Ofin)
				{
					if(Opos == Os[OLast+1])//estoy en un boton?
					{
						if(Oturn&&!Bpushed)//es mi turno de apretar el boton?y el otro no apreto
						{
							OLast++;
							Secuence++;
							Oturn = false;
							if((OLast+1) < Os.size())
								if(Rs[Secuence]=='O') Oturn = true; else Bturn = true;
							else
								Ofin = true;
								if(Secuence<Rs.size())							
									if(Rs[Secuence]=='O') Oturn = true; else Bturn = true;
						}
					}
					else
					{
						if((OLast+1) < Os.size())//quedan botones para apretar?
							if(Os[OLast+1]>Opos)
								Opos++;
							else
								Opos--;
						else
							Ofin = true;
					}
				}
			}
			else
				Ofin = true;

			if(Ofin&&Bfin)
				finish = true;
			else
				Time++;

			Bpushed = false;
		}
		outFile << "Case #" << i+1 << ": " << Time << endl;
	}

	return 0;

}