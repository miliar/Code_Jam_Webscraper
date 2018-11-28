#include <stdio.h>
#include <vector>
#define MAX 1005
using namespace std;

FILE *fin = stdin;
FILE *fout = stdout;



struct DY{
	int x,max;
};

int N;
int Arr[MAX];
int Sum,Max,Xor;
int Ans;

vector<DY> Dy[2];

void Input()
{
	int i;
	fscanf(fin,"%d",&N);

	for(i=1;i<=N;i++){
		fscanf(fin,"%d",&Arr[i]);
		Sum+=Arr[i];
		Xor=Xor^Arr[i];
		Max=Max<Arr[i] ? Arr[i] : Max;
	}
}
void Process()
{
	int i,j;
	int num;
	DY a;

	a.x=0;
	a.max=0;

	Dy[0].push_back(a);
	for(i=1;i<=N;i++){
		for(j=0;j<(signed)Dy[0].size();j++){
			a.x=Dy[0][j].x^Arr[i];
			a.max=Dy[0][j].max+Arr[i];
			Dy[1].push_back(a);
		}
		Dy[1].insert(Dy[1].end(),Dy[0].begin(),Dy[0].end());
		Dy[0]=Dy[1];
		Dy[1].resize(0);
	}
	Ans=-1;
	for(i=0;i<(signed)Dy[0].size();i++){
		if( (Xor^Dy[0][i].x) == Dy[0][i].x && Dy[0][i].max!=Sum){
			Ans=Ans<Dy[0][i].max ? Dy[0][i].max : Ans;
		}
	}
}
void Output(int t)
{
	if(Ans==-1) fprintf(fout,"Case #%d: NO\n",t);
	else fprintf(fout,"Case #%d: %d\n",t,Ans);
}
int main()
{
	int t,i;
	fscanf(fin,"%d",&t);
	for(i=1;i<=t;i++){
		Input();
		Process();
		Output(i);
		Max=0;
		Xor=0;
		Sum=0;
		Dy[0].resize(0);
	}
	return 0;
}