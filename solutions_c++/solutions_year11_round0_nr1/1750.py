#include <stdio.h>


typedef struct _seq{
	char color;
	int button;
}SEQUENCE;

int main()
{
	FILE* fin,*fout;	
	int t,n,i;
	SEQUENCE s[100];
	fin=fopen("input.txt","r");
	fout=fopen("output.txt","w");
	fscanf(fin,"%d",&t);
	for(i=0;i<t;i++)
	{
		fprintf(fout,"Case #%d: ",i+1);

		int opos=1,bpos=1,onextpos=-1,bnextpos=-1;
		int seconds=0;
		int curseq=0;
		fscanf(fin,"%d",&n);
		for(int j=0;j<n;j++)
		{
			do
			{
				s[j].color = fgetc(fin);
			}while(s[j].color==' ');
			fscanf(fin,"%d",&s[j].button);
		}
		int bODone=1,bBDone=1;
		while(1)
		{
			int k=onextpos + 1;
			if(bODone)
			{
				while(k<n)
				{
					if(s[k].color == 'O')
					{
						onextpos = k;
						break;
					}
					k++;
				}			
				if(k==n)
					onextpos=-1;
				bODone=0;
			}
			if(bBDone)
			{
				k=bnextpos+1;
				while(k<n)
				{
					if(s[k].color == 'B')
					{
						bnextpos = k;
						break;
					}
					k++;
				}
				if(k==n)
					bnextpos=-1;
				bBDone=0;
			}
			if(onextpos == -1 && bnextpos == -1)
				break;
			while(1)
			{
				int bDone=0;
				seconds++;
				if(s[curseq].color == 'O')
				{
					if(opos == s[onextpos].button)
					{
						curseq++;
						bDone=1;
						bODone=1;
					}
				}
				else if(!bDone)
				{
					if(bpos == s[bnextpos].button)
					{
						curseq++;
						bDone=1;
						bBDone=1;
					}
				}
				if((onextpos != -1) && (opos != s[onextpos].button))
				{
					if(opos < s[onextpos].button)
						opos++;
					else
						opos--;
				}
				if((bnextpos != -1) && (bpos != s[bnextpos].button))
				{
					if(bpos < s[bnextpos].button)
						bpos++;
					else
						bpos--;
				}
				if(bDone)
					break;
			}
		}
		fprintf(fout,"%d",seconds);
		if(i!=t-1)
			fprintf(fout,"\n");
	}
	return 0;
}