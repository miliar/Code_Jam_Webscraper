#include <iostream>
#include <cstdio>
#include <conio.h>
using namespace std;


int main (void)
	{
	int L,N,D,x,i,p,j,count, lunghezza,n[30],contatore,OK, k;
	char parola[5001][30],testcase[5000],lettera[30][30];
	const char ch=0;

	cin >> L;
	cin >> D;
	cin >> N;
//	cout << "L,D,N=" << L<<D<<N<<"\n";
	cin >> x;
	for(x=0;x<D;x++)
		gets_s(parola[x]);
//	for(x=0;x<D;x++)
//		cout << parola[x]<<"\n";

	for(x=0;x<N;x++)
	{
		gets_s(testcase);
//		cout << testcase<<"\n";
	lunghezza=strlen(testcase);
//	cout << lunghezza;
for(i=0;i<16;i++)
for(j=0;j<16;j++)
lettera[i][j]=ch;

	count=0;
	j=0;
	for(i=0;i<lunghezza;i++){
		if(testcase[i]=='('){
			i++;
			while(testcase[i]!=')') {
				lettera[count][j]=testcase[i];
				i++;
				j++;}
			n[count]=j;
			j=0;
			count++;} else{
				lettera[count][0]=testcase[i];
					n[count]=1;
				count++;}
		}

//			for(p=0;p<count;p++)
//			cout << n[p]<< " " <<lettera[p]<<"\n";
//cout<<"\n";


	contatore=0;
		for(i=0;i<D;i++) //parola i
			{
			for(j=0;j<L;j++) //posizione j
				{
				OK=0;
				for(k=0;k<n[j];k++)
					if(parola[i][j]==lettera[j][k])
						OK=1;
				if(OK==0) break;}
			if(OK==1) contatore++;
			}

		cout << "Case #" << x+1 << ": " << contatore <<"\n";	
		}}