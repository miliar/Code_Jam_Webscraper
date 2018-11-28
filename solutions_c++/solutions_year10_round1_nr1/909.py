#include <cstdio>

using namespace std;

const int MaxN=51;
int ars[MaxN][MaxN];
bool f[MaxN][MaxN];

const int dxy[2][8]={
	 0, -1, -1, -1, 0, 1, 1,  1,
	-1, -1,  0,  1, 1, 1, 0, -1
};
bool check(int i, int j, int n, int k)
{
	int x, y;
	//if(f[i][j]) return false;
	int ct[4]={1, 1, 1, 1};
	for(int dr=0; dr<4; dr++)
	{
		int tf[]={0, 4};
		
		for(int tk=0; tk<2; tk++){
			x=i+dxy[0][dr+tf[tk]];
			y=j+dxy[1][dr+tf[tk]];

			while( x>=0 && x<n && y>=0 && y<n ){
				if(ars[x][y]!=ars[i][j]) break;
			
				++ct[dr];

				x += dxy[0][dr+tf[tk]];
				y += dxy[1][dr+tf[tk]];
			}

			if(ct[dr]>=k) return true;
		}
	}
	return false;
}
int main(int argc, char **argv)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for(int icase=0; icase<t; icase++){
		int k, n;
		scanf("%d%d", &n, &k);
		

		for(int i=0; i<n; i++){
			char c, str[MaxN];

			scanf("%s", str);
			
			for(int j=0; str[j]!='\0'; j++){
				ars[j][n-1-i]=str[j];
			}
		}

		for(int j=0; j<n; j++){
			int i=n;
			for(int ct=n-1; ct>=0; ct--){
				if(ars[ct][j]!='.'){
					ars[--i][j]=ars[ct][j];
				}
			}
			for(int ct=0; ct<i; ct++){
				ars[ct][j]='.';
			}
		}
		
		bool fb=false;
		bool fr=false;
		
		//memset(f, 0, sizeof(f));

		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if( !fb &&  ars[i][j]=='B' && check(i, j, n, k)) fb = true;
				if( !fr &&  ars[i][j]=='R' && check(i, j, n, k)) fr = true;

				if( fr && fb) break;
			}
		}
		if(fr && fb){
			printf("Case #%d: Both\n", icase+1);
		}else if(fr)
		{
			printf("Case #%d: Red\n", icase+1);
		}else if(fb)
		{
			printf("Case #%d: Blue\n", icase+1);
		}else{
			printf("Case #%d: Neither\n", icase+1);
		}

	}
	return 0;
}