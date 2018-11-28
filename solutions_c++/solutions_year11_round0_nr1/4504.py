#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int N, T;
	bool push_O=false, push_B=false;
	FILE *f_in;
	FILE *f_out;
	f_in=fopen("A-large.in","rt");
	f_out=fopen("out.txt","wt");
	fscanf(f_in,"%d",&T);
	for(int r=0; r<T; r++)
	{
		int k=0, m=0, pos_O=1, pos_B=1, time=0;
		int **O, **B, *P;
		char *R;
		fscanf(f_in,"%d",&N);
		P = (int*)calloc(N,sizeof(int));
		R = (char*)calloc(N,sizeof(char));
		for(int i=0; i<N; i++)
		{
			fscanf(f_in,"%c",&R[i]);
			fscanf(f_in,"%c",&R[i]);
			fscanf(f_in,"%d",&P[i]);
		}
		O = (int**)calloc(N,sizeof(int*));
		B = (int**)calloc(N,sizeof(int*));
		for(int i=0; i<N; i++)
		{
			O[i]=(int*)calloc(2,sizeof(int));
			B[i]=(int*)calloc(2,sizeof(int));
		}
		for(int i=0; i<N; i++)
		{
			if(R[i]=='O')
			{
				O[k][0]=P[i];
				O[k][1]=i;
				k++;
			}
			if(R[i]=='B')
			{
				B[m][0]=P[i];
				B[m][1]=i;
				m++;
			}
		}
		int i=0;
		int j=0;
		while(P[N-1]!=0)
		{
			if(i==k||O[i][1]!=0)
			{
				if(i<k&&P[O[i][1]-1]==0&&O[i][0]==pos_O)
				{
					time++;
					push_O=true;
				}
				else if(i<k&&O[i][0]!=pos_O&&k!=0)
				{
					if(O[i][0]>pos_O)
						pos_O++;
					if(O[i][0]<pos_O)
						pos_O--;
					time++;
				}
				else if((O[i][0]==pos_O&&P[O[i][1]-1]!=0)||k==0||i==k)
				{
					time++;
				}
			}
			else if(O[i][1]==0)
			{
				if(O[i][0]==pos_O)
				{
					time++;
					push_O=true;
				}
				else if(i<k&&O[i][0]!=pos_O&&k!=0)
				{
					if(O[i][0]>pos_O)
						pos_O++;
					if(O[i][0]<pos_O)
						pos_O--;
					time++;
				}
			}
			if(j==m||B[j][1]!=0)
			{
				if(j<m&&P[B[j][1]-1]==0&&B[j][0]==pos_B)
				{
					push_B=true;
				}
				else if(j<m&&B[j][0]!=pos_B&&m!=0)
				{
					if(B[j][0]>pos_B)
						pos_B++;
					if(B[j][0]<pos_B)
						pos_B--;
				}/*
				else if((B[j][0]==pos_B&&P[B[j][1]-1]!=0)||m==0||j==m)
				{
					printf("stay\n");
				}*/
			}
			else if(B[j][1]==0)
			{
				if(B[j][0]==pos_B)
				{
					push_B=true;
				}
				else if(j<m&&B[j][0]!=pos_B&&m!=0)
				{
					if(B[j][0]>pos_B)
						pos_B++;
					if(B[j][0]<pos_B)
						pos_B--;
				}
			}
			if(push_O)
			{
				P[O[i][1]]=0;
				i++;
				push_O=false;
			}
			if(push_B)
			{
				P[B[j][1]]=0;
				j++;
				push_B=false;
			}
		}
		fprintf(f_out,"Case #%d: %d\n", r+1,time);
	}
	return 0;
}