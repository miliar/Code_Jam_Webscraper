#include <iostream>
#include <iomanip>
#include <cstring>
#include <vector>
#include <map>
#include <string>

int const N = 1110000;
double val[N];
int go[N][2];
int lines;
int cur, slot;
std::map <std::string, int> feature;
int feature_id = 0;
int name[N];
int cha[N];

char c;

void read_tree(int id)
{
    do
    {
	c = getchar();
    } while (c != '(');
    
    std::cin >> val[id];
    
    do
    {
	c = getchar();
    } while (c != ')' && !(c >= 'a' && c <= 'z'));
    
    if (c == ')')
    {
	c = 0;
	return;
    }
    
    std::string tmp = "";
    for (;;)
    {
	tmp += c;
	c = getchar();
	if (c < 'a' || c > 'z')
	    break;
    }
    
    if (feature.find(tmp) == feature.end())
	feature[tmp] = ++feature_id;
    name[id] = feature[tmp];
    
    go[id][0] = ++slot;
    read_tree(slot);
    go[id][1] = ++slot;
    read_tree(slot);

    while (c != ')') c = getchar();
    c = 0;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int t;
    std::cin >> t;
    for (int tt = 0; tt < t; tt++)
    {
	std::cin >> lines;
	cur = 0, slot = 0;
	feature_id = 0;
		
	memset(val,0,sizeof(val));
	feature.clear();
	memset(go, 0, sizeof(go));
	c = 0;
	read_tree(0);
		
	std::cin.ignore();
//	std::cin.ignore();
	    
	int n;
	std::cin >> n;
	std::cout << "Case #" << tt+1 << ":\n";
	for (int i = 0; i < n; i++)
	{
	    memset(cha,0,sizeof(cha));
	    std::string s;
	    int k;
	    std::cin >> s;
	    std::cin >> k;
	    for (int j = 0; j < k; j++)
	    {
		std::cin >> s;
		cha[feature[s]] = 1;
	    }
	    
	    cur = 0;
	    double res = val[0];
	    while (go[cur][0])
	    {
		if (cha[name[cur]])
		    cur = go[cur][0];
		else
		    cur = go[cur][1];
		    
		res *= val[cur];
	    }
	    
	    std::cout << std::fixed << std::setprecision(7) << res << "\n";
	}
    }
    return 0;
}
