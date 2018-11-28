#include "cstdio"


int tab[100][100];

FILE *in=fopen("A-large.in","r");
FILE *out=fopen("outlarge","w");

int main(){
	int t,n,row,col;
	bool flag;
	fscanf(in,"%d",&t);
	char napis[200];

	for(int k=1;k<=t;k++){
		flag=true;
		fscanf(in,"%d%d ",&row,&col);
	
		for(int i=0;i<row;i++){
			
			fgets(napis,200,in);
			for(int j=0;j<col;j++){
				if(napis[j]=='.') tab[i][j]=0;
				else tab[i][j]=1;	
			}
		}

		// brzegi
		for(int i=0;i<row;i++)
			tab[i][col]=5;
		for(int i=0;i<col;i++)
			tab[row][i]=5;

		// blue=>red
		for(int i=0;i<row;i++)
			for(int j=0;j<col;j++){
				if(tab[i][j]==1 && tab[i+1][j]==1 && tab[i][j+1]==1 && tab[i+1][j+1]==1){
					tab[i][j]=2;
					tab[i+1][j]=3;
					tab[i][j+1]=3;
					tab[i+1][j+1]=2;			
				}
			}
		
		for(int i=0;i<row;i++)
			for(int j=0;j<col;j++)
				if(tab[i][j]==1) flag=false;


		// print
		if(flag==false) fprintf(out,"Case #%d:\nImpossible\n",k);
		else {
			fprintf(out,"Case #%d:\n",k);
			for(int i=0;i<row;i++){
				for(int j=0;j<col;j++)
					if(tab[i][j]==0) fprintf(out,".");
					else if(tab[i][j]==2) fprintf(out,"/");
					else fprintf(out,"\\");
					
				fprintf(out,"\n");
			}
			
		}

	}

return 0;
}