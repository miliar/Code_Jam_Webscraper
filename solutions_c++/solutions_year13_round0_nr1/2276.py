#include <cstdio>
#include <vector>

#define FOR(a,b) for(int a=0; a<b; a++)

using namespace std;

int n;
vector < int > x, o; 
int ax, ao;
int dots;

char c;

int main (){
	x.resize(10);
	o.resize(10);
	scanf("%d", &n);
	getchar();
	
	FOR(cas, n){
		dots=0;
		FOR(i, 4){
			FOR(j, 4){
				switch(c=getchar()){
					case '.':
						ax=0;
						ao=0;
						dots++;
						break;
					case 'O':
						ax=0;
						ao=1;
						break;
					case 'X':
						ax=1;
						ao=0;
						break;
					case 'T':
						ax=1;
						ao=1;
						break;
				}
//				printf("%c", c);
				x[i]+=ax;
				x[j+4]+=ax;
				o[i]+=ao;
				o[j+4]+=ao;
				if(i==j){
					x[8]+=ax;
					o[8]+=ao;
				}
				if(i+j==3){
					x[9]+=ax;
					o[9]+=ao;
				}
			}
			getchar();
//			printf("###\n");
		}
		getchar();
				
/*		FOR(i, 10)
			printf("%3d", i);
		printf("\n");
		FOR(i, 10)
			printf("%3d", x[i]);
		printf("\n");
		FOR(i, 10)
			printf("%3d", o[i]);
		printf("\n");
*/		
		printf("Case #%d: ", cas+1);

			FOR(i, 10){
				if(x[i]==4){
					printf("X won\n");
					break;
				}
				if(o[i]==4){
					printf("O won\n");
					break;
				}
				if(i==9){
					if(dots==0){
						printf("Draw\n");
					}else{
						printf("Game has not completed\n");
					}
				}
			}

		FOR(i, 10)
			x[i]=o[i]=0;
	}
	return 0;
}
