#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
	int L,D,N;	
	while( cin >> L >> D >> N ){
		
		vector<string> vWord;		
		string word;
		for(int i=0; i < D; ++i){
			cin >> word;
			vWord.push_back(word);
		}
		
		for(int n=0; n < N; ++n){

			//scanf("%s", word);
			cin >> word;
			string str="";
			bool LP=false;
			for(int i=0; i < (int)word.size(); ++i){
				if( word[i] == '(' ) LP=true;
				if( LP == false && word[i] != '(' ){
					str+='('; str+=word[i]; str+=')';					
				}
				else
					str += word[i];
				if( word[i] == ')' ) LP=false;
			}

			int index=0;			
			vector<int> possible(D,0);
			vector<bool> charPossible(D,false);
			for(int c=0; c < (int)str.size(); ++c){
			
				switch(str[c]){
					case '(' : break;
					case ')' : 
						for(int i=0; i < D; ++i)
							if( charPossible[i] == true )
								possible[i]+=1;
						index+=1;
						charPossible.assign(D, false);
						break;
					default:
						for(int i=0; i < D; ++i)
							if( vWord[i][index] == str[c] )
								charPossible[i]=true;
						break;
				}
			}

			int possibleCase=0;
			for(int i=0; i < D; ++i)
				if( possible[i] == L )
					++possibleCase;
			printf("Case #%d: %d\n", n+1, possibleCase);
		}

	}

	return 0;
}
