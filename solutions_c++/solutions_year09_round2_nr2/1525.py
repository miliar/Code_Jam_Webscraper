#include<iostream>
#include<string>
using namespace std;
#define N_len 10

string s;
int str[N_len], a[N_len], definition[10], redefinition[10];
int D[10], base=0, T;

void Increment()
{
	++a[N_len-1];
	for(int i=N_len-1; i>=0; --i)
		if (a[i]==base)
		{
			a[i]=0;
			++a[i-1];
		}
}

bool IsNext()
{
	int D2[N_len];
	for(int i=0; i<N_len; ++i) D2[i] = 0;
	for(int i=0; i<N_len; ++i)
	{
		D2[a[i]]++;
	}
	D2[0] = 0;
	bool b = true;
	for(int i=1; i<10; ++i)
	{
		if (D[i]!=D2[definition[i]]) b = false;
	}
	return b;
}
void main()
{
	freopen("B-Small.in", "r", stdin);
	freopen("B-Small.out", "w", stdout);
	cin >> T;
	for(int t=0; t<T; ++t)
	{
		cin >> s;
		int len=s.length();
		for(int i=0; i<N_len; ++i)
			str[i]=0;
		for(int i=0; i<len; ++i)
		{
			str[N_len-len+i]=s[i] - '0';
		}
		for(int i=0; i<10; ++i)
		{
			D[i]=0;
		}
		for(int i=0; i<N_len; ++i)
		{
			++D[str[i]];
		}
		base = 0;
		for(int i=0; i<10; ++i)
		{
			definition[i] = 0;
			redefinition[i] = 0;
		}
		for(int i=1; i<10; ++i)
		{
			if (D[i]>0) 
			{
				++base;
				definition[i] = base;
				redefinition[base] = i;
			}
		}
		base++;
		for(int i=0; i<N_len; ++i)
		{
			a[i] = definition[str[i]];
		}
		
		Increment();
		while(!IsNext()) 
			Increment();
		int pos = 0;
		while ((pos<N_len-1)&&(a[pos]==0)) ++pos;
		cout << "Case #" << t+1 << ": ";
		for(int i=pos; i<N_len; ++i)
		{	
			cout << redefinition[a[i]];
		}
		cout << endl;
	}
}