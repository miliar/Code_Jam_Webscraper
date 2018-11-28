#include <iostream>
#include <fstream>
#include <cstring>
#include <stack>
using namespace std;

#define salida fout

char matriz[4][4];

int moves[8][2]={{0,1},
				 {1,1},
				 {1,0},
				 {1,-1},
				 {0,-1},
				 {-1,-1},
				 {-1,0},
				 {-1,1}};

typedef pair<int,int> pii;

int main()
{
	int dim=4,T,caso=1;
	char c;
	//X uma 1 - 0 suma 20
	//X gana con 4 o 3
	//0 gana con 60 o 80
	ifstream fin("a_chico2.in");
	ofstream fout("salidachico.txt");
	fin>>T;
	while(T--){
		int cuentaRow;
		int cuentaCol[4]={0,0,0,0};
		bool notComplete=false;
		bool gameOver=false;
	
		salida<<"Case #"<<caso<<": ";
		
		for(int i=0;i<dim;i++){
			cuentaRow=0;
			for(int j=0;j<dim;j++){
				fin>>c;
				matriz[i][j]=c;
				if(c=='X') {
					cuentaCol[j]+=1;
					cuentaRow+=1;
				}
				else if(c=='O'){
					cuentaCol[j]+=20;
					cuentaRow+=20;
				}
				else if(c=='.'){
					notComplete=true;
					cuentaCol[j]+=100;
					cuentaRow+=100;	
				}
			}
			
			
			//cout<<"f-"<<cuentaRow<<" "<<endl;
			//check de fila
			if (cuentaRow==3 || cuentaRow==4){
				salida<<"X won"<<endl; 
				gameOver=true;
			}
			if (cuentaRow==60 || cuentaRow==80){
				salida<<"O won"<<endl; 
				gameOver=true;
			}
		}
	
	
	
		//check columnas
		if(gameOver==false){
			for(int i=0;i<4;i++){
				if (cuentaCol[i]==3 || cuentaCol[i]==4){
					gameOver=true;
					salida<<"X won"<<endl; 
					break;
				}
				else if (cuentaCol[i]==60 || cuentaCol[i]==80){
					gameOver=true;
					salida<<"O won"<<endl; 
					break;
				}
			}
		}
	
		//diagonales - son 2
		int diag1=0,diag2=0;
		if(gameOver==false){
			for(int i=0;i<4;i++){
				char c=matriz[i][i];
				if(c=='X')
					diag1+=1;
				else if(c=='O')
					diag1+=20;
				else if(c=='.')
					cuentaRow+=100;
			}
		
			if (diag1==3 || diag1==4){
				gameOver=true;
				salida<<"X won"<<endl; 
			}
		
			else if (diag1==60 || diag1==80){
					gameOver=true;
					salida<<"O won"<<endl; 
			}
		}

	
	
	
	
	
		if(gameOver==false){
			for(int i=0;i<4;i++){
				char c=matriz[i][3-i];
				if(c=='X')
					diag2+=1;
				else if(c=='O')
					diag2+=20;
				else if(c=='.')
					cuentaRow+=100;
			}
	
			if (diag2==3 || diag2==4){
				gameOver=true;
				salida<<"X won"<<endl; 
			}
		
			else if (diag2==60 || diag2==80){
					gameOver=true;
					salida<<"O won"<<endl; 
			}
		}
	
	
		//tie?
		if(gameOver==false){
			if(notComplete)
				salida<<"Game has not completed"<<endl;
			else
				salida<<"Draw"<<endl;
		}
		caso++;
	}

	return 0;
}
