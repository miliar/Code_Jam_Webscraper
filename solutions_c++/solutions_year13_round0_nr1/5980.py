#include<stdio.h>

void main()
{
	char temp_ch,S=0,G=0,parity_bit=0;
	char TTT[4][4]={0,};
	int T,l,i,j,c;
	FILE *pFile,*pFile1;
	pFile=fopen("C:\\Users\\ABC\\Desktop\\input.txt","r");
	fscanf(pFile,"%d",&T);
	pFile1=fopen("E:\\output.txt","a");
	for(l=1;l<=T;l++)
	 {
		 temp_ch=fgetc(pFile);
	  for(i=0;i<4;i++)
	  {
		  for(j=0;j<4;j++)
		  {
			temp_ch=fgetc(pFile);
			TTT[i][j]=temp_ch;
		  }
		  temp_ch=fgetc(pFile);
	  } 
	  temp_ch=TTT[0][0];
	  //check four rows
	 	for(i=0;i<4;i++)
		  {
			temp_ch=TTT[i][0];
			  for(j=0;j<4;j++)
			  {
				  if(TTT[i][j]=='.')
					  G='E';
				  if(temp_ch!=TTT[i][j] && TTT[i][j]!='T')
					  parity_bit=1;
				  else
				 {
					 temp_ch=TTT[i][j];
					 if(TTT[i][j]!='T'&&TTT[i][j]!='.' )
						 S=TTT[i][j];

				  }
			  }
			  if(!parity_bit)
				  break;
			  else
			  {
					parity_bit=0;
					S=0;
			  }
	  }
		//check four columns
		if(!S)
		{
		for(i=0;i<4;i++)
		  {
			  temp_ch=TTT[0][i];
			  for(j=0;j<4;j++)
			  {
				  if(TTT[j][i]=='.')
					  G='E';
				  if(temp_ch!=TTT[j][i] && TTT[j][i]!='T')
					  parity_bit=1;
				  else
				 {
					 temp_ch=TTT[j][i];
					 if(TTT[j][i]!='T'&&TTT[j][i]!='.' )
						 S=TTT[j][i];

				  }
			  }
			  if(!parity_bit)
				  break;
			  else
			  {
					parity_bit=0;
					S=0;
			  }
	  }
		}
		//check first diagonal
		if(!S)
		{
			temp_ch=TTT[0][0];
			for(i=0;i<4;i++)
			{
			 
				  if(TTT[i][i]=='.')
					  G='E';
				  if(temp_ch!=TTT[i][i] && TTT[i][i]!='T')
					  parity_bit=1;
				  else
				 {
					 temp_ch=TTT[i][i];
					 if(TTT[i][i]!='T'&&TTT[i][i]!='.' )
						 S=TTT[i][i];

				  }
			}
			if(parity_bit)
			{
				S=0;
				parity_bit=0;

			}
		}
		//check second diagonal
		if(!S)
		{
		 temp_ch=TTT[0][3];
			 for(i=0,j=3;i<4,j>=0;i++,j--)
			 { 
					  if(TTT[i][j]=='.')
						  G='E';
					  if(temp_ch!=TTT[i][j] && TTT[i][j]!='T')
						  parity_bit=1;
					  else
					 {
						 temp_ch=TTT[i][j];
						 if(TTT[i][j]!='T'&& TTT[j][i]!='.' )
							 S=TTT[i][j];

					  }
			}
			 if(parity_bit)
				 S=0;
		}
	   if(S=='O')
	   fprintf(pFile1,"Case #%d: %s\n",l,"O won");
	   else if(S=='X')
	   fprintf(pFile1,"Case #%d: %s\n",l,"X won");
	   else if(S==0 && G==0)
	   fprintf(pFile1,"Case #%d: %s\n",l,"Draw");
	   else if(S==0 && G=='E')
	   fprintf(pFile1,"Case #%d: %s\n",l,"Game has not completed");
	   S=0;
	   G=0;
	   parity_bit=0;
	}
	fclose(pFile1);
}