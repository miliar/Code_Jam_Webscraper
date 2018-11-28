#include<iostream>
#include<string>
#include<list>
#include<fstream>


using namespace std;

void getLetterCombinations(char a[], string b[]);
bool searchChar(char a, string b);


void main(){

	ifstream in;
	ofstream out;
	out.open("A-Large.out");
	in.open("A-Large.in");

	unsigned int L=0; char l[10];
	unsigned int D=0; char d[10];
	unsigned int N=0; char n[10];

	in.getline(l,10,' ');	L = atoi(l);
	in.getline(d,10,' ');	D = atoi(d);
	in.getline(n,10);		N = atoi(n);

	list<string> Dictionary;
	
	char temp[20];
	while(Dictionary.size() < D){
		in.getline(temp,20);
		string newWord(temp);
		Dictionary.push_back(newWord);
	}

	Dictionary.sort();

	unsigned int cases=0;

	while(cases<N){
		
		char temp[1000]; 
		in.getline(temp,1000);

		string letters[20];
		getLetterCombinations(temp,letters);

		list<string> Dict(Dictionary); 
		list<string>::iterator Di;

		int Dz = Dict.size();
	
		for (unsigned int count=0; count<L; count++){
		
			for( Di=Dict.begin(); Di != Dict.end();){
				string l = Di->data();

				if(searchChar(l[count],letters[count])==false)
					Di = Dict.erase(Di);
				else
					Di++;
			}
		}

		cases++;

		Dz = Dict.size();

		cout<<"Case #"<<cases<<": "<<Dz;
		out<<"Case #"<<cases<<": "<<Dz;

		if(cases<N){
			cout<<endl;
			out<<endl;
		}
	}

	in.close();
	out.close();
}


void getLetterCombinations(char a[], string b[]){
	
	int counter = 0;
	int m = strlen(a);
	for(int x=0; x<m; x++){

		if(a[x]=='('){
			x++;
			while(a[x]!=')'){
				b[counter]+=a[x];
				x++;
			}
		}

		else 
			b[counter]+=a[x];
		
		counter++;
	}
}

bool searchChar(char a, string b){

	for(unsigned int c=0; c<b.size(); c++)
			if(a == b[c])
				return true;

	return false;
				

}