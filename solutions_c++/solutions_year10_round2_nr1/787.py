#include <stdio.h>
#include <string.h>

int MAX_VAL = 1000000;

int cas = 0;
int	T;
int n_ext, m_cr;

char ext[210][500];
char create[500];
int ans;

int getdir()
{
	int len = strlen(create);
	int i, j, k;
	int r = 0;
	for (i=0; i<len; i++)
	{
		if (create[i] == '/')
			r++;
	}
	return r;
}

int getSameDir(int a)
{
	int i, j, k;
	int r = 0;

	int len_a = strlen(ext[a]);
	int len_c = strlen(create);

	for (i=0; i<len_a && i < len_c; i++)
	{	
		if (ext[a][i] != create[i])	
		{
			return r - 1;
		}
		if (create[i] == '/' || ext[a][i] == '/')
			r++;								
	}
	if (len_a == i && create[i] == '/')
		return r;
	if (len_c == i && ext[a][i] == '/')
		return r;
	if (len_a == len_c)
		return r;

	return r - 1;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int i, j, k;

	scanf("%d", &T);
	//int sc = 0;
	while (T--)
	{
		memset(ext, 0, sizeof(ext));		
		scanf("%d %d", &n_ext, &m_cr);
		for (i=0; i<n_ext; i++)
		{
			scanf("%s", ext[i]);
			//ext[i][strlen(ext[i])] = '/';
		}

		ans = 0;
		for (i=0; i<m_cr; i++)
		{
			memset(create, 0, sizeof(create));
			scanf("%s", create);
			//create[strlen(create)] = '/';
		
			int n_dir = getdir();

			int max_dir = 0;
			for (j=0; j<n_ext; j++)
			{
				int t = getSameDir(j);
				if (t > max_dir)
					max_dir = t;
			}
			//printf("-- %d\n", max_dir);

			ans += n_dir - max_dir;
			strcpy(ext[n_ext], create);
			n_ext++;
		}		
		printf("Case #%d: %d\n", ++cas, ans);		
	}	
	return 0;
}