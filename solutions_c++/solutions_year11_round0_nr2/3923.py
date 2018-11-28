#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int C, D, N, T;
	char **combine_ch, **oposed_ch, *elem_list;
	char tmp;
	FILE *f_in;
	FILE *f_out;
	f_in=fopen("B-small-attempt2.in","rt");
	f_out=fopen("out.txt","wt");
	fscanf(f_in,"%d",&T);
	for(int r=0; r<T; r++)
	{
		fscanf(f_in,"%d",&C);
		fscanf(f_in,"%c",&tmp);
		combine_ch=(char**)calloc(C,sizeof(char*));
		for(int i=0; i<C; i++)
		{
			combine_ch[i]=(char*)calloc(3,sizeof(char));
			fscanf(f_in,"%c",&combine_ch[i][0]);
			fscanf(f_in,"%c",&combine_ch[i][1]);
			fscanf(f_in,"%c",&combine_ch[i][2]);
		}
		fscanf(f_in,"%d",&D);
		fscanf(f_in,"%c",&tmp);
		oposed_ch=(char**)calloc(C,sizeof(char*));
		for(int i=0; i<D; i++)
		{
			oposed_ch[i]=(char*)calloc(2,sizeof(char));
			fscanf(f_in,"%c",&oposed_ch[i][0]);
			fscanf(f_in,"%c",&oposed_ch[i][1]);
		}
		fscanf(f_in,"%d",&N);
		fscanf(f_in,"%c",&tmp);
		elem_list=(char*)calloc(N,sizeof(char));
		for(int i=0; i<N; i++)
		{
			fscanf(f_in,"%c",&elem_list[i]);
		}
		for(int i=0; i<N-1; i++)
		{
			for(int j=0; j<C; j++)
			{
				if((elem_list[i]==combine_ch[j][0]&&elem_list[i+1]==combine_ch[j][1])||(elem_list[i]==combine_ch[j][1]&&elem_list[i+1]==combine_ch[j][0]))
				{
					elem_list[i]=combine_ch[j][2];
					for(int k=i+1; k<N-1; k++)
						elem_list[k]=elem_list[k+1];
					N--;
					break;
				}
			}
			for(int j=0; j<D; j++)
			{
				if(elem_list[i]==oposed_ch[j][0])
				{
					for(int h=i+1; h<N; h++)
					{
						for(int j=0; j<C; j++)
						{
							if((elem_list[h]==combine_ch[j][0]&&elem_list[h-1]==combine_ch[j][1])||(elem_list[h]==combine_ch[j][1]&&elem_list[h-1]==combine_ch[j][0]))
							{
								elem_list[h-1]=combine_ch[j][2];
								for(int k=h; k<N-1; k++)
									elem_list[k]=elem_list[k+1];
								h--;
								N--;
								break;
							}
						}
						if(elem_list[h]==oposed_ch[j][1])
						{
							for(int o=h+1; o<N; o++)
								elem_list[o-h-1]=elem_list[o];
							N=N-h-1;
							i=-1;
							break;
						}
					}
				}
				else if(elem_list[i]==oposed_ch[j][1])
				{
					for(int h=i+1; h<N; h++)
					{
						for(int j=0; j<C; j++)
						{
							if((elem_list[h]==combine_ch[j][0]&&elem_list[h-1]==combine_ch[j][1])||(elem_list[h]==combine_ch[j][1]&&elem_list[h-1]==combine_ch[j][0]))
							{
								elem_list[h-1]=combine_ch[j][2];
								for(int k=h; k<N-1; k++)
									elem_list[k]=elem_list[k+1];
								h--;
								N--;
								break;
							}
						}
						if(elem_list[h]==oposed_ch[j][0])
						{
							for(int o=h+1; o<N; o++)
								elem_list[o-h-1]=elem_list[o];
							N=N-h-1;
							i=-1;
							break;
						}
					}
				}
			}
		}
		fprintf(f_out,"Case #%d: [", r+1);
		for(int i=0; i<N; i++)
		{
			fprintf(f_out,"%c, ",elem_list[i]);
		}
		if(N!=0)
			fseek(f_out, -2*sizeof(char), SEEK_CUR);
		fprintf(f_out,"]\n");
	}
	return 0;
}