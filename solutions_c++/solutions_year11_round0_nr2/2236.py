#include <stdio.h>
#include <string>
using namespace std;

int C,T,A,B,L,P[255][255];
char IN[5],CH[255][255],U[220];

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int i,j;

	scanf ("%d",&T); while (T--){
		for (i='A';i<='Z';i++) for (j='A';j<='Z';j++) CH[i][j] = P[i][j] = 0;

		scanf ("%d",&A);
		for (i=0;i<A;i++){
			scanf ("%s",IN); CH[IN[0]][IN[1]] = CH[IN[1]][IN[0]] = IN[2];
		}

		scanf ("%d",&B);
		for (i=0;i<B;i++){
			scanf ("%s",IN); P[IN[0]][IN[1]] = P[IN[1]][IN[0]] = 1;
		}

		scanf("%d %s",&L,U); string t = "";
		for (j=0;j<L;j++){
			t = U[j] + t;
			while (1){
				if (t.length() >= 2 && CH[t[0]][t[1]] != 0){
					t = CH[t[0]][t[1]] + t.substr(2,t.length()-2);
				}
				else break;
			}
			for (i=1;i<t.length();i++){
				if (P[t[0]][t[i]]){
					t = ""; break;
				}
			}
		}

		printf ("Case #%d: ",++C);
		printf ("[");
		for (i=int(t.length())-1;i>=0;i--){
			printf ("%c",t[i]);
			if (i != 0) printf (", ");
		} printf ("]\n");
	}

	return 0;
}