#include<iostream> 
#include<cmath> 
#include<vector> 
#include<algorithm> 
#include<cstdio> 
#include<cstdlib> 
#include<string> 
#include<sstream> 
#include<map> 
#include<queue> 
#include<set> 
#define vi vector<int> 
#define vs vector<string> 

#define REP(i,n) for(int i=0;i<(int) n;i++) 
#define LL long long 
#define INF (2<<29) 

using namespace std;

int L, A, N;
string str;


int Index;
struct node
{
	int next1, next2;
	double p;
	string feature;
};

node Nodes[10000];
int calc(int pos)
{
	int cnt = 0;

	while(true)
	{
		if(str[pos] == '(') ++cnt;
		else if(str[pos] ==')') --cnt;
		if(cnt == 0) return pos;
		++pos;
	}
}
int parse(int x, int y)
{
	// cout << "X " << x << " " << y << endl;
	int pos;
	for(pos = x+1;;++pos)
	{
		if(str[pos] != ' ')
		{
			break;
		}
	}

	string num;
	for(;;++pos)
	{
		if(str[pos] == ' ' || str[pos] == ')')
		{
			break;
		}
		else
		{
			num += str[pos];
		}
	}
	
	istringstream in(num);
	
	double p;
	in >> p;

	while(str[pos] ==' ') ++pos;

	if(str[pos] == ')')
	{
		node nd;
		nd.next1 = -1;
		nd.next2 = -1;
		nd.p = p;
		nd.feature = "";
		Nodes[Index] = nd;
		++Index;
		
		return Index-1;
	}
	else
	{
		string feature;
		while(str[pos] != ' ')
		{
			feature += str[pos];
			++pos;
		}
		
		while(str[pos] == ' ')
		{
			++pos;
		}
		
		
		node nd;
		int idx = Index;
		++Index;
		int end1 = calc(pos);

		int next1 = parse(pos, end1);
		pos = end1 + 1;
		while(str[pos] ==' ') ++pos;

		int next2 = parse(pos, calc(pos));
		
		nd.next1 = next1;
		nd.next2 = next2;

		nd.p = p;
		nd.feature = feature;
		Nodes[idx] = nd;

		return idx;
	}
	return 0;
}

int main()
{
	int kases;
	cin >> kases;
	for(int kase = 1; kase <= kases; ++kase)
	{
		cin >> L;
		str = "";
		string c;
		getline(cin, c);
		REP(i, L)
		{
			getline(cin, c);
			str += c;
		}

		// cout << str << endl;
		
		Index = 0;
		parse(0, str.size()-1);
		
 		int animals;
		cin >> animals;
		cout << "Case #" << kase << ":\n";
		while(animals--)
		{
			string name;
			cin >> name;
			int CNT;
			cin >> CNT;
			set<string> fs;
			REP(i, CNT) { string S; cin >> S; fs.insert(S);}
			
			int IDX = 0;

			double prob = 1.0;
			while(1)
			{
				node nd = Nodes[IDX];
				prob *= nd.p;
				if(nd.next1 == -1)
				{
					printf("%.7lf\n", prob);
					break;
				}
				else
				{
					set<string>::iterator iter = fs.find(nd.feature);
					if(iter != fs.end())
					{
						IDX = nd.next1;
					}
					else
					{
						IDX = nd.next2;
					}
				}
			}
		}
		
		
		
	}
}
