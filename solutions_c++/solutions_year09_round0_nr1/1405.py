#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>
#include <conio.h>

using namespace std;

#define lint long long

#define ss stringstream
#define pb push_back
#define sz size()
#define FOR(i,n) for(i=0;i<n;i++)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

int A[30][20];
int main()
{
	int n,l,d;
	memset(A,0,sizeof(A));
	int i,j,k;
	FILE * f1 = fopen("A-large.in","r");
	FILE * f2 = fopen("A-large1.out","w");
	fscanf(f1,"%d%d%d",&l,&d,&n);
	vector <string> dic;
	string str;
	char buf[505];
	FOR(i,d) {
		fscanf(f1,"%s",buf);
		str = string(buf);
		dic.pb(str);
	}
	vector <string> r;
	FOR(i,n) {
		fscanf(f1,"%s",buf);
		str = string(buf);
		r.pb(str);
	}
	
	FOR(j,n){
		memset(A,0,sizeof(A));
		bool check=true;
		int k=0,res=0;
		FOR(i,r[j].sz)
		{
			if (r[j][i]==')') check=true;
			if (r[j][i]=='(') check=false;
			if ((r[j][i]!=')')&&(r[j][i]!='(')) A[r[j][i]-'a'][k]=1;
			if (check) k++;

		}
		
		FOR(i,d){
		int temp=1;
		FOR(k,l) temp*=A[dic[i][k]-'a'][k];
		res+=temp;
		}

		fprintf(f2,"Case #%d: %d\n",j+1,res);
	}

	fclose(f1);
	fclose(f2);
	return 0;
}