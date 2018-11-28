#include<iostream>
#include<string>
#include<math.h>
#include<fstream>
using namespace std;

bool espalin(int n){  
     int num, digit,rev = 0;
     num=n;
     do{
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
   //S cout<<n<<" "<<rev<<endl;
     if (n == rev){
       return true;//cout<<"espalin"<<endl;
     }else{
       return false;}

} 

bool superpalin(int n){
	int num,digit,rev=0;
	num=n;
	bool super=true;
	digit=num%10;
	do{
	if(num%10!=digit)super=false;
	num=num/10;
	}while(num!=0);
//if(super)cout<<num<<endl;
return super;

}  

int main(){
ifstream fin;
ofstream fout;
fin.open("C-small-attempt0.in",ifstream::in);
fout.open("C-small-attempt0.out",ofstream::out);
string a;
int A,B,tam,cont;
int t,k,cases=1;
fin>>t;
while(t--){
fin>>a;
fin>>B;
k=a.length();
A = atoi(a.c_str());
int number;
int aux,aux2;
cont=0;
for(number=A;number<=B;number++){

aux2=number;
	for(int i=1;i<k;i++){
	
	aux=aux2%10;
	
	aux2=aux2/10;
	
		for(int v=0;v<k-1;v++){aux=aux*10;}
	
	aux2=aux2+aux;
	
	if(aux2<=B&&aux2>=A&&!espalin(aux2)){cont++;//cout<<number<<" -> "<<A<<"<"<<aux2<<"<"<<B<<endl;}
	}
	if(aux2<=B&&aux2>=A&&espalin(aux2)&&k>2){if(!superpalin(aux2))cont++;//cout<<number<<" -> "<<A<<"<"<<aux2<<"<"<<B<<endl;}
	
	
	}
		
}
}
fout<<"Case #"<<cases<<": "<<cont/2<<endl;
cases=cases+1;


}
}
