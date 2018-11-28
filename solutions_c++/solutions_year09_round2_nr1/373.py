# include <iostream>
# include <string>
# include <cstdio>
# include <algorithm>
# include <vector>
# include <queue>
# include <cstring>
# include <map>
# include <cmath>
# include <stack>

using namespace std;

# define vi vector < int >
# define vvi vector < vi >
# define For(i,n) for((int)i = 0; (int)i < (int)n; ++i)

char s[1000000];
int d[1000000];

double todouble(char *tiv)
{
//	cerr<<tiv<<"    ";
	int n = strlen(tiv);
	double ans = 0.0;
	double k = 10.0;
	bool p = true;
	for(int i = 0; i < n; ++i)
	{
		if(tiv[i]=='.')
		{
			p = false;
			continue;
		}
		if(p)
		{
			ans*=10.0;
			ans+=(double)(tiv[i] - '0');
		}
		else
		{
			ans += (double)(tiv[i] - '0')/k;
			k *= 10.0;
		}
	}
//	cerr<<ans<<endl<<endl;
	return ans;
}

double solv(int first, int last, char fut[110][15], int n, double ans)
{
	int i,j = 0,k = 0;
	bool p = true;
	char animal[20];
	char num[20];
	for(i = first; i <= last; ++i)
	{
		if(isdigit(s[i]) || s[i] == '.')
		{
			p = false;
			num[k++] = s[i];
		}
		else if(!p)
			break;
	}
	num[k] = '\0';
	ans *= todouble(num);
//	cerr<<ans<<endl;
	p = true;
	for(; i <= last; ++i)
	{
		if(s[i] == ')')
			return ans;
		if(isalpha(s[i]))
		{
			p = false;
			animal[j++] = s[i];
		}
		else if(!p)
			break;
	}
	animal[j] = '\0';

	int u,y;
	u = i;
	while(s[u]!='(')
		u++;
	
	y = d[u];
	while(s[y]!='(')
		y++;
	For(i,n)
	{
		if(strcmp(animal,fut[i]) == 0)
			return solv(u,d[u],fut,n,ans);
	}
	return solv(y,d[y],fut,n,ans);
}
int main ()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("AoutputL.out", "w", stdout);
	int t,k;
	char c;
	int m,i,j,h;
	int a;
	string zibil;
	char fut[110][15];
	stack <char> pak;
	stack <int> tiv;
	cin>>t;
	int n;
	For(k,t)
	{
		cout<<"Case #"<<k + 1<<": "<<endl; 
		cin>>n;
		m = 0;
		while(c!='(')
			c = getchar();
		s[m++] = c;
		tiv.push(m-1);
		pak.push('(');
		while(!pak.empty())
		{
			c = getchar();
			if(c == '(')
			{
				pak.push('(');
				tiv.push(m);
			}
			else if(c == ')')
			{
				d[tiv.top()] = m;
				tiv.pop();
				pak.pop();
			}
			if(c!='\n')
				s[m++] = c;
		}
		s[m] = '\0';
		cin>>a;
		For(i,a)
		{
			cin>>zibil;
			cin>>j;
			For(h,j)
				cin>>fut[h];
			printf("%.7lf\n", solv(0,m-1,fut,j,1.0));
		}
		
	}
	return 0;
}
