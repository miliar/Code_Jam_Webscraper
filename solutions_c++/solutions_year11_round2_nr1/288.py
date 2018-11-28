/*
TASK: G2011_1B_1 - RPI
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>

#define NMAX 100

using namespace std;

int table[NMAX][NMAX];
double pts[3][NMAX]; //0-WP,1-OWP,2-OOWP

void func()
{
	int n; scanf("%d",&n);
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			char ch; scanf("\n%c",&ch);
			switch(ch){
				case '0':
					table[i][j] = 0;
					break;
				case '1':
					table[i][j] = 1;
					break;
				case '.':
					table[i][j] = -1;
					break;
			}
		}
	}

	for(int i=0;i<n;i++){
		int cnt=0,sum=0;
		for(int j=0;j<n;j++){
			if(-1!=table[i][j]) cnt++;
			if(1==table[i][j]) sum++;
		}
		pts[0][i] = (double)sum/(double)cnt;
	}

	for(int i=0;i<n;i++){
		int cnt=0; double sum=0.0l;
		for(int j=0;j<n;j++){
			if(i==j||-1==table[i][j]) continue;
			int cnt2=0,sum2=0;
			for(int k=0;k<n;k++){
				if(k==i) continue;
				if(-1!=table[j][k]) cnt2++;
				if(1==table[j][k]) sum2++;
			}
			cnt++; sum += (double)sum2/(double)cnt2;
		}
		pts[1][i] = sum/(double)cnt;
	}

	for(int i=0;i<n;i++){
		int cnt=0; double sum=0.0l;
		for(int j=0;j<n;j++){
			if(i==j||-1==table[i][j]) continue;
			cnt++; sum += pts[1][j];
		}
		pts[2][i] = sum/(double)cnt;
	}

	for(int i=0;i<n;i++){
		//printf("wp-%lf ,owp-%lf, oowp-%lf\n",pts[0][i],pts[1][i],pts[2][i]);
		printf("%.12lf\n",0.25l*pts[0][i]+0.5l*pts[1][i]+0.25l*pts[2][i]);
	}

	return;
}

int main()
{
	FILE *fin=NULL,*fout=NULL;
	fin = freopen("input.txt","r",stdin);
	fout = freopen("output.txt","w",stdout);

	int t; scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d:\n",i+1);
		func();
	}

	//finalize
	if(NULL!=fin) fclose(fin);
	if(NULL!=fout) fclose(fout);

	return 0;
}