#include <cmath>
#include <iostream>
using namespace std;

struct wpis
{
	int where_;
	int zysk;
};

int who(char znak)
{
	int out = 0;
	if(znak=='O') out = 1;
	return out;
}

int drugi(int kto)
{
	return (kto+1)%2;
}


#define LARGE
int main(int argc, char* argv[])
{
	
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif

#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif


	int T = 0;
	int N = 0;

	cin >> T;
	wpis robots[2];
	
	char kto;
	int where_ = 0;
	int czas = 0;	

	for(int i = 0 ; i< T ; i++)
	{
		czas = 0;
		robots[0].where_ = 1;
		robots[1].where_ = 1;
		robots[0].zysk = 0;
		robots[1].zysk = 0;

		cin >> N;
		while(N--)
		{
			cin >> kto;
			cin >> where_;

			int idKto = who(kto);
			int odleglosc = abs(robots[idKto].where_ - where_);
			int ilebedeszedl = odleglosc + robots[idKto].zysk; 
			if(ilebedeszedl < 0) ilebedeszedl = 0;

			robots[idKto].zysk=0;
			robots[idKto].where_ = where_;

			int czaspracy = ilebedeszedl+1;
			czas+= czaspracy;
			robots[drugi(idKto)].zysk-=czaspracy;
		}

		cout<<"Case #"<<i+1<<": "<<czas<<endl;
	}

	return 0;
}

