// a.cpp, Stefan Veis Pennerup, kumuluzz@gmail.com
// Description: Program for the qualification round, google code jam 2012

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	int T,t;
	char eng[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char goo[26] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	int i,j; //a b c d e f g h i j k l m n o p q r s t u v w x y w z
	char x;  //y n f i c w l b k u o m x s e v z p d r j g a t h a q

	ifstream input ("small.in");
	ofstream output ("small-output.txt");

	if(!input.is_open())
		cout << "File could not be opened" << endl;
	else{
			input >> T;
			x= input.get();
		
			for(t=0;t<T;t++){
				output << "Case #" << t+1 << ": ";
				
				do{
					x = input.get();
					if(x == ' '){
						output << " ";
					}
					else{
						for(i=0;i<26;i++){
							if(x == goo[i])
								output.put(eng[i]);
						}
					}
				}while(x!='\n');

				output << endl;
			}
		
	}

	return 0;
}
