#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outlarge.txt","w",stdout);
	bool m[15][26];
	memset(m,0,15*26);
	int L, D, N, i;
	vector<string> slov;
	char tmp[500];
	scanf("%d %d %d\n",&L,&D,&N);
	for (int d = 0; d < D; ++d){
		gets(tmp);
		slov.push_back(tmp);	
	}
	int pos = 0;
	bool skob = false;
	for (int n = 0; n < N; n++)
	{
		memset(m,0,15*26);
		gets(tmp);
		pos = 0;
		skob = false;
		for (int i = 0; i < strlen(tmp); ++i )
		{
			if ( (tmp[i] >= 'a') && (tmp[i] <= 'z') ){
				m[pos][tmp[i]-'a'] = true;
				if (!skob) pos++;
			} 
			else if (tmp[i] == '(') skob = true; 
			else if (tmp[i] == ')') { skob = false;   pos++;   }
		}
		int count = 0;
		for (int d = 0; d < slov.size(); ++d){
			int fl = true; 
			for (int l = 0; l < L; l++){
				if (m[ l ][ slov[d][l]-'a' ] == false ) {
					fl = false;
					break;
				}
			}
			if (fl) count++;
		}
		printf("Case #%d: %d\n",n+1,count);
	}
	return 0;
}