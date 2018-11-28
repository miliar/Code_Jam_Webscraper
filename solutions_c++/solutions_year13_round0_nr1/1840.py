#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>

using namespace std;

int main(){
	/*freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);*/
	int TC;
	cin>>TC;
	for(int tc=1; tc<=TC; tc++){
		char mat[4][4];
		string linea;
		for(int i=0; i<4; i++){
			cin>>linea;
			for(int c=0; c<linea.length(); c++){
				mat[i][c]=linea[c];
			}
		}
		/*cout<<"la matriz que tengo es: "<<endl;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++)
				cout<<mat[i][j];
			cout<<endl;
		}
		*/	
		bool sirve=false;
		bool empty=false;
		char ganador;
		for(int fila=0; fila<4 && !sirve; fila++){						
			int count[2];
			for(int i=0; i<2; i++)
				count[i]=0;
			for(int col=0; col<4; col++){
				switch(mat[fila][col]){
					case 'X':
						count[0]++;
						break;
					case 'O':
						count[1]++;
						break;
					case 'T':
						count[1]++;
						count[0]++;
						break;
				}				
			}
			if(count[0]==4){
				sirve=true;
				ganador='X';
			}
			if(count[1]==4){
				sirve=true;
				ganador='O';
			}
		}
		for(int col=0; col<4 && !sirve; col++){						
			int count[2];
			for(int i=0; i<2; i++)
				count[i]=0;
			for(int fila=0; fila<4; fila++){
				switch(mat[fila][col]){
					case 'X':
						count[0]++;
						break;
					case 'O':
						count[1]++;
						break;
					case 'T':
						count[1]++;
						count[0]++;
						break;
				}				
			}
			if(count[0]==4){
				sirve=true;
				ganador='X';
			}
			if(count[1]==4){
				sirve=true;
				ganador='O';
			}
		}
		int count1[2],count2[2];
		for(int i=0; i<2; i++){		
			count1[i]=0;
			count2[i]=0;
		}
		for(int i=0; i<4; i++){
			switch(mat[i][i]){
				case 'X':
					count1[0]++;
					break;
				case 'O':
					count1[1]++;
					break;
				case 'T':
					count1[1]++;
					count1[0]++;
					break;	
			}
			switch(mat[i][3-i]){
				case 'X':
					count2[0]++;
					break;
				case 'O':
					count2[1]++;
					break;
				case 'T':
					count2[1]++;
					count2[0]++;
					break;	
			}			
		}
		if(count1[0]==4 ||count2[0]==4){
			sirve=true;
			ganador='X';
		}
		if(count1[1]==4 ||count2[1]==4){
			sirve=true;
			ganador='O';
		}
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(mat[i][j]=='.')
					empty=true;
		cout<<"Case #"<<tc<<": ";
		if(sirve){
			cout<<ganador<<" won";
		}
		else{
			if(empty){
				cout<<"Game has not completed";			
			}
			else{
				cout<<"Draw";
			}
		}
		cout<<endl;
	}	
}
