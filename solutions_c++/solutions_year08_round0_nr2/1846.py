#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>

using namespace std;

int match[256];
bool ck[256];
int cnt[256];
int graph[256][256];

int M;
int N, NA, NB, T;
int dep[256], arr[256];
bool vis[256];

bool search(int k)
{
    for (int j = 0; j < cnt[k]; j++)
	{
        int p = graph[k][j];
        if (ck[p])
		{
            ck[p] = false;
            int t = match[p];
            if (t == -1 || search(t))
			{
                match[p] = k;
                return true;
			}
            match[p] = t;
		}
	}
    return false;
}

int hungry()
{
    int ans = 0;
    for (int j = 0; j < M; j++)
	{
		match[j] = -1;
	}
    for (int i = 0; i < M; i++)
	{
        for (int j = 0; j < M; j++)
		{
			ck[j] = true;
		}
        if (search(i))
		{
			ans++;
		}
    }
    return ans;
}

int main()
{
	ifstream fin("B.in");
	ofstream fout("B.out");

	fin >> N;
	for (int ni = 1; ni <= N; ni++)
	{
		fin >> T;
		fin >> NA >> NB;
		M = NA + NB;
		for (int i = 0; i < M; i++)
		{
			cnt[i] = 0;
			vis[i] = true;
		}

		for (int i = 0; i < NA; i++)
		{
			string hm;
			int h, m;
			fin >> hm;
			sscanf(hm.c_str(), "%d:%d", &h, &m);
			dep[i] = h * 60 + m;
			fin >> hm;
			sscanf(hm.c_str(), "%d:%d", &h, &m);
			arr[i] = h * 60 + m;
		}
		for (int i = 0; i < NB; i++)
		{
			string hm;
			int h, m;
			fin >> hm;
			sscanf(hm.c_str(), "%d:%d", &h, &m);
			dep[NA + i] = h * 60 + m;
			fin >> hm;
			sscanf(hm.c_str(), "%d:%d", &h, &m);
			arr[NA + i] = h * 60 + m;
		}

		for (int i = 0; i < NA; i++)
		{
			for (int j = NA; j < M; j++)
			{
				if (arr[i] + T <= dep[j])
				{
					graph[i][cnt[i]++] = j;
				}
				if (arr[j] + T <= dep[i])
				{
					graph[j][cnt[j]++] = i;
				}
			}
		}

		//for (int i = 0; i < M; i++)
		//{
		//	fout << i << ": " << cnt[i] << " - ";
		//	for (int j = 0; j < cnt[i]; j++)
		//	{
		//		fout << graph[i][j] << " ";
		//	}
		//	fout << endl;
		//}

		int x = hungry();

		for (int i = 0; i < M; i++)
		{
			if (vis[i] && match[i] != -1)
			{
				int k = i;
				do
				{
					vis[k] = false;
					k = match[k];
				} while (match[k] != -1 && vis[k]);
			}
		}

		int ansA = 0;
		for (int i = 0; i < NA; i++)
		{
			if (vis[i])
			{
				ansA++;
			}
		}
		int ansB = 0;
		for (int i = NA; i < M; i++)
		{
			if (vis[i])
			{
				ansB++;
			}
		}

		fout << "Case #" << ni << ": " << ansA << " " << ansB << endl;
	}
}
