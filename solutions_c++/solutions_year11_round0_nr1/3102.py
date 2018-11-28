#include <iostream>
#include <queue>


unsigned solve(std::queue < std::pair <int,int> > &O, 
				std::queue < std::pair <int,int> > &B){

 unsigned time = 0;
 int Opos = 1,Bpos = 1;
 while ( !O.empty() && !B.empty() )
	{
		if (O.front().second < B.front().second){
			if(O.front().first == Opos)
				O.pop();
			else if (O.front().first > Opos) Opos++;
				 else Opos--;
			
			if (B.front().first > Bpos) Bpos++;
			else if (B.front().first < Bpos) Bpos--;
			} else {
			if(B.front().first == Bpos)
				B.pop();
			else if (B.front().first > Bpos) Bpos++;
				 else Bpos--;
			
			if (O.front().first > Opos) Opos++;
			else if (O.front().first < Opos) Opos--;
			}
	time++;
	}

 while (!O.empty()){
	if(O.front().first == Opos)
		O.pop();
	else if (O.front().first > Opos) Opos++;
		 else Opos--;
 time++;
 }

 while (!B.empty()){
	if(B.front().first == Bpos)
		B.pop();
	else if (B.front().first > Bpos) Bpos++;
		else Bpos--;
 time++;
 }
return time;
}


int main(int argc, char ** argv){

 std::queue < std::pair <int,int> > O;
 std::queue < std::pair <int,int> > B;
 unsigned i,j,b, N, T;
 char R;
 std::cin >> T;
 for(i=0;i<T;i++){
 	std::cin >> N;
 	for(j=0;j<N;j++){
		std::cin >> R;
		std::cin >> b;
		if (R == 'O') O.push(std::make_pair(b,j));
		else if (R == 'B') B.push(std::make_pair(b,j));
 	}
	std::cout<< "Case #" << i+1<< ": " << solve(O,B)<<std::endl;
 }



return 0;
}

