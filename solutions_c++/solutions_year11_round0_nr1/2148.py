#include<iostream>
#include<stdio.h>

using namespace std;
/*
t- no of test cases
n- no of buttons to be pressed
p- button no to be pressed.
p[i] - i represents the seq no
*/
int ans,n,t,b;
int i,j,k,p,q,z;//iteratr
int c,c1,c2,f,f1,f2;//counter
char ch;
int but[101];
int seq[101];
int p1[101];
int p2[101];
int cost;
int time1[101];
int time2[101];
int w;
int md(int y){
	w = y;	
	if(y < 0)
		w = -1*y;
	return w;
}

int calc(){
cost = 0;
f = 0;
f1 = 0;
f2 = 0;
p = q = 1;
for(z = 0;z < 101;z++){
	time1[z] = time2[z] = 0;
}

for(f1 = 0;f1 < c1; f1++){
	time1[f1] = md(p1[f1] - p) + 1;
	p = p1[f1];
}

for(f2 = 0;f2 < c2; f2++){
	time2[f2] = md(p2[f2] - q) + 1;
	q = p2[f2];
}

f1 = f2 = 0;
//cout << "\nTotal buttons:"<<c;
for(f = 0;f < c; f++){

	if(seq[f] == 1){
		if(time2[f2] > time1[f1])
			time2[f2] -=time1[f1];
		else if(time2[f2] != 0)
			time2[f2] = 1;
		cost += time1[f1++];			
	}
	else{
		if(time1[f1] > time2[f2])
			time1[f1] -=time2[f2];
		else if(time1[f1] != 0)
			time1[f1] = 1;
		cost += time2[f2++];			
	}
	//printing time arrays
	//cout << "\nSeq["<<f<<"] :"<<seq[f];
	//cout <<"\nt1 :"<<time1[f1]<<" t2 :"<<time2[f2];
	//cout <<"\ncost(cum):"<<cost;
   }
}
int main(){
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;
	k = 0;
	while(k<t){
	cost = 0;
	for(i=0;i<=100;i++)
	{
		p1[i] = p2[i] = 0;
	}
	cin >> n;
	//cout <<"\nTotal Buttons:"<<n;
	i = j = 0;
	c = 0;
	c1 = c2 = 0;
	while(c<n){
		cin >> ch;
		cin >> b;
		//cout<<"\nInput is "<<b<<" of "<<ch;
		if(ch == 'O'){
			but[c] = b;
			seq[c] = 1;
			c++;
			p1[c1++] = b;			
		}
		else{
			but[c] = b;
			seq[c] = 2;
			c++;
			p2[c2++] = b;
		}
		//cout << "\nSequence nos c:"<<c<<" c1:"<<c1<<" c2:"<<c2;
	}
	calc();
	k++;
	cout<<"\nCase #"<<k<<": "<<cost;					
	}//uter while
	cout << endl;
}

