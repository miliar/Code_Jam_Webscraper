
#include <fstream>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

int n, m;
int t[100];
int a[100][100];
int b[100][100];
int ans[100];
int res;
int tmp[100];

void init()
{
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> t[i];
        for (int j = 0; j < t[i]; j++)
        {
            cin >> a[i][j] >> b[i][j];
        }
    }
    res = 1000;
}

void dfs(const int &x, const int &y)
{
    if (y >= res)
        return;
    if (x == n)
    {
        bool ok = true;
        for (int i = 0; i < m; i++)
        {
            bool f = false;
            for (int j = 0; j < t[i]; j++)
            {
                if (tmp[a[i][j]-1] == b[i][j])
                {
                    f = true;
                    break;
                }
            }
			if (!f)
			{
				ok = false;
				break;
			}
        }
        
        if (!ok)
            return;
        if (y < res)
        {
            for (int i = 0; i < n; i++)
                ans[i] = tmp[i];
			res = y;
        }
        return;
    }
    
    tmp[x] = 0;
    dfs(x+1, y);
    tmp[x] = 1;
    dfs(x+1, y+1);
}
        

int main()
{
    int c;
    cin >> c;
    for (int i = 0; i < c; i++)
    {
        init();
        dfs(0, 0);
        cout << "Case #" << i+1 << ":";
		if (res == 1000)
			cout << " IMPOSSIBLE";
		else
        for (int j = 0; j < n; j++)
            cout << " " << ans[j];
        cout<<endl;
    }
}
        
