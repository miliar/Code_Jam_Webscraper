#include "iostream"
#include "algorithm"
#include "cstdio"
#include "cstring"
using namespace std;

int r,c;
char m[100][100];
int ans[100][100];
int main(){
	freopen("A.out","w",stdout);
	int cs;
	cin>>cs;
	for(int css=1;css<=cs;css++){
		cin>>r>>c;
		for (int i=0;i<r;i++)
		{
			scanf("%s", m[i]);
		}

		bool pos = 1;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(m[i][j]=='.') continue;
				if(m[i][j]=='#'){
					if(i+1>=r || j+1>=c){
						pos = 0;
						break;
					}
					if(m[i+1][j+1] != '#'||m[i][j+1]!='#' || m[i+1][j]!='#'){
						pos = 0;
						break;
					}
					m[i+1][j+1]='/';
					m[i+1][j] = '\\';
					m[i][j+1] = '\\';
					m[i][j] = '/';
				}
			}
			if(pos==0)break;
		}
		printf("Case #%d:\n", css);
		if(pos==0) printf("Impossible\n");
		else{
			for(int i=0;i<r;i++)
			{
				printf("%s\n",m[i]);
			}
		}
		
	}
	return 0;
}