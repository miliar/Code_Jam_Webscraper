//2009Äê9ÔÂ3ÈÕ Google Code Jam
//Alien Language
#include<iostream>
#include<stdlib.h>
using namespace std;

struct DICT{
	char word[16];
	bool match;
};

struct TEST{
	char letter[26];
	int token;
};

int main()
{
	int L=0, D=0, N=0;
	TEST test[15] = {};
	DICT dict[5000] = {};
		
	cin>>L>>D>>N;
	for(int i = 0; i<D; i++)
		cin>>dict[i].word;
	cin.get();
	for(int c=1; c<=N; c++){
		for(int i = 0; i<5000; i++){
			dict[i].match = true;
		}
		memset(test, 0, sizeof(test));
		
		for(int i = 0; i<L; i++){
			if(cin.peek() == '('){
				cin.get();
				while(cin.peek() != ')'){
					cin.get(test[i].letter[test[i].token]);
					test[i].token ++;
				}
				cin.get();
			}
			else{
				cin.get(test[i].letter[test[i].token]);
				test[i].token = 1;
			}
			
			for(int j = 0; j<D; j++){
				bool temp = false;
				for(int k = 0; k<test[i].token; k++){
					if(dict[j].word[i] == test[i].letter[k]){
						temp = true;
						break;
					}
				}
				if(temp == false)
					dict[j].match = false;
			}
		}
		cin.get();
		
		int result = 0;
		for(int i = 0; i<D; i++){
			result += dict[i].match;
		}
		cout<<"Case #"<<c<<": "<<result<<endl;
	}
	return 0;
}
