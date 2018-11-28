#include<stdio.h>
int main(){
	int T, cases = 1;
	scanf("%d",&T);
	while(T--)
	{
		   int C,D,N;
		   char combine[26][26];
		   bool diff[26][26];
		   for(int i = 0; i < 26; i++)
		   {
			   for(int j = 0; j < 26; j++)
			   {
				   diff[i][j] = false;
				   combine[i][j] = 0;
			   }
		   }
		   scanf("%d", &C);
		   while(C--)
		   {
			   char str[3];
			   scanf("%s", str);
			   combine[str[0] - 'A'][str[1] - 'A'] = str[2];
			   combine[str[1] - 'A'][str[0] - 'A'] = str[2];
		   }
		   scanf("%d", &D);
		   while(D--)
		   {
			   char str[2];
			   scanf("%s", str);
			   diff[str[0] - 'A'][str[1] - 'A'] = true;
			   diff[str[1] - 'A'][str[0] - 'A'] = true;
		   }
		   scanf("%d", &N);
		   char input[100], output[100];
		   int cursor = 0;
		   scanf("%s", input);
		   for(int i = 0; i < N; i++)
		   {
			   if( cursor == 0)
			   {
				   output[cursor++] = input[i];
				   continue;
			   }
			   char curr = input[i], top = output[cursor - 1];	
			   if( combine[top - 'A'][curr - 'A'] != 0)
			   {
				   cursor--;
				   output[cursor++] = combine[top - 'A'][curr - 'A'];
				   continue;
			   }
			   bool bClear = false;
			   for( int j = 0; j < cursor; j++)
			   {
				   if( diff[input[i] - 'A'][output[j] - 'A'] )
				   {
					   bClear = true;
					   break;
				   }
			   }
			   if( bClear )
			   {
				   cursor = 0;
			   }
			   else
			   {
				   output[cursor++] = input[i];
			   }
		   }
		   if( cursor == 0)
		   {
			   printf("Case #%d: []\n", cases++);
		   }
	        else
	        {
				 printf("Case #%d: [", cases++);
				 for( int i = 0; i < cursor; i++)
				 {
					 printf("%c", output[i]);
					 if( i == cursor - 1 )
					 {
						 printf("]\n");
					 }
					 else
					 {
						 printf(", ");
					 }
				 }
		   }

	}
	return 0;
} 
