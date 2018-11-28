#include <iostream>
#include <vector>
#include <utility>

using namespace std;

struct combine
{
	char a,b,c;
	combine() {}
	combine(char a, char b, char c) : a(a),b(b),c(c) {}
};

typedef pair<char,char> elim;
typedef vector<elim> VE;
typedef vector<combine> VC;

int main()
{
	ios_base::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		int C; cin>>C;
		VC Komb;
		for (int i=0; i<C; ++i)
		{
			char a,b,c;
			cin>>a>>b>>c;
			Komb.push_back(combine(a,b,c));
			Komb.push_back(combine(b,a,c));
		}

		int D; cin>>D;
		VE Elimin;
		for (int i=0; i<D; ++i)
		{
			char x,y; cin>>x>>y;
			Elimin.push_back(elim(x,y));
			Elimin.push_back(elim(y,x));
		}

		int Used[300]={};
		int N; cin>>N;
		vector<char> Napis;

		for (int i=0; i<N; ++i)
		{
			char zn; cin>>zn;
			Napis.push_back(zn);
			++Used[zn];

			while (true)
			{
				int siz=(int)Napis.size();
				if (siz<2) break;
				for (int i=0; i<2*C; ++i)
				{
					char a=Komb[i].a,b=Komb[i].b,c=Komb[i].c;
					if (a!=zn) continue;
					if (Napis[siz-2]==b)
					{
						Napis.pop_back();
						Napis.pop_back();
						Napis.push_back(c);
						--Used[a];
						--Used[b];
						++Used[c];
						continue;
					}
				}
				break;
			}
			for (int i=0; i<2*D; ++i)
			{
				char x=Elimin[i].first,y=Elimin[i].second;
				if (Napis.back()==x && Used[y]>0)
				{
					while (!Napis.empty())
					{
						--Used[Napis.back()];
						Napis.pop_back();
					}
					break;
				}
			}
		}
		cout<<"Case #"<<test<<": [";
		for (int i=0; i<(int)Napis.size()-1; ++i) cout<<Napis[i]<<", ";
		if (!Napis.empty()) cout<<Napis.back();
		cout<<']'<<endl;
	}
	return 0;
}
