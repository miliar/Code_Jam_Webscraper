#include <cstdio>

char a[5][5];

int main(){// freopen("in.txt", "r", stdin);
		//	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int r=1; r<=T; r++){
		bool f=1, x=0, o=0, ch;
		for(int i=0; i<4; i++)
			scanf("%s", a[i]);
		for(int i=0; i<4; i++){
			ch=1;
			for(int j=0; j<4; j++)
				if(!(a[i][j] == 'X' || a[i][j] == 'T'))
					ch=0;
			if(ch) x=1;

			ch=1;
			for(int j=0; j<4; j++)
				if(!(a[j][i] == 'X' || a[j][i] == 'T'))
					ch=0;
			if(ch) x=1;

			
			ch=1;
			for(int j=0; j<4; j++)
				if(!(a[i][j] == 'O' || a[i][j] == 'T'))
					ch=0;
			if(ch) o=1;

			ch=1;
			for(int j=0; j<4; j++)
				if(!(a[j][i] == 'O' || a[j][i] == 'T'))
					ch=0;
			if(ch) o=1;
		}

		ch=1;
		for(int i=0; i<4; i++)
			if(!(a[i][i] == 'X' || a[i][i] == 'T'))
				ch=0;
		if(ch) x=1;

		ch=1;
		for(int i=0; i<4; i++)
			if(!(a[i][3-i] == 'X' || a[i][3-i] == 'T'))
				ch=0;
		if(ch) x=1;
		
		ch=1;
		for(int i=0; i<4; i++)
			if(!(a[i][i] == 'O' || a[i][i] == 'T'))
				ch=0;
		if(ch) o=1;

		ch=1;
		for(int i=0; i<4; i++)
			if(!(a[i][3-i] == 'O' || a[i][3-i] == 'T'))
				ch=0;
		if(ch) o=1;

		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(a[i][j]=='.') 
					f=0;
		if(x | o)
			f=1;

		printf("Case #%d: ", r);
		
		if(f){
			if(x) puts("X won");
			else if(o) puts("O won");
			else puts("Draw");
		}
		else{
			puts("Game has not completed");
		}
	}
}