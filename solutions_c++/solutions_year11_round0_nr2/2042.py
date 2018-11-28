#include<iostream>
#include<stdio.h>

using namespace std;
//
//t- no of test cases
//n- no of buttons to be pressed
//p- button no to be pressed.
//p[i] - i represents the seq no
//

unsigned long n,t,b;
unsigned long i,j,k,p,q;//iteratr
unsigned long c,c1,c2,f,f1,f2,d;//counter
char ch;
unsigned long cost;
unsigned long w;
int alphad[201][201];
int alphac[201][201];
char str[4];
char input[101];
char ans[101];
char temp[101];
int x,y,z,zc,zd;
int len,tlen;


int calc(){
cost = 0;
len = 0;
tlen = 0;
int checker;
/*
for(i=0 ;i < 101;i++){
	ans[i] = temp[i] = "";
}
*/
temp[0] = input[0];
tlen = 1;
for(i=1;i < n;i++){
	if(tlen != 0){
	checker = 0;
	x = temp[tlen - 1];
	y = input[i];
	zc = alphac[x][y];
	zd = alphad[x][y];
	//cout << "\nx:"<<char(x)<<" y:"<<char(y)<<" z:"<<z;
	if(zc > 0){
		temp[tlen - 1] = char(zc);
		checker = 1;
		//cout<<"\nCombining "<<char(x)<<" + "<<char(y)<<" = "<<char(zc);
	}	

	if(zc == 0){
		temp[tlen++] = char(y);		
	}
	
	
	//cout << "\n(befre des)temp(in progress):";
	/*	
	for(j = 0;j < tlen;j++)	
		cout << temp[j];
	//*/	
	if(checker == 0){
	int rvr = (tlen - checker) - 1;
	y = temp[rvr];
	//for(j = rvr;j >= 0;j--){		
	for(j = 0;j < (tlen - checker);j++){		
		//x = temp[j];
		x = temp[rvr - j];
		zd = alphad[x][y];
		//cout << "\nx:"<<char(x)<<" y:"<<char(y)<<" z:"<<z;
			if(zd == -1){
				//cout<<"\nDestroying "<<char(x) <<" to "<<char(y);
				//tlen = rvr - j;
				tlen = 0;
				break;
			}
		}
	}
	}
	else{		
		temp[0] = input[i];
		tlen = 1;
	}
	//cout << "\n(after des)temp(in progress):";
	/*	
	for(j = 0;j < tlen;j++)	
		cout << temp[j];
	//*/
}
//cout << "\ntlen:"<<tlen;
//cout << "\ntemp:";
/*
for(j = 0;j < tlen;j++)	
	cout << temp[j];
*/
//len = 0;
//output[0] = "";
}

int main(){

///*
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;
	k = 0;
	while(k<t){
	cost = 0;
	for(i=0;i<=200;i++)
		for(j=0;j<=200;j++){
			alphac[i][j] = 0;
			alphad[i][j] = 0;
		}
	cin >> c;
	for(i = 0;i < c;i++){
		cin >> str;
		x = str[0];
		y = str[1];
		z = str[2];
		alphac[x][y] = z;
		alphac[y][x] = z;
	}
	i = j = 0;
	d = 0;
	cin >> d;
	for(i = 0;i < d;i++){
		cin >> str;
		x = str[0];
		y = str[1];
		z = -1;
		alphad[x][y] = -1;
		alphad[y][x] = -1;
	}
	cin >> n;
	cin >> input;
	//cout <<"\nInput :"<<input << " n:"<<n;
	calc();
	k++;
	cout<<"\nCase #"<<k<<": [";
	i = 0;
	for(i = 0; i < tlen;i++){
		cout << temp[i];
		if(i != tlen -	1)
			cout << ", ";
	}
	cout << "]";
	}//uter while
	cout << endl;
//*/
}

