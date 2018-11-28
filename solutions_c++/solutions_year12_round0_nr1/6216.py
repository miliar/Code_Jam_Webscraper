#include <stdio.h>

int index=1;
FILE *baca = fopen("A-small-attempt7.in","r") ;
FILE *tulis= fopen("Jawaban.txt","w");

void ganti(char kata);

void main (){

	int input;
	char kata;
	

	fprintf(tulis,"Case #%d: ",index++);

	


	if(baca==NULL){printf("Tidak Terbaca");}
	else{
	
	
		fscanf(baca,"%d\n",&input);	

		fscanf(baca,"%c",&kata);
		ganti(kata);


		while(!feof(baca)){
		
			fscanf(baca,"%c",&kata);
			ganti(kata);

			
		
		}
	
	
		
	
	
	
	
	
	}





	fclose (baca);
	fclose(tulis);
	
getchar();
}

void ganti(char kata){

	switch (kata){
	
		case ' ':
		fprintf(tulis," ");
	break;

	case 'a':
		fprintf(tulis,"y");
	break;
	
	case 'b':
		fprintf(tulis,"h");
	break;
	case 'c':
		fprintf(tulis,"e");
	break;
	case 'd':
		fprintf(tulis,"s");
	break;
	case 'e':
		fprintf(tulis,"o");
	break;
	
	case 'f':
		fprintf(tulis,"c");
	break;
	case 'g':
		fprintf(tulis,"v");
	break;
	
	case 'h':
		fprintf(tulis,"x");
	break;
	case 'i':
		fprintf(tulis,"d");
	break;
	
	case 'j':
		fprintf(tulis,"u");
	break;
	
	case 'k':
		fprintf(tulis,"i");
	break;
	case 'l':
		fprintf(tulis,"g");
	break;
	
	case 'm':
		fprintf(tulis,"l");
	break;

	case 'n':
		fprintf(tulis,"b");
	break;

	case 'o':
		fprintf(tulis,"k");
	break;

	case 'p':
		fprintf(tulis,"r");
	break;

	case 'q':
		fprintf(tulis,"z");
	break;

	case 'r':
		fprintf(tulis,"t");
	break;

	case 's':
		fprintf(tulis,"n");
	break;

	case 't':
		fprintf(tulis,"w");
	break;

	case 'u':
		fprintf(tulis,"j");
	break;

	case 'v':
		fprintf(tulis,"p");
	break;

	case 'w':
		fprintf(tulis,"f");
	break;

	case 'x':
		fprintf(tulis,"m");
	break;

	case 'y':
		fprintf(tulis,"a");
	break;

	case 'z':
		fprintf(tulis,"q");
	break;

	case '\n':
		fprintf(tulis,"\n");
		fprintf(tulis,"Case #%d: ",index++);
	break;
	}



}
