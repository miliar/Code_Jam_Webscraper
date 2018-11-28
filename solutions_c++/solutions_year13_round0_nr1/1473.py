#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<cmath>
#include<algorithm>
#include<queue>

using namespace std;

char field[5][5];

void main(){
#ifdef MY_TEST_VAR
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif
   
   int n;
   scanf("%d",&n);

   for (int I = 1; I <= n; I++)
   {
	   bool def = 0;
	   char et;
	   gets( field[0] );
	   printf("Case #%d: ", I);
	   for (int i = 0; i < 4; i++)
		   gets( field[i] );

	   et = field[0][0];
	   if (et == 'T')
		   et = field[1][1];
	   if (et != '.')
	   {
		   bool w = 1;
		   for (int i = 0; i < 4 && w; i++)
			   w = w && (field[i][i] == et || field[i][i] == 'T');

		   if (w)
		   {
			   printf("%c won\n", et);
			   def = 1;
		   }
	   }
	   if (def)	continue;

	   et = field[0][3];
	   if (et == 'T')
		   et = field[1][2];
	   if (et != '.')
	   {
		   bool w = 1;
		   for (int i = 0; i < 4 && w; i++)
			   w = w && (field[i][3 - i] == et || field[i][3 - i] == 'T');

		   if (w)
		   {
			   printf("%c won\n", et);
			   def = 1;
		   }
	   }
	   if (def)	continue;

	   for (int i = 0; i < 4 && !def; i++)
	   {
		   et = field[i][0];
		   if (et == 'T')
			   et = field[i][1];
		   if (et != '.')
		   {
			   bool w = 1;
			   for (int j = 0; j < 4 && w; j++)
				   w = w && (field[i][j] == et || field[i][j] == 'T');

			   if (w)
			   {
				   printf("%c won\n", et);
				   def = 1;
			   }
			}
	   }
	   if (def)	continue;
	   	   
	   for (int i = 0; i < 4 && !def; i++)
	   {
		   et = field[0][i];
		   if (et == 'T')
			   et = field[1][i];
		   if (et != '.')
		   {
			   bool w = 1;
			   for (int j = 0; j < 4 && w; j++)
				   w = w && (field[j][i] == et || field[j][i] == 'T');

			   if (w)
			   {
				   printf("%c won\n", et);
				   def = 1;
			   }
			}
	   }
	   if (def)	continue;

	   bool d = 1;
	   for (int i = 0; i < 4 && d; i++)
		   for (int j = 0; j < 4 && d; j++)
			   d = d && (field[i][j] != '.');

	   if (d)
		   printf("Draw\n");
	   else
		   printf("Game has not completed\n");
   }
}