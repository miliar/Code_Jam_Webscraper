#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<omp.h>

unsigned int Opos,Bpos,time;
unsigned int Osteps,Bsteps;


void init();
void output(int,FILE*);
void read_file(char*,char*);
void read_line(FILE*);
void solve(char,unsigned int);

void init()
{
	Opos=Bpos=1;
	time=Osteps=Bsteps=0;
}
void output(int cse,FILE *fp)
{
	fprintf(stdout,"Case #%d: %d\n",cse,time);
	fprintf(fp,"Case #%d: %d\n",cse,time);
}

void read_file(char *inf,char *outf)
{
	FILE *fp=NULL,*of=NULL;
	fp=fopen(inf,"r");
	of=fopen(outf,"w");
	if(fp!=NULL && of!=NULL){
		unsigned int y=0;
		fscanf(fp,"%d",&y);

		for(int i=0;i<y;i++){
			read_line(fp);
			output(i+1,of);
			init();
		}
		fclose(of);
		fclose(fp);
	}

}

void read_line(FILE *fp)
{
	unsigned int butt=0,x=0;
	unsigned char bot;

	fscanf(fp,"%d ",&x);
	for(int i=0;i<x;i++){
			fscanf(fp,"%c %d ",&bot,&butt);
			solve(bot,butt);
	}
	
}

void solve(char bot,unsigned int goal)
{
	unsigned int action=0;
	if(bot=='O'){
		if( Opos < goal ) action= (goal - Opos) + 1; else action= (Opos - goal) + 1;
		if(Bsteps < action){
			time+=action-Bsteps;
			Osteps+=action-Bsteps;
		}else if(Bsteps >= action){
			time+=1;
			Osteps+=1;			
		}
		Opos=goal;
		Bsteps=0;
	}else{
		if( Bpos < goal ) action= (goal - Bpos) + 1; else action= (Bpos - goal) + 1;
		if(Osteps < action){
			time+=action-Osteps;
			Bsteps+=action-Osteps;
		}else if(Osteps >= action){
			time+=1;
			Bsteps+=1;
		}
		Bpos=goal;
		Osteps=0;
	}
}
void solveA(char bot,unsigned int goal)
{
	unsigned int action=0;
	if(bot=='O'){
		if( Opos < goal ) action= (goal - Opos)+1; else action= (Opos - goal)+1;
		if(Bsteps < action){
			time+=action-Bsteps;
		}else if(Bsteps >= action){
			time+=1;
		}
		Opos=goal;
		Osteps+=action;
		Bsteps=0;
	}else{

	}

}
int main(int argc, char **argv )
{
	char input[50],output[50];
	if(argv[1]==NULL){ printf("Error:Input File Missing\n"); exit(1);}
	if(argv[2]==NULL){ printf("Error:Output File Missing\n"); exit(1);}
	strcpy(input,argv[1]);
	strcpy(output,argv[2]);
	init();
	read_file(input,output);

}


