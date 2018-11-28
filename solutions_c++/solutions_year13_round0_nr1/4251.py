#include<cstdio>

using namespace std;

int getcounts(char *arr, int t, FILE* fp)
{
	int dot = 0;
	int x = 0, o = 0, T = 0;
	
	for(int i=0; i<4; i++) 
	{
	
	switch(arr[i])
	{
		case 'X' : x++;
			break;
		case 'O' : o++;
			break;
		case '.' : dot++;
			break;
		case 'T' : T++;
			break;
		default: printf("ERROR\n");
	}
			
	if(x>2 || o>2)
	{
		if((x == 4) || ((x == 3) && T == 1))
		{
			//x has won
			fprintf(fp, "Case #%d: X won\n", t);
			return -1;
		}
		else if((o == 4) || ((o == 3) && T == 1))
		{
			//o has won	
			fprintf(fp, "Case #%d: O won\n", t);
			return -1;
		}	
	}
	
	}	
	return dot;
}

int main(int argc, char** argv)
{
	int t = 0;
	FILE *fp = fopen(argv[1], "r");
	FILE *fm = fopen(argv[2], "w");
	fscanf(fp, "%d", &t);

	for(int i=0; i<t; i++)
	{
		char inp[4][4] ={'\0'};
		
		for(int j=0; j<4; j++)
		{
			fscanf(fp, "%s", inp[j]);
		}
			
		int dot = 0; // no dots
		int flag = 0;

		//for the rows
		for(int k=0; k<4; k++)
		{	
			int y = getcounts(inp[k], i+1, fm);

			if(y > 0)
				dot = 1;
			else if(y == -1)
			{
				flag = 1;
				break;
			}
		}
	
		if(!flag) {
		//for columns
		int flg = 0;
		for(int k=0; k<4; k++)
		{
			char temp0[4] = {'\0'};
			
			for(int m=0; m<4; m++)
			{
				temp0[m] = inp[m][k];
			}
			
			int y0 = getcounts(temp0, i+1, fm);

			if(y0 > 0)
				dot = 1;
			else if(y0 == -1)
			{
				flg = 1;
				break;
			}

		}
	
		if(!flg) {
		
			int fl = 0;

			char temp1[4] = {'\0'};
			
			for(int m=0; m<4; m++)
			{
				temp1[m] = inp[m][m];
			}
		
			int y1 = getcounts(temp1, i+1, fm);

			if(y1 > 0)
				dot = 1;
			else if(y1 == -1)
				fl = 1;
	
			if(!fl)
			{
				char temp2[4] = {'\0'};

				for(int m=0; m<4; m++)
				{
					temp2[m] = inp[m][3-m];
				}
	
				int y2 = getcounts(temp2, i+1, fm);
	
				if(y2 > 0)
					dot = 1;
				else if(y2 == -1)
					continue;;
		
				if(dot > 0)
				{
					//game is incomplete
					fprintf(fm, "Case #%d: Game has not completed\n", i+1);
				}
				else
				{
					//draw
					fprintf(fm, "Case #%d: Draw\n", i+1);
				}
			}// fl end
		}// flg end

		} // flag end

//	if(i != (t-1)) {
//	char tmp[10] = {'\0'};
	fscanf(fp, "\n"); 
	}
	
	return 0;
}
