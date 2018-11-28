#include <iostream>
#include <fstream>
#include <vector>

using namespace std;



const int NSIZE = 2097152;
const int shift = NSIZE / 2;


                        
int tr[NSIZE*2+1];// mx in subtree;
int wh[NSIZE*2+1];
int tadd[NSIZE*2+1];
int l[NSIZE*2+1];
int r[NSIZE*2+1];



void Build()
{
	int i;
	for (i = NSIZE; i < 2*NSIZE; i++)
	{
		wh[i] = l[i] = r[i] = i - NSIZE;
	}
	for (i = NSIZE-1; i >= 1; i--)
	{
		l[i] = l[2*i];
		r[i] = r[2*i+1];
	}
}


void relax(int i)
{
	if(tadd[i] == 0) return;
	if (i >= NSIZE)
	{
		tadd[i] = 0;
	}
	else
	{
		tadd[2*i] += tadd[i];
		tadd[2*i+1] += tadd[i];
		tr[2*i] += tadd[i];
		tr[2*i+1] += tadd[i];
		tadd[i] = 0;
	}
}

void count(int i)
{
	if (i >= NSIZE)
	{
	 	wh[i] = i-NSIZE;
	 	return;
	}
	int j;
	if (tr[2*i] > tr[2*i+1])
		j = 2*i;
	else j = 2*i+1;
	tr[i] = tr[j];
	wh[i] = wh[j];
}



void Load()
{
	memset(tadd, 0, sizeof(tadd));
	memset(tr, 0, sizeof(tr));
	int c, p, v;
	cin >> c;
	int i;
	for (i = 0; i < c; i++)
	{
		cin >> p >> v;
		tr[p+shift+NSIZE] = v;
	}
	for (i = 2*NSIZE-1; i >= 1; i--)
	{
		count(i);
	}
                                                          
}



void add(int v, int ll, int rr, int c)
{
	relax(v);
	if (ll == l[v] && rr == r[v])
	{
		tr[v] += c;
		tadd[v] += c;
		return;
	}
	relax(2*v);
	relax(2*v+1);
	if (ll >= l[2*v+1])
	{
		add(2*v+1,ll,rr,c);
		count(v);
		return;
	}
	if (rr <= r[2*v])
	{
		add(2*v,ll,rr,c);
		count(v);
		return;
	}
	add(2*v,ll, r[2*v], c);
	add(2*v+1, l[2*v+1], rr, c);
	count(v);

}


long long f(int i)
{
		long long j = i / 2;
		return j*(j+1)*(2*j+1)/6;


}




void Solve()
{
	long long ans = 0;
	int i, j;
	while (tr[1] > 1)
	{
		i = tr[1];
		j = wh[1];
//		cerr << "mx = " << i << " in " << j - shift << "\n";

		
		ans += f(i);
		add(1, j, j, -i);
		if (i % 2)
		{
			add(1, j - i/2, j + i/2, 1);
		}
		else
		{
			add(1, j - i/2, j - 1, 1);
			add(1, j + 1, j + i/2, 1);

		}
	}
	cout << ans << "\n";
}



int main()
{
	int nt, tt;

//	Test();
//	return 0;

	cin >> nt;

	Build();
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
