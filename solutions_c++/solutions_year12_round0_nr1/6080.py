#include<cstdio>
#include<cstdlib>
#include<cstring>

//#define DEBUG

using namespace std;

inline int readInt()
{
	int n;
	scanf("%d", &n);
	return n;
}

#define MAX 101
char G[MAX];
char S[MAX];

class Map
{
public:
	Map();
	char getMap(char c) 
	{ return c==' '?' ': mapping[c-'a']; }
	void setMap(char s, char d) { mapping[s-'a'] = d; } 
	void Transform()
	{
		int i=0;
		int l = strlen(G);
		for(;i<l;i++)
			S[i] = getMap(G[i]);
		S[i] = '\0';
	}
private:
	enum { size = 26 };
	char mapping[size];
};

Map::Map()
{
	memset(mapping, 0, size);
	char source[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char dest[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	for(int i=0;i<sizeof source/sizeof source[0];i++)
	{
		mapping[source[i] - 'a'] = dest[i];
	}
#ifdef DEBUG
	for(int i=0;i<size; i++)
	{
		printf("%c - %c\n", i+'a', mapping[i]);
	}
#endif
}



int main()
{
	Map mappings;
	mappings.setMap('z', 'q');
	mappings.setMap('q', 'z');
	/*mappings.setMap('z', 'z');
	mappings.setMap('q', 'q');*/
	int nTc = readInt();
	for(int t=1;t<=nTc;t++)
	{
		scanf("\n%[^\n]", G);
#ifdef DEBUG 
		printf("%s\n", G);
#endif
		mappings.Transform();
		printf("Case #%d: %s\n", t, S);
	}
	return 0;
}