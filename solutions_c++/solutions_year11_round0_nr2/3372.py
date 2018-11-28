#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
string inventory;
vector<int>oppositions[26];
int hasLetter[26];
//Just covering all bases:
bool hasCombo[26][26];
char combonations[26][26];
int convertChar(char X)
{
	return (int) (X-'A');
			
}
bool doCombos()
{
	bool done = false;
	int s = inventory.length();
	while (s>1)
	{
		if (not hasCombo[convertChar(inventory[s-1])][convertChar(inventory[s-2])])
		{
			break;
		}
		char n = combonations[convertChar(inventory[s-1])][convertChar(inventory[s-2])];
		hasLetter[convertChar(inventory[s-1])]--;
		hasLetter[convertChar(inventory[s-2])]--;
		hasLetter[convertChar(n)]++;
		inventory.erase(inventory.end()-1);
		inventory.erase(inventory.end()-1);
		inventory+=n;
		s--;
		done = true;
	}
	return done;
}
void bang(char last)
{
	for (int i = 0; i<oppositions[convertChar(last)].size();i++)
	{
		if (hasLetter[convertChar(oppositions[convertChar(last)][i])])
		{
			inventory.clear();
			for (int i = 0; i<26;i++)
				hasLetter[i] = false;
		}
	}
}

int main()
{
	int T;
	cin>>T;
	for (int q = 0; q<T;q++)
	{
		inventory.clear();
		for (int i = 0; i<26;i++)
		{
			oppositions[i].clear();
			hasLetter[i] = 0;
			for (int d = 0; d<26;d++)
				hasCombo[i][d] = false;
		}
		int C;
		cin>>C;
		for (int i = 0;i<C;i++)
		{
			char a,b,c;
			int ai,bi,ci;
			cin>>a>>b>>c;
			ai = convertChar(a);
			bi = convertChar(b);
			hasCombo[ai][bi] = true;
			hasCombo[bi][ai] = true;
			combonations[ai][bi] = c;
			combonations[bi][ai] = c;
		}
		int D;
		cin>>D;
		for (int i = 0;i<D;i++)
		{
			char a,b;
			int ai,bi;
			cin>>a>>b;
			ai = convertChar(a);
			bi = convertChar(b);
			oppositions[ai].push_back(b);
			oppositions[bi].push_back(a);
		}
		string order;
		int len;
		cin>>len;
		cin>>order;
		for (int i = 0; i<order.length();i++)
		{
			
			inventory.append(1,order[i]);
			hasLetter[convertChar(order[i])]++;
			if (not doCombos())
				bang(order[i]);
			//cout<<inventory<<endl;
		}
		cout<<"Case #"<<q+1<<": [";
		for (int i = 0; i<inventory.length()-1 and inventory.length()>1;i++)
		{
			cout<<inventory[i]<<", ";
		} 
		if (inventory.length()==0)
		{
			cout<<"]"<<endl;
			continue;
		}
		cout<<inventory[inventory.length()-1]<<"]"<<endl;
	}
	return 0;
}