#include <stdio.h>
FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
int score[1000][1000];
double wp[1000];
double owp[1000];
double oowp[1000];
double rpi[1000];
int n;
void input()
{
	int c,i,j;
	char str[1000];
	fscanf(fin,"%d",&n);
	for (i=0;i<n;i++){
		fscanf(fin,"%s",&str);
		for (j=0;j<n;j++){
			if (str[j] != '.'){
				score[i][j] = str[j]-'0';
			}else{
				score[i][j] = -1;
			}
		}
	}
}
void pro()
{
	int i,j,k;
	int win,team;
	double wnum;
	int wteam;
	for (i=0;i<n;i++){
		win=team=0;
		for (j=0;j<n;j++){
			if (i==j) continue;
			if (score[i][j] == 1) win++;
			if (score[i][j] != -1) team++;
		}
		wp[i] = (double)win/team;
	}
	for (i=0;i<n;i++){
		wteam=0;
		wnum=0;
		for (j=0;j<n;j++){
			if (score[i][j] == -1) continue;
			wteam++;
			team=win=0;
			if (i==j) continue;
			for (k=0;k<n;k++){
				if (j==k || i==k) continue;
				if (score[j][k] != -1) team++;
				if (score[j][k] == 1) win++;
			}
			wnum += (double)win/team;
		}
		owp[i] = wnum/wteam;
	}
	for (i=0;i<n;i++){
		wteam=0;
		wnum=0;
		for (j=0;j<n;j++){
			if (score[i][j] == -1) continue;
			wteam++;
			wnum += owp[j];
		}
		oowp[i] = wnum/wteam;
		rpi[i] = (double)0.25*wp[i] + (double)0.5*owp[i] + (double)0.25*oowp[i];
	}
}
void output()
{
	int i;
	for (i=0;i<n;i++){
		fprintf(fout,"%lf\n",rpi[i]);
	}
}
int main()
{
	int i,t;
	fscanf(fin,"%d",&t);
	for (i=0;i<t;i++){
		input();
		pro();
		fprintf(fout,"Case #%d:\n",i+1);
		output();
	}
}