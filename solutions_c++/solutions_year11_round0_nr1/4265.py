#include <stdio.h>
#include <memory.h>
#define MAX 105

FILE *fin = stdin;
FILE *fout= stdout;

int N;
int Ans;

struct DATA{
	int bo,x;
};
DATA Data[MAX];

void Input()
{
	int i;
	char alp[5];
	int x;

	fscanf(fin,"%d",&N);
	for(i=1;i<=N;i++){
		fscanf(fin,"%s %d",&alp[1],&x);
		if(alp[1]=='O'){
			Data[i].bo=0;
			Data[i].x=x;
		}else{
			Data[i].bo=1;
			Data[i].x=x;
		}
	}
}
int Abs(int x)
{
	if(x<0) return -x;
	else return x;
}
void Process()
{
	int i;
	int x[2]={1,1};
	int ti=0;

	x[Data[1].bo]=Data[1].x;
	Ans+=Data[1].x;
	ti=Ans;

	for(i=2;i<=N;i++){
		if(Data[i-1].bo==Data[i].bo){
			Ans+=Abs(x[Data[i].bo]-Data[i].x)+1;
			ti+=Abs(x[Data[i].bo]-Data[i].x)+1;
			x[Data[i].bo]=Data[i].x;
		}else{
			if(ti>=Abs(x[Data[i].bo]-Data[i].x)){
				ti=1;
				Ans++;
			}else{
				Ans+=Abs(x[Data[i].bo]-Data[i].x)-ti+1;
				ti=Abs(x[Data[i].bo]-Data[i].x)-ti+1;
			}
			x[Data[i].bo]=Data[i].x;
		}
	}
}
void Output(int t)
{
	fprintf(fout,"Case #%d: %d\n",t,Ans);
}
int main()
{
	int t,i;
	fscanf(fin,"%d",&t);
	for(i=1;i<=t;i++){
		Input();
		Process();
		Output(i);
		Ans=0;
		memset(Data,0,sizeof(Data));
	}
	return 0;
}