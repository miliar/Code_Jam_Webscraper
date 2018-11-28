///By kelwin :)

#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
using namespace std;

void googlerese(string line);
char cambio(char letra);

int main(){
	int num,i;
	char a;
	string l;	
	cin>>num;	
	cin.ignore(1,'\n');
	for (i = 0; i < num; i++){				
		getline(cin,l);
		cout<<"Case #"<<i+1<<": ";
		googlerese(l);
	}
	return 0;
}

void googlerese(string line)
{
	int cant = line.size(),i;
	for (i = 0; i < cant; i++)
	cout<<cambio(line[i]);
	
	cout<<endl;
	
}

char cambio(char letra)
{
	switch (letra)
	{
		case 'a': 
		return 'y';			
			break;
		
		case 'b': 
		return 'h';			
			break;
		
		case 'c':	
		return 'e';		
			break;
			
		case 'd':	
		return 's';		
			break;
			
		case 'e':	
		return 'o';		
			break;
			
		case 'f':	
		return 'c';
			break;
			
		case 'g':	
		return 'v';		
			break;
			
		case 'h':	
		return 'x';		
			break;
			
		case 'i':	
		return 'd';		
			break;
			
		case 'j':	
		return 'u';		
			break;
			
		case 'k':	
		return 'i';		
			break;
			
		case 'l':	
		return 'g';		
			break;
			
		case 'm':	
		return 'l';		
			break;
			
		case 'n':	
		return 'b';		
			break;
			
		case 'o':	
		return 'k';		
			break;
			
		case 'p':	
		return 'r';		
			break;
			
		case 'q':	
		return 'z';		
			break;
			
		case 'r':	
		return 't';		
			break;
			
		case 's':	
		return 'n';		
			break;
			
		case 't':	
		return 'w';		
			break;
			
			
		case 'u':	
		return 'j';		
			break;
			
		case 'v':	
		return 'p';		
			break;
			
				
		case 'w':	
		return 'f';		
			break;
			
			
		case 'x':	
		return 'm';		
			break;
		
		case 'y':	
		return 'a';		
			break;
		
		case 'z':	
		return 'q';		
			break;
						
		default: return ' ';
			
	}
	

}
/**
 a -> y 
 b -> h
 c -> e
 d -> s
 e -> o
 f -> c
 g -> v
 h -> x
 i -> d
 j -> u
 k -> i
 l -> g
 m -> l
 n -> b
 o -> k
 p -> r
 q -> z
 r -> t
 s -> n
 t -> w
 u -> j
 v -> p
 w -> f
 x -> m
 y -> a
 z -> q*/


/**
Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/
