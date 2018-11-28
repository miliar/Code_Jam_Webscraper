#include <stdio.h>
#include <vector>

using namespace std;

int main(){
	FILE *fp= fopen("c:\\prvi2.out", "w+");
	int t,n;
	vector <int> o;
	vector <int> b;
	vector <int> redoslijed;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int o_trenutno=1,b_trenutno=1;
		int o_naredba=0,b_naredba=0,redoslijed_naredbi=0;
		int timer=0;
		scanf("%d",&n);
		for(int j=0;j<n;j++){
			int gumb;
			char robot;
			scanf(" %c", &robot);
			scanf(" %d", &gumb);
			if(robot=='O')
				o.push_back(gumb);
			else
				b.push_back(gumb);
			redoslijed.push_back(robot);
		}

		while(redoslijed_naredbi!=redoslijed.size()){

			timer++;
			int pom=1;
			if(o_naredba<o.size())
			if(o[o_naredba]==o_trenutno){
				if(redoslijed[redoslijed_naredbi]=='O'){
				//	printf("o stisce gumb\n");
					redoslijed_naredbi++;
					o_naredba++;
					pom=0;
				}
			}else{
			//	printf("pomicem o\n");
				if(o_trenutno<o[o_naredba]){
					o_trenutno++;
				}else{
					o_trenutno--;
				}
			}	
			if(b_naredba<b.size())
			if(b[b_naredba]==b_trenutno){				
				if(redoslijed[redoslijed_naredbi]=='B' && pom){
				//	printf("b stisce gumb\n");
					redoslijed_naredbi++;
					b_naredba++;
				}
			}else{
			//	printf("%d %d",b_trenutno, b[b_naredba]);
			//	printf("pomicem b ");
				if(b_trenutno<b[b_naredba]){
					b_trenutno++;
			//		printf("desno\n");
				}else{
					b_trenutno--;
				//	printf("lijevo\n");
				}
			}
						
		}
		o.clear();
		b.clear();
		redoslijed.clear();
		printf("Case #%d: %d\n",(i+1),timer);
		fprintf(fp, "Case #%d: %d\n",(i+1),timer);
	}
	
}