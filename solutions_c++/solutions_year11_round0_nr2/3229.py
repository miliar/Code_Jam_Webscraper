/*
 * Olaf "Ritave" Tomalka
 * GCJ 2011
 */
#include <iostream>
#include <vector>

static const char Rename[]={'Q','W','E','R','A','S','D','F'};

int Ren(char a)
{
	for (int i=0;i<sizeof(Rename);i++)
	{
		if (Rename[i]==a)
			return i;
	}
	return 9;
}

void DoTest()
{
	// Connections table
	char Tab[8][8];
	// Destroyment table
	bool DesTab[8][8];
	// Clear the table
	for (int i=0;i<8;i++)
	{
		for (int j=0;j<8;j++)
		{
			Tab[j][i]=0;
			DesTab[j][i]=false;
		}
	}

	int Comb,Destr,Elem;
	std::vector<char> V;

	std::cin >> Comb;
	// Populate the combination table
	for (int i=0;i<Comb;i++)
	{
		char a,b,c;
		std::cin >> a >> b >> c;
		int aR=Ren(a),bR=Ren(b);
		Tab[aR][bR]=c;
		Tab[bR][aR]=c;
	}

	std::cin >> Destr;
	// Populate the desturction table
	for (int i=0;i<Destr;i++)
	{
		char a,b;
		std::cin >> a >> b;
		int aR=Ren(a),bR=Ren(b);
		DesTab[aR][bR]=true;
		DesTab[bR][aR]=true;
	}

	std::cin >> Elem;
	// Process the fun
	for (int i=0;i<Elem;i++)
	{
		char a;
		std::cin >> a;
		if (!(V.empty()))
		{
			// If can be combined
			int aR=Ren(a),bR=Ren(V[V.size()-1]);
			if ((bR>=0 && bR<=8) && Tab[aR][bR])
				V[V.size()-1]=Tab[aR][bR];
			else
			{
				// Check for conflicting elements
				int s=V.size();
				bool Found=false;
				for (int j=0;j<s;j++)
				{
					int cR=Ren(V[j]);
					if ((cR>=0 && cR<=8) && DesTab[aR][cR]) // Found conflicting
					{
						V.clear();
						Found=true;
						break;
					}
				}
				// Not found anything, not collecting or destroying
				if (!Found)
					V.push_back(a);
			}
		} else
			V.push_back(a);
	}

	// Writeout
	int s=V.size();
	if (s==0)
		std::cout << "]\n";
	else
	{
		for (int i=0;i<s;i++)
		{
			std::cout << V[i];
			if (i==s-1)
				std::cout << "]\n";
			else
				std::cout << ", ";
		}
	}
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	int t;
	std::cin >> t;
	for (int i=0;i<t;i++)
	{
		std::cout << "Case #" << i+1 << ": [";
		DoTest();
	}
	std::cout << std::flush;
}
