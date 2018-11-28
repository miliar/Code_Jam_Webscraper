#include<iostream>
#include<vector>

#define VECINT std::vector<int>
#define VV std::vector< std::vector<int> > 

int cyfra(char a);
int wynik(const VV & plansza);

int main(){
	std::ios_base::sync_with_stdio(false);
	
	int T;
	std::cin >> T;
	
	for(int i = 0 ; i < T; ++i){
		VV plansza(4, VECINT(4,0));
		bool dot = false;
		
		for(int w = 0; w < 4; ++w)
			for(int k = 0; k < 4; ++k){
				char a;
				std::cin>> a;
				
				if(a=='.')
					dot = true;
				
				plansza[w][k] = cyfra(a);
			}
		

		int R = wynik(plansza);
		std::cout << "Case #" << (i+1) << ": ";
		if(R==0)
			std::cout << "O won" << std::endl;
		else if(R==1)
			std::cout << "X won" << std::endl;
		else{
			if(dot)
				std::cout << "Game has not completed" << std::endl;
			else
				std::cout << "Draw" << std::endl;
		}

	}
	
	return 0;
}


int cyfra(char a){
	if(a=='O')
		return 0;
	else if(a=='X')
		return 1;
	else if(a=='.')
		return 2;
	else
		return 3;
}

int wynik(const VV & plansza){

	
	for(unsigned int w = 0; w < plansza.size(); ++w){
		VECINT P(4,0);
		for(unsigned int k = 0; k < plansza[w].size(); ++k)
			++P[plansza[w][k]];
		
		if(P[0]==0&&P[2]==0) return 1;
		if(P[1]==0&&P[2]==0) return 0;	
	}
	
	for(unsigned int k=0; k < plansza.size(); ++k){
		VECINT P(4,0);
		for(unsigned int w = 0; w < plansza.size(); ++w)
			++P[plansza[w][k]];
		
		if(P[0]==0&&P[2]==0) return 1;
		if(P[1]==0&&P[2]==0) return 0;
	}
	
	
	{
		VECINT P(4,0);
		
		for(unsigned int k = 0 ; k < plansza.size(); ++k)
			++P[plansza[k][k]];
			
		if(P[0]==0&&P[2]==0) return 1;
		if(P[1]==0&&P[2]==0) return 0;
	}
	
	{
		VECINT P(3,0);
		
		for(unsigned int k = 0 ; k < plansza.size(); ++k)
			++P[plansza[k][plansza[k].size()-1-k]];
			
		if(P[0]==0&&P[2]==0) return 1;
		if(P[1]==0&&P[2]==0) return 0;
	}
	
	return 2;
}
