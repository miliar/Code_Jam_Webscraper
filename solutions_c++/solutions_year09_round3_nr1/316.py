#include <iostream>
#include <string>
#include <set>

#define taskId "A"

using namespace std;

char dict[1000];
bool was[1000];

unsigned long long trans(char c)
{
	if ('0'<=c && c<='9') return c-'0';
	else return c - 'a' + 10;
}

unsigned long long solve(const string& input)
{
	set<char> alpha;
	
	for (int i=0; i<input.length(); i++)
		alpha.insert(input[i]);
	
	int base = max(alpha.size(), (size_t)2);
	
	string minIn;
	
	for (int i=0; i<1000; i++)
	{
		dict[i] = -1;
		was[i] = false;
	}
	
	minIn = "1";
	
	dict[input[0]] = '1';
	was['1'] = true;
	
	for (int i=1; i<input.length(); i++)
	{
		if (dict[input[i]] == -1)
		{
			bool find = false;
			
			for (char c = '0'; c<='9'; c++)
			{
				if (was[c] == false)
				{
					dict[input[i]] = c;
					was[c] = true;
					find = true;
					minIn += c;
					break;
				}				
			}
			
			if (find) continue;
			
			for (char c = 'a'; c <= 'z'; c++)
			{
				if (was[c] == false)
				{
					dict[input[i]] = c;
					was[c] = true;
					find = true;
					minIn +=c;
					break;
				}
			}
			
		}
		else
		{
			minIn += dict[input[i]];
		}
	}
	
	unsigned long long ans = 0;
	for (int i=0; i<minIn.length(); i++)
	{
		ans = ans * base + trans(minIn[i]);
	}
	return ans;
}

int main (int argc, char * const argv[])
{
	freopen(taskId"-large.in","r",stdin);
	freopen(taskId"-large.out","w",stdout);

	int n;
	cin >> n;
	for (int i=0; i<n; i++)
	{
		string input;
		cin >> input;
		unsigned long long ans = solve(input);
		cout << "Case #" << i + 1 << ": " << ans << '\n';
	}

    return 0;
}
