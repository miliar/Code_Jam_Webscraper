/**********************************************************************
Author: cominde
Created Time: Thursday, July 17, 2008 Arange09:13:50 HKT
File Name: ACrange/code/codejam1/a/a.cpp
**********************************************************************/
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>

using namespace std;

#define out(x) (cout<<#x<<":"<<x<<endl)
#define debug(x) (cout<<"debug"<<x<<endl)
const int maxint=0x7FFFFFFF;
const long long maxlonglong=0x7FFFFFFFFFFFFFFFLL;
template<class T>void show(T a,int n,int f){for(int i=f; i<n+f; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a,int r,int l,int f){for(int i=f; i<r+f; ++i)show(a[i],l,f);cout<<endl;}

int n, s, q;

struct Hash
{
	char str[110];
	int cnt;
	Hash *next;
};

const int range = 10001;

Hash *hash[range];
int cnt;

void init ()
{
	cnt = 1;
	for (int i = 0; i < range; i++)
		hash[i] = NULL;
	return ;
}

int ELFhash (char *key)
{
	unsigned long h = 0;
	while (*key)
	{
		h = (h << 4) + *key++;
		unsigned long g = h & 0Xf0000000L;
		if (g)
			h ^= g >> 24;
		h &= ~g;
	}
	return h % range;
}

int find (char *str)
{
	int k = ELFhash (str);
	for (Hash *p = hash[k]; p; p = p -> next)
		if (strcmp (str, p -> str) == 0)
			return p -> cnt;
	return -1;
}

int insert (char *str)
{
	int tmp = find (str);
	if (tmp != -1)
		return tmp;
	int k = ELFhash (str);
	Hash *p = new Hash;
	strcpy (p -> str, str);
	p -> cnt = cnt;
	tmp = cnt;
	cnt++;
	p -> next = hash[k];
	hash[k] = p;
	return tmp;
}

int a[1010];
int f[1010][110];

int main () {
//    freopen ("a.out", "w", stdout);
    scanf ("%d", &n);
    int c = 1;
    while (n--) {
        scanf ("%d\n", &s);
        init ();
        for (int i = 1; i <= s; i++) {
            char tmp[110];
            gets (tmp);
            insert (tmp);
        }
        scanf ("%d\n", &q);
        for (int i = 1; i <= q; i++) {
            char tmp[110];
            gets (tmp);
            a[i] = find (tmp);
        }

        for (int i = 1; i <= q; i++)
            f[0][i] = 0;
        for (int i = 1; i <= q; i++) {
//            printf ("ss\n");
            for (int j = 1; j <= s; j++) {
                int Min = 1010;
                for (int k = 1; k <= s; k++)
                    if (k != j && Min > f[i - 1][k] + 1)
                        Min = f[i - 1][k] + 1;
                if (a[i] == j) 
                    f[i][j] = 1010;
                else
                    f[i][j] = min (Min, f[i - 1][j]);
            }
        }
        int Min = maxint;
        for (int i = 1; i <= s; i++)
            if (Min > f[q][i])
                Min = f[q][i];
        printf ("Case #%d: %d\n", c++, Min);
    }
    return 0;
}

