#include <iostream>
#include <fstream>

using namespace std;

void setDigits(char stream[] , int alien[] , int alienS, int &base);
int convert(int alien[], int base, int res[], int s);
int search(char stream[], int alien[], char n, int s);
int power(int base, int exponent);


void main(){

	ifstream in;
	in.open("A-small-attempt1.in");
	ofstream out;
	out.open("A-small-attempt1.out");

	char stream[1000];

	in.getline(stream,1000);
	int cases = atoi(stream);

	int C = 0;
	while(C<cases){
		C++;
		
		
		in.getline(stream,1000);
		int alien[100];
		int alienS = strlen(stream);
		int base = 0;
		setDigits(stream,alien,alienS,base);
		int res[100];
		int dec = convert(alien,base,res,alienS);


		cout<<"Case #"<<C<<": "<<dec<<endl;
	

		out<<"Case #"<<C<<": "<<dec<<endl;
			
	}

	out.close();
	in.close();
}

void setDigits(char stream[] , int alien[] , int alienS, int &base){

	if(alienS>=1)
		alien[0]=1;
		
	int b=0;
	for(int x=1; x<alienS; x++){

			int r = search(stream,alien,stream[x],x);
			if(r!=-1)
				alien[x]=r;
			else{
				alien[x]=b;
				b++;
				if( b==1)
				b++;
			}

			//cout<<alien[x];
			
	}
	//cout<<" \t";
	base=b;
	if(base==0)
		base=2;
}
int convert(int alien[], int base, int res[], int s){

	int decimal=0;

	if(base==1)
		base++;
	cout<<base;
		
		for(int index=s-1 , ex=0 ; index>=0; ex++, index--){

			int temp = alien[index] * power(base,ex);
			decimal = decimal + temp;

			

		}
		
		return decimal;

}

int power(int base, int exponent){

	if(exponent==0)
		return 1;
	else if(exponent==1)
		return base;

	else if(exponent%2==0)
		return power(base*base,exponent/2);

	else 
		return power(base*base,exponent/2)*base;
}

int search(char stream[], int alien[], char n, int s){
	for(int x=0; x<s; x++){
		if(stream[x]==n)
			return alien[x];
	}

	return -1;
}

