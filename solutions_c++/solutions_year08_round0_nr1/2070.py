#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int N;		//number of cases

class Case{

public:
	
	int S;		//number of search engines
	int Q;		//number of queries
	int answer;
	string *name;

	Case(fstream &f){

		this->answer=0;
		f>>this->S;
		
		name = new string[this->S];

		for(int i=0;i<S;i++){

			name[i]=this->getln(f);
		}
	}

	string getln(fstream &f){
	
		string temp;
		f>>temp;
		char x;
			
		f.read(&x,1);
		if(x!=10){

			while(true){

				string stemp;
				f>>stemp;
				temp.append(" ");
				temp.append(stemp);

				f.read(&x,1);
				if(x==10)
					break;
			}
		}
		return temp;
	}

	int eslestir(string &Str){

		for(int i=0;i<this->S;i++)
			if(!Str.compare(this->name[i]))
				return i;
	}

	int sifirvarmi(int *dizi,int sayi){

		for(int i=0;i<sayi;i++)
			if(dizi[i]==0)
				return 1;
		return 0;
	}

	int solve(fstream &f){

		this->answer=0;
		int *temp;
		temp = new int[this->S];
		for(int i=0;i<this->S;i++)
			temp[i]=0;

		string solvetemp;

		f>>this->Q;

		for(int i=0;i<this->Q;i++){
	
			solvetemp=this->getln(f);
			temp[this->eslestir(solvetemp)]++;

			if(!sifirvarmi(temp,this->S)){

				answer++;
				for(int i=0;i<this->S;i++)
					temp[i]=0;
				temp[this->eslestir(solvetemp)]++;
			}

		}
		return answer;
	}

};

int main(){

	fstream f,f2;
	f.open("A-small.in",ios::in);
	f>>N;

	f2.open("A-small.out",ios::out);

	for(int i=1;i<=N;i++){

		Case C(f);
		int ans;
		ans = C.solve(f);
		//system("pause");
		f2<<"Case #"<<i<<": "<<ans<<endl;
	}

	f.close();
	f2.close();
	return 1;
}