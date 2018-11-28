#include <stdio.h>
#include <string.h>

int main()
{
	int N, T, C, min, i, j, I, x, total, len;
	char combine[26][26];
	char oppose[26][26];
	int count[26];
	char str[200];
	char input[200];
	scanf("%d",&N);
	for(I=0; I<N; ++I)
	{
		memset(combine,0,sizeof(combine));
		memset(oppose,0,sizeof(oppose));
		memset(count,0,sizeof(count));
		len = 0;
//		x = total = 0;
		scanf("%d",&C);
		for(i=0; i<C; ++i)
		{
			scanf("%s", input);
			combine[input[0]-'A'][input[1]-'A']=combine[input[1]-'A'][input[0]-'A']=input[2];
		}
		// reuse C as D
		scanf("%d",&C);
		for(i=0; i<C; ++i)
		{
			scanf("%s", input);
			oppose[input[0]-'A'][input[1]-'A']=oppose[input[1]-'A'][input[0]-'A']=1;
		}
		int n;
		scanf("%d",&n);
		scanf("%s",input);
		for(i=0; i<n; ++i)
		{
			char p = input[i]-'A'; //process_char
			str[len]=p;
//			count[p]++;
			++len;
			// check combine
			if( len>=2 && combine[str[len-1]][str[len-2]]!=0 )
			{
				count[p]++; // count p;
				-- count[str[len-1]];
				-- count[str[len-2]];
				++ count[combine[str[len-1]][str[len-2]]-'A'];
				str[len-2]=combine[str[len-1]][str[len-2]]-'A';
				str[len-1]=0;
				--len;
				continue;
			}

			// check oppose
			for(j=0; j<26; ++j)
			{
				if( count[j] && oppose[str[len-1]][j] )
				{
					// empty string
					memset(count,0,sizeof(count));
					len = 0;
					break;
				}
			}

			// don't count current
			if(j==26)
				++count[p];
		}
		printf("Case #%d: [", I+1);
		for(j = 0; j< len; ++j )
		{
			if( j!=0 )
				printf( ", " );
			putchar( str[j]+'A' );
		}
		printf("]\n");
	}
	return 0;
}