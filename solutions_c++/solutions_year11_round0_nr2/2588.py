#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <sstream>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define pb push_back

using namespace std;

bool op[26][26];
char tr[26][26];
vector<char> deck;

bool f_tr()	{
	int s = deck.size() -1;
	if (s >= 1)	{
		if (tr[deck[s] - 'A'][deck[s-1] - 'A'] != '\0')	{
			deck[s-1] = tr[deck[s] - 'A'][deck[s-1] - 'A'];
			deck.erase(deck.end() - 1);
			return true;
		}
	}
	return false;
}

void f_op()	{
	char c = deck[deck.size() -1];
	forp(0,deck.size(),i)	{
		if (op[c - 'A'][deck[i] - 'A'])	{
			deck.clear();
			return;
		}
	}
}

int main()	{
	
	int t;
	cin >> t;
	forp(0,t,z)	{
	
		forp(0,26,i) forp(0,26,j)	{
			op[i][j] = false;
			tr[i][j] = '\0';
		}
		deck.clear();
		
		int c,d,n;
		cin >> c;
		forp(0,c,i)	{
			char a,s,f;
			cin >> ws >> a >> ws >>  s >> ws >> f;
			tr[a - 'A'][s - 'A'] = tr[s - 'A'][a - 'A']= f;
		}
		
		cin >> d;
		forp(0,d,i)	{
			char a,s;
			cin >> ws >> a >> ws >> s;
			op[a - 'A'][s - 'A'] = op[s - 'A'][a - 'A'] = true;
		}
		
		cin >> n;
		forp(0,n,i)	{
			char a;
			cin >> ws >>  a;
			deck.pb(a);
			while (f_tr());
			f_op();
		}
		
		cout << "Case #" << (z+1) << ": [";
		forp(0,deck.size(),i)	{
			if (i != 0) cout << ", ";
			cout << deck[i];
		}
		cout << "]" << endl;
	}
}