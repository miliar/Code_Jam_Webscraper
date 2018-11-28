#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;
//
//t- no of test cases
//n- no of buttons to be pressed
//p- button no to be pressed.
//p[i] - i represents the seq no
//

unsigned long n,t,b;
unsigned long i,j,k,p,q;//iterator
unsigned long c1,c2,f,f1,f2,d;//counter
char ch;
unsigned long cost;
unsigned long w,chk,sum,rsum;
unsigned long c[10001];
char str[4];
unsigned long temp[10001];
unsigned long ans[10001],num[10001];
unsigned long p2[10001],n2[10001];
unsigned long p1[10001],n1[10001];
char s1[205];
char s2[205];
int x,y,z,zc,zd;
int len,tlen;


unsigned long add(unsigned chk1, unsigned chk2)
{
  unsigned long xor1, and1, temp;

  and1 = chk1 & chk2; //start-marker// Obtain the carry bits //end-marker//
  xor1 = chk1 ^ chk2; //start-marker// resulting bits //end-marker//
  /*  
  while(and1 != 0 ) //start-marker// stop when carry bits are gone //end-marker//
  {
    and1 <<= 1; //start-marker// shifting the carry bits one space //end-marker//
    temp = xor1 ^ and1; //start-marker// hold the new xor result bits//end-marker//
    and1 &= xor1; //start-marker// clear the previous carry bits and assign the new carry bits //end-marker//
    xor1 = temp; //start-marker// resulting bits //end-marker//
  }
  */	
  return xor1; //start-marker// final result //end-marker//
}

int calc(){
	cost = 0;
	c1 = c2 = 0;
	for(i = 0;i < 10001;i++){
		p1[i] = p2[i] = 0;
	}
	sum = 0;
	rsum = 0;
	for(i = 0;i < n ;i++){
		sum = add(sum,c[i]);
		rsum += c[i]; 
	}
	if(sum != 0){
		cost = -1;
		return cost;	
	}
	sort(num,num + n);
	cost = rsum - num[0];
	return cost;
}

int main(){

	cin >> t;
	//cout<<"Total cases:"<<t<<endl;
	k = 0;
	while(k<t){
	cost = 0;
	cin >> n;
	for(i = 0;i < n;i++){
		cin >> c[i];
		num[i] = c[i];
	}
	//cout <<"\nInput :"<<input << " n:"<<n;
	cost = calc();
	k++;
	cout<<"\nCase #"<<k<<": ";
	if(cost == -1){
		cout << "NO";
	}
	else
		cout << cost;
	}//uter while
	cout << endl;

}

