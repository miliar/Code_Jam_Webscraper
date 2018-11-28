#include <iostream>
//#include <string>
//#include <vector>
using namespace std;
const int L=110;
int aa[L], ad[L], ba[L], bd[L];
bool la[L], lb[L];

void sort(int taba[L], int tabb[L])
{
	int i, j;
	for (i=0; i<L; ++i)
		for (j=0; j<L; ++j)
			if (taba[i]<taba[j])
			{
				int tmp=taba[i];
				taba[i]=taba[j];
				taba[j]=tmp;
				tmp=tabb[i];
				tabb[i]=tabb[j];
				tabb[j]=tmp;
			}
}

int stoi(char s)
{
	return (int(s)-48);
}

void clean()
{
	int i;
	for (i=0; i<L; ++i)
	{
		aa[i]=1500;
		ad[i]=1500;
		ba[i]=1500;
		bd[i]=1500;
		la[i]=true;
		lb[i]=true;
	}
}

bool findt(int tab[L], bool tl[L], int t, int n)
{
	int i;
	for (i=0; i<n; ++i)
		if ((tab[i]<=t)&&(tl[i])&&(tab[i]!=1500)) 
		{
			tl[i]=false;
			return true;
		}
	return false;

}
int main()
{
	int N, T, j, i, o, a, b, ta, tb;
	char tmp[6];
	cin >> N;
	for (o=1; o<=N; ++o)
	{
		clean();
		cin >> T;
		cin >> a >> b;
		for (j=0; j<a; ++j)
			{
				scanf("%s", &tmp);
				aa[j]=(10*stoi(tmp[0])+stoi(tmp[1]))*60;
				aa[j]+=(10*stoi(tmp[3])+stoi(tmp[4]));
				scanf("%s", &tmp);
				ad[j]=(10*stoi(tmp[0])+stoi(tmp[1]))*60;
				ad[j]+=(10*stoi(tmp[3])+stoi(tmp[4]));
			}
		for (j=0; j<b; ++j)
			{
				scanf("%s", &tmp);
				ba[j]=(10*stoi(tmp[0])+stoi(tmp[1]))*60;
				ba[j]+=(10*stoi(tmp[3])+stoi(tmp[4]));
				scanf("%s", &tmp);
				bd[j]=(10*stoi(tmp[0])+stoi(tmp[1]))*60;
				bd[j]+=(10*stoi(tmp[3])+stoi(tmp[4]));
			}
		ta=0;
		tb=0;
		i=0;
		j=0;
		sort(aa, ad);
		sort(ba, bd);
		while ((i<a)||(j<b))
		{
			if (aa[i]<ba[j])
			{
				if (!findt(bd, lb, aa[i]-T, j)) ++ta;
				++i;
			}
			else
			{
				if (!findt(ad, la, ba[j]-T, i)) ++tb;
				++j;
			}
		}
		cout << "Case #" << o << ": " << ta << " " << tb << endl;
	}
	return 0;
}

