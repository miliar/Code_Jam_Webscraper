#include <stdio.h>
#include <string>
#include <string.h>
#include <set>

using namespace std;

#define MAXCHR 1024*24

set<string> qualities;

double calcula(const char *tree)
{
	double ret = 1;
	double temp;
	int l = 0;
	int lt;

//	printf("[%s]\n",tree); fflush(stdout);
	for ( l = 0 ; tree[l] == ' ' || tree[l] == '(' ; l++ ) ;

	sscanf(&tree[l],"%lf%n",&temp,&lt);
	ret *= temp;

	l += lt;
	for ( ; tree[l] == ' ' ; l++) ;
	if ( tree[l] != ')' )
	{
		char feature[MAXCHR];
		sscanf(&tree[l],"%[a-zA-Z]%n",feature,&lt);
		l += lt;
		for ( ; tree[l] == ' ' ; l++) ;
		if ( qualities.find(feature) == qualities.end() )
		{
			int p = 0;

			for ( ; ; l++)
			{
				if ( tree[l] == '(' ) p++;
				else if ( tree[l] == ')' ) p--;

				if ( p == 0 ) break;
			}
			l++;
		}
		ret *= calcula(&tree[l]);
	}

	return ret;
}

int main (void)
{
	int n;
	
	scanf("%d",&n);

	for ( int i = 0 ; i < n ; i++ )
	{
		printf("Case #%d:\n",i+1);
		int l;
		string linha;
		scanf("%d%*c",&l);

		for ( int j = 0 ; j < l ; j++ )
		{
			char temp[MAXCHR];
			fgets(temp, sizeof(temp), stdin);
			if ( temp[strlen(temp)-1] == '\n' ) temp[strlen(temp)-1] = '\0';

			linha += temp;
		}
//		printf("--%s--\n",linha.c_str());

		int a;
		scanf("%d%*c",&a);

		for ( int j = 0 ; j < a ; j++ )
		{
			char animal[MAXCHR];
			int q;

			qualities.clear();

			scanf("%s",animal);
			scanf("%d",&q);

			for ( int k = 0 ; k < q ; k++ )
			{
				char temp[MAXCHR];
				scanf("%s",temp);
				qualities.insert(temp);
			}

			printf("%0.7f\n",calcula(linha.c_str()));
		}
	}

	return 0;
}
