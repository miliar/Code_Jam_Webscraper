#include<iostream>
#include<map>
#include<list>
#include<cmath>

using namespace std;

class ms{

	public:
	int cor;
	int butao;

	
	ms(int but, char cor): cor(cor), butao(but) {}
};

int main(){

	int cases;

	cin>> cases;
	

	for(int i = 0 ; i < cases; i++){
		
		int n;
		cin>> n;
	
		list<int> movesO;
		list<int> movesB;
		list<ms> movesAll;

		//posicao[0] = O
		//posicao[1] -= B
		int posicao[2]= {1,1};
//		int posicaoB = 1;
//		int posicaoO = 1;

		for(int j = 0; j < n; j++){
			char r;
			int b;
			int cor;
			cin>>r>>b;
		
//			cout<<r<<" "<<b<<endl;
		
			if ( r == 'O'){
				cor = 0;
				movesO.push_back(b);
			}
			else{
				cor = 1;
				movesB.push_back(b);
			}
			
			ms m(b,cor);
			movesAll.push_back(m);
		}

		int total_moves = 0;
		while(!movesAll.empty()){
			ms next = movesAll.front();
			movesAll.pop_front();
			int ocor = next.cor;
			int obutao = next.butao;
			int outrocara = 0;
			int moves = 0;
			int outrocaraobj = 0;

//			cout<<"carinha atual  = "<< ocor <<endl;

			if(ocor == 0){
				outrocaraobj = movesB.front();
				outrocara = 1;
				
				if(!movesO.empty())
					movesO.pop_front();
			}
			else{
				outrocaraobj = movesO.front();
				outrocara = 0;
				
				if(!movesB.empty())
					movesB.pop_front();
			}

			moves = abs(posicao[ocor] - obutao) + 1; // + 1 eh apertar o butao
//			cout<<"moves = "<<moves<<endl;
			posicao[ocor] = obutao;

			total_moves += moves;

//			cout<<"outrocara = "<<outrocara<<endl;
//			cout<<"outrocara obj = "<< outrocaraobj<<endl;

			//da pra mover o outro cara para o lugar correto?
			if(  posicao[outrocara] + moves <= outrocaraobj   && posicao[outrocara] - moves >= outrocaraobj ||
			(  posicao[outrocara] + moves >= outrocaraobj   && posicao[outrocara] - moves <= outrocaraobj )) {
				
				posicao[outrocara] = outrocaraobj;			

			}
			else{
				if(posicao[outrocara] < outrocaraobj){
					posicao[outrocara] += moves ;
				}
				else{
					posicao[outrocara] -= moves ;
				}
		
			}
//			cout<<"posicao["<<outrocara<<"] = "<< posicao[outrocara]<<endl;
			
			
		}

		cout<<"Case #"<< i+1 << ": " << total_moves<<endl;

	}





	return 0;



}




