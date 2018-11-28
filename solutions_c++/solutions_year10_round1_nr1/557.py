#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <cmath>
using namespace std;
const double PI = acos(-1.0);
const int mn=60;

int n,k;
char s[mn][mn];

void transform(){
    int c[mn][mn]={};
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            c[j][n-i-1]=s[i][j];
    for(int i=0;i<n;i++){
        int cp=n-1;
        for(int j=n-1;j>=0;j--){
            if(c[j][i]!='.'){
                c[cp--][i]=c[j][i];
            }
        }
        for(int j=cp;j>=0;j--)
            c[j][i]='.';
    }
    memset(s,0,sizeof(s));
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            s[i][j]=c[i][j];
}

int count(int x,int y,int dx,int dy,char winc){
    int c=0;
    while(x>=0 && x<n && y>=0 && y<n){
        if(s[x][y]==winc)c++;
        else break;
        x+=dx;
        y+=dy;
    }
    return c;
}

bool checkwin(char winc){
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(s[i][j]==winc){
                int m=0;
                m=max(m,count(i,j,0,1,winc)+count(i,j,0,-1,winc)-1);
                m=max(m,count(i,j,1,0,winc)+count(i,j,-1,0,winc)-1);
                m=max(m,count(i,j,1,1,winc)+count(i,j,-1,-1,winc)-1);
                m=max(m,count(i,j,-1,1,winc)+count(i,j,1,-1,winc)-1);
                if(m>=k)return 1;
            }
    return 0;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
	int Tn;
	scanf("%d", &Tn);
	for (int T = 1; T <= Tn; T++) {
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++)scanf("%s",s[i]);
		transform();
		/*for(int i=0;i<n;i++){
		    puts(s[i]);
		}*/
		bool R = checkwin('R');
		bool B = checkwin('B');
		printf("Case #%d: ", T);
		if(R&&B){
		    puts("Both");
		}else if(R){
		    puts("Red");
		}else if(B){
		    puts("Blue");
		}else{
		    puts("Neither");
		}
	}
	return 0;
}
