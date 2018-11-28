#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

long long power (long long base, long long n) {
    long long i,p=1;
    for (i=1;i<=n;++i)
	p*=base;
	if (n==0)
	p=1;
    return p;
}
long long bin_dec(char *number){
   long long tnum1=0,tnum2,tnum3=0;
   while(number[tnum1]!='\0'){
   tnum2=number[tnum1]-48;
   tnum3+=tnum2*power(2,strlen(number)-tnum1-1);  
   tnum1++;
   }
   return tnum3; 
}
char *dec_bin(long long number){
char *res=new char[22];
long long i=0;
while(number>0){
for(int j=i-1;j>=0;j--) res[j+1]=res[j];
res[0] = (number % 2)+48;
i++;
number=(number / 2);
}res[i]='\0';
return res;
}
char *stupid_add(char *bin1,char *bin2){
	char *temp=new char[22];
	int tmp=strlen(bin1)-strlen(bin2);
	for(int i=0;i<max(strlen(bin1),strlen(bin2));i++){
		if(tmp<0){temp[i]=bin2[i];if((i+tmp)>=0)temp[i]+=bin1[i+tmp]-48;}
		if(tmp>=0){temp[i]=bin1[i];if((i-tmp)>=0)temp[i]+=bin2[i-tmp]-48;}
		if(temp[i]>49)temp[i]=48;
	}temp[max(strlen(bin1),strlen(bin2))]='\0';
	return temp;
}
void ACT(long long *DATA,int *FORS,int KO,int *ANS,int N){
	long long TM1=0,TM2=0;
	char *T1=new char[22],*T2=new char[22];
	T1=dec_bin(0);
	T2=dec_bin(0);
	vector<long long> a,b;
	for(int i=0;i<N;i++) a.push_back(DATA[i]);
	for (int i=1;i<=KO;i++) {a.erase(a.begin()+FORS[i]); b.push_back(DATA[FORS[i]]);}
	for (int i=0;i<a.size();i++){TM2+=a.at(i);T2=stupid_add(T2,dec_bin(a.at(i)));}
	for (int i=0;i<b.size();i++){TM1+=b.at(i);T1=stupid_add(T1,dec_bin(b.at(i)));}
	if(b.size()>0 && a.size()>0)if(bin_dec(T1)==bin_dec(T2))if(TM1>*ANS){*ANS=TM1;
	/*cout<<"--------------------------------\n";
	for (int i=0;i<a.size();i++) cout<<a.at(i)<<"  ";
	cout<<"||"<<TM2<<" +"<<T2<<endl;
	for (int i=0;i<b.size();i++) cout<<b.at(i)<<"  ";
	cout<<"||"<<TM1<<" +"<<T2<<endl;
	*/}
}
void Fors(int *FORS,long long *DATA,int N, int F,int KO,int *ANS){
	FORS[F]=FORS[F+1]+1;
	if(F>1){
		while(FORS[F]<N) Fors(FORS,DATA,N,F-1,KO,ANS);
	}else{
		while(FORS[1]<N){
			ACT(DATA,FORS,KO,ANS,N);
			FORS[1]++;
		}
	}
	if(FORS[F]==N){FORS[F+1]++;}
}

int main(){
ifstream input;
ofstream output;
input.open("d:/input.in");
output.open("d:/output.in");
int N,FORS[1001];
long long Ns[1001];
input>>N;
for(int i=1;i<=N;i++){
	output<<"Case #"<<i<<": ";
	cout<<"Case #"<<i<<": ";
	int T,tm1,tm2,big=0;
	input>>T;
	for(int j=0;j<T;j++) input>>Ns[j];
	int *ANS=new int();
	*ANS=0;
	for(int j=1;j<T;j++){	
		FORS[j+1]=-1;
		Fors(FORS,Ns,T,j,j,ANS);
	}




	if(*ANS>0){output<<*ANS<<endl; cout<<*ANS<<endl;}else{output<<"NO"<<endl; cout<<"NO"<<endl;}
}
system("pause");
return 0;
}